import streamlit as st
from deep_translator import GoogleTranslator
from langchain_community.document_loaders import WikipediaLoader


st.set_page_config(page_title="Wikipedia Search")
st.title("Welcome to Wikioedia Search")

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

if query:
   
    try:
        query_en = GoogleTranslator(source="auto", target="en").translate(query)
    except Exception as e:
        st.error(f"Translation failed: {e}")
        query_en = query
   
    
    content = fetch_wikipedia(query=query_en,max_docs=3)
    
   
    if "An error occurred" in content:
        st.error(content)
    elif content:
        st.write(content)
    else:
        st.warning("No content found for the given query.")
        
else:
    st.info("Please enter a query to search.")
