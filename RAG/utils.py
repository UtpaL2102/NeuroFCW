import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from concurrent.futures import ProcessPoolExecutor
import pdfplumber
import os
from tqdm import tqdm
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader

def get_embedding_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    model_name="sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': device}
    encode_kwargs = {'normalize_embeddings': False}

    embedding_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embedding_model

def get_vector_store(persist_dir="./chroma_db"):
    embedding_model=get_embedding_model()
    
    vector_store = Chroma(
        collection_name="Compliance",
        embedding_function=embedding_model,
        persist_directory=persist_dir,
    )

    return vector_store

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "".join([page.extract_text() for page in pdf.pages])
    return {"text": text, "source": os.path.basename(file_path)}

def extract_text_from_pdfs_parallel(folder_path):
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".pdf")]
    with ProcessPoolExecutor() as executor:
        documents = list(tqdm(executor.map(extract_text_from_pdf, pdf_files), total=len(pdf_files)))
    return documents