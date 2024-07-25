import streamlit as st
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/sentence-t5-base')

st.title('Text Similarity Check')
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
        embedding1 = model.encode(text1)
        embedding2 = model.encode(text2)
        st.write(embedding1)
        st.write(embedding2)
    else:
        st.warning ("Please enter both texts to compare.")
