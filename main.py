import streamlit as st
from sentence_transformers import SentenceTransformer
import plotly.graph_objects as go
import numpy as np

@st.cache_resource
def load_model():
    return SentenceTransformer('sentence-transformers/sentence-t5-base')

model = load_model()

def cosine_similarity(embedding1, embedding2):
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    return dot_product / (norm1 * norm2)

def sharpened_cosine_similarity(embedding1, embedding2, exponent=3):
    # Compute standard cosine similarity
    cos_sim = cosine_similarity(embedding1, embedding2)
    # Apply sharpening
    sharpened_sim = cos_sim ** exponent
    return sharpened_sim

st.title('Compare Text Semantics')
st.info("This app compares two texts and provides a semantic similarity score based on their main content.")

# Create two columns for text input fields
col1, col2 = st.columns(2)

with col1:
    text1 = st.text_area("Enter Text 1:", height=300)

with col2:
    text2 = st.text_area("Enter Text 2:", height=300)

# Button to trigger comparison
if st.button("Compare Texts"):
    if text1 and text2:
        with st.spinner('Computing similarity...'):
            embedding1 = model.encode(text1)
            embedding2 = model.encode(text2)
            sharpened_sim = sharpened_cosine_similarity(embedding1, embedding2, exponent=3)

            # Create the gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=sharpened_sim,
                title={"text": "Sharpened Cosine Similarity"},
                gauge={
                    "axis": {"range": [0, 1]},
                    "bar": {"color": "blue"},
                    "bgcolor": "lightgray",
                    "steps": [
                        {"range": [0, 0.5], "color": "lightgray"},
                        {"range": [0.5, 1], "color": "lightblue"},
                    ],
                },
            ))

            st.write("This gauge chart displays the cosine similarity score.")
            st.plotly_chart(fig)
    else:
        st.warning("Please enter both texts to compare.")
