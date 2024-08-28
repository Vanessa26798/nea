import streamlit as st

st.title("ENCRYPTION TEACHING TOOL")
st.write(
  "Select the encryption method that you would like to discover more about"
)


title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)


st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
