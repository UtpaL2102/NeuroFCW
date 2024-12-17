import os
import docx2txt
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

def extract_text_from_docx(docx_file):
    text = docx2txt.process(docx_file)
    return {"text": text, "source": os.path.basename(docx_file)}

def extract_text_from_docx_parallel(folder_path):
    docx_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".docx")]
    with ProcessPoolExecutor() as executor:
        documents = list(tqdm(executor.map(extract_text_from_docx, docx_files), total=len(docx_files)))
    return documents
