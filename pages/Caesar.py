import streamlit as st
import random


st.header("Caesar Encryption")


tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Weakness"])

with tab1:
    st.header("History")

with tab2:
    st.header("Encryt a plaintext")
    
    Plaintext = st.text_input("Please enter the plaintext in upper case: ", value="")
    if Plaintext.isupper() == False:
      st.write("Invalid plaintext")
    
    Input = st.text_input("Input your own key (1) or a random key (2)? ", value="")
    if Input == "1":
        Key = st.text_input("Please enter the key: ", value="")
        st.write("The key is ", Key)
    elif Input == "2": 
        Key = random.randrange(1, 26)
        st.write("The key is ", Key)
    elif Input != 1 and Input != 2: 
        st.write("Invalid input.")
    if Plaintext.isupper() == True and Key.isdigit() == True:
       Key = int(Key)
       Ciphertext = []
       for x in Plaintext:
         Letter = int(Alphabet.index(x))
         Letter += Key
         if Letter >= 26: 
           Letter -= 26
           Letter = Alphabet[Letter]
           Ciphertext.append(Letter) 
           st.write("The ciphertext is ", *Ciphertext)
    Occurence = {}
    for x in Plaintext:
      Total_occurence = len(Plaintext)
      Count = Plaintext.count(x)
      Character_occurence = round(Count/ Total_occurence * 100)
      Occurence[x] = Character_occurence, '%'
    st.write(Occurence)





with tab3:
    st.header("Decrypt a ciphertext")

with tab4: 
    st.header("Weakness")


