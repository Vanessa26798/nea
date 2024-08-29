import streamlit as st
import random

st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")


Input = st.text_input("Input your own key (1) or a random key (2)? ", "")
if Input == "1":
  Key = st.text_input("Please enter the key: ", "")
elif Input == "2":  
  Key = random.randrange(1, 26)
  st.write("The key is ", Key)
while Key != 1 and Key != 2: 
  Input = st.text_input("Invalid choice."")


# Key = input("Input your own key (1) or a random key (2)? ")
# if Key == "1":
#   Key = input("Please enter the key: ")
#   while Key.isdigit() == False:
#    print("Invalid key")
#    Key = input("Please enter the key: ")
# elif Key == "2": 
#   Key = random.randrange(1, 26)
#   print(Key)
# while Key != 1 and Key != 2: 
#   Key = input("input your own key (1) or a random key (2)")
