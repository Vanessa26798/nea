

import streamlit as st
import random

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

st.header("Vernam cipher")


tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Level of security"])

with tab1:
    st.header("History")
    col1, col2 = st.columns(2)

with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeIbofN8VxLSPyQPAXN5tGi4wE_xP2AQOPDyFZ05zAGSQfMsZupIP7IdQEMhP4diqqTxQ&usqp=CAU", caption="Gilbert S. Vernam")


with col2:
    st.write("Vernam cipher, also known as one-time pad, is invented by Gilbert S. Vernam when he was working for the American Telephone & Telegraph Company (AT&T) as an engineer in 1917. ")


with tab2:
    st.header("Encryt a plaintext")

    Correct_Plaintext_Range = False
    Plaintext = st.text_input("Please enter the plaintext in upper case, within 10-30 characters: ", value="")
    Plaintext = Plaintext.upper()
    for x in Plaintext: 
        if (x in Alphabet or x == " ") and Plaintext[0] != " ":
            Plaintext_in_Alphabet = True
        else:
            Plaintext_in_Alphabet = False
        
        if Plaintext_in_Alphabet == False and Plaintext != "":
            st.error('Invalid plaintext.', icon="🚨")
            Correct_Plaintext_Range = False
            break
        elif Plaintext_in_Alphabet == True or Plaintext == " ":
            Correct_Plaintext_Range = True

    Correct_Plaintext_Length = False
    if Correct_Plaintext_Range == True:
        if (len(Plaintext) < 10 or len(Plaintext) > 30) and Plaintext != "": 
            st.error('Plaintext out of range.', icon="🚨")
            Correct_Plaintext_Length = False
        elif len(Plaintext) >= 10 and len(Plaintext) <= 30 and len(Plaintext) != 0 and Plaintext != "":
            Correct_Plaintext_Length = True



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





# hashtable?

with tab3:
    st.header("Decrypt a ciphertext")

    Correct_Ciphertext_Range = False
    Ciphertext = st.text_input("Please enter the ciphertext in upper case, within 10-30 characters: ", value="")    
    Ciphertext = Ciphertext.upper()
    for x in Ciphertext: 
        if (x in Alphabet or x == " ") and Ciphertext[0] != " ":
            Ciphertext_in_Alphabet = True
        else:
            Ciphertext_in_Alphabet = False
        
        if Ciphertext_in_Alphabet == False and Ciphertext != "":
            st.error('Invalid ciphertext.', icon="🚨")
            Correct_Ciphertext_Range = False
            break
        elif Ciphertext_in_Alphabet == True or Ciphertext == " ":
            Correct_Ciphertext_Range = True

    Correct_Ciphertext_Length = False
    if Correct_Ciphertext_Range == True:
        if (len(Ciphertext) < 10 or len(Ciphertext) > 30) and Ciphertext != "": 
            st.error('Ciphertext out of range.', icon="🚨")
            Correct_Ciphertext_Length = False
        elif len(Ciphertext) >= 10 and len(Ciphertext) <= 30 and len(Ciphertext) != 0 and Ciphertext != "":
            Correct_Ciphertext_Length = True







with tab4: 
    st.header("Level of security")
    st.write("Theoratically, Vernam cipher offers perfect security due to the unique key, making it mathematically impossible to break. ")





