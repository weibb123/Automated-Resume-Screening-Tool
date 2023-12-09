from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader

def get_pdf(doc):
    """
    function to get the pdf(resume) from user
    """

    text = ""

    for pdf in doc:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_chunks(text):
    text_spliter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len
    )
    chunks = text_spliter.split_text(text)
    return chunks
