import streamlit as st
from langdetect import detect
from deep_translator import GoogleTranslator
from langchain_community.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="Wikipedia Search")
st.title("Welcome to Wikipedia Search")

query = st.text_input("Enter a query:")

@st.cache_data
def fetch_wikipedia(query, max_docs=3):  
    try:
        loader = WikipediaLoader(query, load_max_docs=max_docs)
        docs = loader.load()
        combined_content = " ".join([doc.page_content for doc in docs])  
        return combined_content
    except Exception as e:
        return f"An error occurred: {e}"

def split_text(text, chunk_size=2000, chunk_overlap=300):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)

if query:
    try:
        
        language = detect(query)
        query_en = GoogleTranslator(source="auto", target="en").translate(query)
    except Exception as e:
        st.error(f"Translation failed: {e}")
        query_en = query

    
    content = fetch_wikipedia(query=query_en, max_docs=3)

    if "An error occurred" in content:
        st.error(content)
    elif content:
        try:
            content_chunks = split_text(content, chunk_size=2000, chunk_overlap=300)
            
            translated_chunks = [
                GoogleTranslator(source="en", target=language).translate(chunk)
                for chunk in content_chunks
            ]
            translated_content = " ".join(translated_chunks)
            st.write(translated_content)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("No content found for the given query.")
else:
    st.info("Please enter a query to search.")

