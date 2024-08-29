import streamlit as st
import random




st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")
     


col1, col2 = st.columns(2)

with col1:
    st.header("Caesar cipher")
    st.info('Uses ...')
if st.button("Caesar cipher"):
     st.page_link("http://www.google.com")

with col2:
    st.header("Vernam cipher")
    st.info('Uses ...')






# st.info('Uses ...', icon="ℹ️")
# if st.button("Caesar cipher"):
#      st.page_link("pages/page2")


# if st.button("Caesar cipher"):
#     st.write("C")
    


# st.button("Vernam Cipher")
# st.info('Uses ...', icon="ℹ️")
# if st.button("Vernam Cipher"):
#     st.write("V")


# def page2():
#  st.title("Second page")
#  pg = st.navigation([
#     st.Page("page1.py", title="First page", icon="🔥"),
#     st.Page(page2, title="Second page", icon=":material/favorite:"),
#  ])
# pg.run()


# tab1, tab2, tab3, tab4 = st.tabs(["Encrypt a plaintext", "Decrypt a ciphertext", "History", "Weakness"])

# with tab1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
# with tab2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
# with tab3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
# with tab4: 



