import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
import os
from dotenv import load_dotenv
load_dotenv()


#Streamlit App

st.set_page_config(page_title="Langchain: Summarize Text from TY or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

#Configuring Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")


generic_url = st.text_input("URL",label_visibility="collapsed")

#Gemma Model using Groq API
llm = ChatGroq(model="Gemma-7b-It",groq_api_key=groq_api_key)

#Prompting
##Creating prompt template
prompt_template = """
Provide a summary of the following content in 300 words
Content:{text}


"""
#define prompt
prompt = PromptTemplate(template=prompt_template,input_variables=["text"])


if st.button("Summarize the content from YT or Website"):
    #Validate all inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")

    elif not validators.url(generic_url):
        st.error("Not a valid URL. Please enter a valid YT / Website url")

    else:
        try:
            with st.spinner("Waiting..."):
                #Loading the website data
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],
                                                 ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    
                docs = loader.load()

                ##Chain for Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary = chain.run(docs)


                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception:{e}")


#Sample youtube videos URLS - https://www.youtube.com/watch?v=X8zzxySJvG8&t=43s ; https://www.youtube.com/watch?v=b0Z1YDSB1IE