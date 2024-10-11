# Youtube-Video-Summarizer


## Overview
- An application to summarize YouTube videos and Webpages through URLs using streamlit web application

## Project Structure
- [app.py](https://github.com/Pratik872/Youtube-Video-Summarizer/blob/main/app.py) : Streamlit application for summarizing videos/webpages.

- [requirements.txt](https://github.com/Pratik872/Youtube-Video-Summarizer/blob/main/requirements.txt) : Packages required for the application

## Problem Objective
- To build a web application to summarize the videos / webpages using a Large Language model.

## Methodology

![MultiModal RAG Flow](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/Multimodal_RAG_Flow.png)

The RAG Framework involves:
- Preprocessing videos/images for passing into framework

- Computing the joint embeddings of images/videos and captions and ingesting them into vector store

- Passing a query from user to the framework and augmenting the query using the video transcripts

- Using a Large Vision-Language Model to get inference and chat completion

### 1 - Computing Embeddings

Here are sample pictures and computation of BridgeTower embeddings

![Sample images](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/sample_images_embeds.png)

The embeddings have 512 dimensions and so I have used UMAP to project into 2 dimensions to visualize it

![UMAP](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/embeds_UMAP.png)

- The embeddings of image-text pairs of `cats` (i.e., blue dots) are
closed to each other.
- The embeddings of image-text pairs of `cars` (i.e., orange dots) are
closed to each other.
- The embeddings of image-text pairs of `cats` (blue dots) are far away
from the embeddings of image-text pairs of `cars` (orange dots).


### 2 - Preprocessing Videos

- Videos were downloaded from Youtube along with the transcripts. For the videos which didn't have transcripts were generated using 'Whisper' model.

- For videos without language, LVLM model was used to generate captions which were then passed as an query.

- For each video segment, we will extract:
    1. A frame right at the middle of the time frame of the video segment;
    2. Its metadata including:
        -extracted_frame_path: Path to the saved extracted-frame;
        -transcript: Transcript of the extracted frame;
        -video_segment_id: The order of video segment from which the frame was extracted;
        -video_path: Path to the video from which the frame was extracted; This helps to retrieve the correct video when there are many ones in your video corpus;
        -mid_time_ms: Time stamp (in ms) of the extracted frame

- Here is the sample generated caption for an image
 ![video_preprocess](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/video_preprocess.png)


### 3 - Vector Store - Ingesting and Retrieval
![vector_store](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/vector_stores.png)

- LanceDB (as retreiever) and Langchain was used to store the embeddings for the metadata.

- Top 'k' results were retrieved. Below are the sample quesry and results for top 3.
        Query - "a toddler and an adult"

        ![1](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/1.png)
        ![2](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/2.png)
        ![3](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/3.png)


### 4 - Large Vision-Language model for completion

![LLMvsLVLM](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/LLM%20vs%20LVLM.png)

#### LLaVA (Large Language-and-Vision Assistant) model
![LLaVA](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/LLaVA.png)
- LLaVA , an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding.

- LLaVA doesn't just see images but understands them, reads the text embedded in them, and reasons about their context—all while conversing with you in a way that feels almost natural.


### 5 - Working of Application

- ![sample1](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/working1.png)
- ![sample2](https://github.com/Pratik872/RAG/blob/main/Multimodal%20RAG/images/working2.png)


### Built with 🛠️
- Packages/Repo : Langchain, Jupyter, LanceDB, Gradio

- Coded on : Jupter Notebook (modelling), VSCode(building application)

