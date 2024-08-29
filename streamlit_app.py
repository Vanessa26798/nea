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
    
st.info('Uses ...', icon="ℹ️") 
def page2():
 st.title("Second page")
 pg = st.navigation([
    st.Page("page1.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
 ])
pg.run()

