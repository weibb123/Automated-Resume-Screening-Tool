import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.embeddings.openai import OpenAIEmbeddings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sidebar import *
from util import *

# page setup
st.set_page_config(page_title="Automated Resume Screening Tool")

# header
st.title("😊Automated Resume Screening Tool")

sbar()
# receive inputs from user
job_post = st.text_area("Paste the whole job description here")

def process_resume(resume_pdf, job_text):
    """function to generate response
    """
    try:
        API_KEY = st.session_state['OPENAI_API_KEY']
    except Exception as e:
        st.error("no api key")


    text = get_pdf(resume_pdf)
    st.write("Got PDF")

    text_chunks = get_chunks(text)
    st.write("get chunk")

    # create vectorstore embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
    vectorstore = Chroma.from_texts(texts=text_chunks, embedding=embeddings)

    # create retriever
    retriever = vectorstore.as_retriever()

    template = """You are a trustworthy assistant for question-answering tasks.
        use the following pieces of retrieved context to answer the question.
        Question: {question}
        context: {context}
        Answer:
    """

    prompt = PromptTemplate.from_template(template)
    llm = ChatOpenAI(openai_api_key=API_KEY, temperature=0.01, model="gpt-4-1106-preview")

    rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
    query = f"""Using {job_text}, identify key skills, experience levels, job role suitability, what candidate good at and lack experience on.
            Make sure to mention company's name
            Identify if candidate will be likely to get interview or not.
            Keep it at most 3 sentences.
            """
   
    response = rag_chain.invoke(query)
        
    return response


uploaded_file = st.file_uploader("Upload your resume in pdf", accept_multiple_files=True)

if st.button("Get info") and uploaded_file:
    with st.spinner("Working hard.."):
       response = process_resume(uploaded_file, job_post)
       st.write(response)
       
       #cosine similarity
       vectorizer = TfidfVectorizer()
       tfidf_matrix = vectorizer.fit_transform([response, job_post])
       cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
       st.write(f"Similarity: {cosine_sim[0][0]:.2f}")

