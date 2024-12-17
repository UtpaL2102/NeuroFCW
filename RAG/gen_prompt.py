from utils import get_vector_store
from langchain.prompts import PromptTemplate

def query_vector_store(query, vector_store, top_k=2):
    results = vector_store.similarity_search(query, k=top_k)
    for i, result in enumerate(results):
        with open(f"Result-{i+1}.txt",'w',encoding="utf-8") as f:
            content=f"Content: {result}"+"\n"+f"Metadata: {result.metadata}\n"
            f.write(content)

prompt_template = """
Using the following context, answer the query or generate the required output:

Context:
{context}

Query:
{query}
"""

def generate_augmented_query(input_variables):
    prompt = PromptTemplate(input_variables=["context", "query"], template=prompt_template)
    return prompt.format(**input_variables)

if __name__ == "__main__":
    persist_dir="./chroma_db"
    vector_store = get_vector_store(persist_dir=persist_dir)
    query = "Tell me the software development process according to MISRA compliance"
    retriever = vector_store.as_retriever()
    docs = retriever.invoke(query)
    len(docs)
    print(docs)