import streamlit as st
import random



st.header("Caesar Encryption")


tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Weakness"])

with tab1:
    st.header("History")

with tab2:
    st.header("Encryt a plaintext")
    
    Plaintext = st.text_input("Please enter the plaintext in upper case: ", value="")
    if Plaintext.isupper() == False and Plaintext != "": 
      st.error('Invalid plaintext.', icon="🚨")
    
    Choice = st.text_input("Input your own key (1) or a random key (2)? ", value="")
    if Choice == "1":
        Key = st.text_input("Please enter the key: ", value="")
        if Key.isdigit() == True:
            st.write("The key is ", Key)
        else: 
            st.error('Invalid input.', icon="🚨")
    elif Choice == "2": 
        Key = random.randrange(1, 26)
        st.write("The key is ", Key)
    elif Choice != 1 and Choice != 2 and Choice != "": 
        st.error('Invalid input.', icon="🚨")
    if Plaintext.isupper() == True:
       Ciphertext = []
       Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
       for x in Plaintext:
         if x == " ":
             Ciphertext.append(Letter)
         else: 
             Key = int(Key)
             Letter_index = int(Alphabet.index(x))
             Letter_index += Key
             if Letter_index >= 26: 
                 Letter_index -= 26
                 Letter = Alphabet[Letter_index]
             Ciphertext.append(Letter) 
       st.write("The ciphertext is ", *Ciphertext)


    # Occurence = {}
    # for x in Plaintext:
    #   Total_occurence = len(Plaintext)
    #   Count = Plaintext.count(x)
    #   Character_occurence = round(Count/ Total_occurence * 100)
    #   Occurence[x] = Character_occurence, '%'
    # st.write(Occurence)





with tab3:
    st.header("Decrypt a ciphertext")

with tab4: 
    st.header("Weakness")


