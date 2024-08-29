import streamlit as st
import random

st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")


# tab1, tab2 = st.tabs(["Caesar Encryption", "Vernam Encryption"])

# with tab1:
#     st.header("Caesar Encryption")
#     Input = st.text_input("Input your own key (1) or a random key (2)? ", " ")
#     if Input == "1":
#         Key = st.text_input("Please enter the key: ", "")
#         st.write("The key is ", Key)
#     elif Input == "2": 
#         Key = random.randrange(1, 26)
#         st.write("The key is ", Key)
#     elif Input != 1 and Input != 2: 
#         st.write("Invalid input.")

# with tab2:
#     st.header("Vernam Encryption")
#     st.write("tesing")
     

st.button("Caesar cipher")
st.info('Uses ...', icon="ℹ️")
# if st.button("Caesar cipher"):
#     print("C")
    


# st.button("Vernam Cipher")
# st.info('Uses ...', icon="ℹ️")
# if st.button("Vernam Cipher"):
#     print("V")


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



