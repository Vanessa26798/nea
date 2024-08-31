import streamlit as st
import random

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

st.header("Vernam cipher")


tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Strengths"])

with tab1:
    st.header("History")

with tab2:
    st.header("Encryt a plaintext")
    
    Plaintext = st.text_input("Please enter the plaintext in upper case, between 10-30 characters: ", value="")
    if Plaintext.isupper() == False and Plaintext != " ": 
      st.error('Invalid plaintext.', icon="🚨")
    else:
        Key = random.sample()
        st.write("The key is ", )


# key < length? 



#    for x in Plaintext:
#      Plaintext_ASCII = []
#      LetterASCII = ord(x)
#      while LetterASCII >= 1:
#       LetterBinary = LetterASCII % 2
#       Plaintext_ASCII.append(LetterBinary)
#       LetterASCII = LetterASCII // 2

#      Key_ASCII = []
#      Key = random.choice(Alphabet)
#      KeyASCII = ord(Key)
#      while KeyASCII >= 1:
#       KeyBinary = KeyASCII % 2
#       Key_ASCII.append(KeyBinary)
#       KeyASCII = KeyASCII // 2     

#      print(Plaintext_ASCII)
#      print(Key_ASCII)

#      Ciphtertext_ASCII = []
#      for x in Plaintext_ASCII:
#        CiphertextASCII = Plaintext_ASCII[x] ^ Key_ASCII[x]
#        Ciphtertext_ASCII.append(CiphertextASCII)
#        print(Ciphtertext_ASCII)       







with tab3:
    st.header("Decrypt a ciphertext")

with tab4: 
    st.header("Strengths")
