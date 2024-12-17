import os
from utils import get_vector_store, extract_text_from_pdfs_parallel
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from concurrent.futures import ThreadPoolExecutor

# Step 2: Chunk Text for Embedding
def chunk_text(documents, chunk_size=250, overlap=40):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    
    def process_doc(doc):
        chunks = []
        for chunk in splitter.split_text(doc["text"]):
            chunks.append({"text": chunk, "source": doc["source"]})
        return chunks
    
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_doc, documents)

    return [chunk for result in results for chunk in result]

# Step 3: Embed and Store in ChromaDB
def create_vector_db(chunks, persist_dir="./chroma_db"):
    documents = [
        Document(page_content=chunk["text"], metadata={"source": chunk["source"]})
        for chunk in chunks
    ]

    vector_store=get_vector_store(persist_dir=persist_dir)

    vector_store.add_documents(documents)

    return vector_store

# Main Execution
if __name__ == "__main__":
    pdf_folder = "../Document"
    
    # Step 1: Extract Text from PDFs
    print("Extracting text from PDFs in parallel...")
    documents = extract_text_from_pdfs_parallel(pdf_folder)

    print("Splitting text into chunks...")
    chunks = chunk_text(documents)

    print("Creating Chroma vector database...")
    vector_db = create_vector_db(chunks)

    print("Vector database created and persisted.")
