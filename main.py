import streamlit as st

st.title('Text Similarity Check')
st.info("This app compares two texts and provides a semantic similarity score based on their main content.")

text1 = st.text_area("Enter Text 1:")
text2 = st.text_area("Enter Text 2:")

if st.botton("Compare Texts"):
  if text1 and text2:
    st.text("done")
  else:
    st.write("Please enter both texts to compare.")
