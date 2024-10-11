# Youtube-Video-Summarizer


## Overview
- An application to summarize YouTube videos and Webpages through URLs using streamlit web application

## Project Structure
- [app.py](https://github.com/Pratik872/Youtube-Video-Summarizer/blob/main/app.py) : Streamlit application for summarizing videos/webpages.

- [requirements.txt](https://github.com/Pratik872/Youtube-Video-Summarizer/blob/main/requirements.txt) : Packages required for the application

## Problem Objective
- To build a web application to summarize the videos / webpages using a Large Language model.

## Methodology

![App Demo](https://github.com/Pratik872/Youtube-Video-Summarizer/blob/main/readme%20resources/app%20demo.png)

The Web Application involves:
- Initializing the web application

- Invoking a Large Language model

- Creating a prompt for LLM 

- Passing the URL to Langchain/external tools to get the transcripts. Conversion of those transcripts into data and passing it to LLM

### 1 - Initializing the Web Application
- Created using Streamlit

- Integrated the application with Groq API

### 2 - Invoking a Large Language model
- Used `Gemma-7b-It` model through Groq. Other free models can also be used

- Prompts would be passed to this model using Groq API

### 3 - Creating a prompt for LLM
- Created a prompt template using `Langchain`

- Defined the prompt to LLM using prompt template

### 4 - Getting transcripts for the video/website using external tools and `Langchain`
- Fetching the URL uploaded by user through streamlit

- Used this URL to get transcripts through `YoutubeLoader` and `UnstructuredURLLoader` in `Langchain` and converting those to data which needs to be passed to the LLM


### Sample Working

![Demo](https://github.com/Pratik872/Youtube-Video-Summarizer/blob/main/readme%20resources/app%20sample.png)


### Built with 🛠️
- Packages/Repo : Langchain, Jupyter, Streamlit, Groq

- Coded on : Jupter Notebook (modelling), VSCode(building application)

