from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv() 
groq_api_key = os.getenv("GROQ_API_KEY")

yt_link= st.text_input("Enter the youtube link")

if st.button("Generate Summary", key="summary"):
    loader = YoutubeLoader.from_youtube_url(
    yt_link, add_video_info=False
    )
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    model = "mixtral-8x7b-32768"
    llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=model
    )
    chain= load_summarize_chain(llm, chain_type="refine")
    response=chain.invoke(docs)
    st.write(response['output_text'])