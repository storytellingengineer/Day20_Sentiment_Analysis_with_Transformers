# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1algXhb2RgqVdWNrBuvrQ5rBZOwO-7jnD
"""

!pip install streamlit

import streamlit as st
from transformers import pipeline

# Set Streamlit page config
st.set_page_config(page_title="Sentiment Analysis with Transformers", page_icon="🤗")

st.title("🤗 Sentiment Analysis with Transformers")

# Load sentiment analysis pipeline
@st.cache_resource
def load_pipeline():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_pipeline()

# User input
user_text = st.text_area("Enter text to analyze sentiment:", "")

if st.button("Analyze"):
    if user_text.strip() != "":
        with st.spinner("Analyzing..."):
            result = sentiment_pipeline(user_text)[0]
            st.subheader("Result")
            st.write(f"**Sentiment:** {result['label']}")
            st.write(f"**Confidence:** {round(result['score'], 4)}")
    else:
        st.warning("Please enter some text.")

