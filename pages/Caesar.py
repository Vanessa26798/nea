import streamlit as st
import random

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

st.header("Caesar cipher")


tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Weakness"])

with tab1:
    st.header("History")

with tab2:
    st.header("Encryt a plaintext")

    Correct_Plaintext = False
    Plaintext = st.text_input("Please enter the plaintext in upper case, between 10-30 characters: ", value="")    
    for x in Plaintext: 
        if (x in Alphabet or x == " ") and Plaintext[0] != " ":
            Plaintext_in_Alphabet = True
        else:
            Plaintext_in_Alphabet = False
        
        if Plaintext_in_Alphabet == False and Plaintext != "":
            st.error('Invalid plaintext.', icon="🚨")
            Correct_Plaintext = False
            break
        elif Plaintext_in_Alphabet == True or Plaintext == " ":
            Correct_Plaintext = True

    Correct_Length = False
    if Correct_Plaintext == True:
        if (len(Plaintext) < 10 or len(Plaintext) > 30) and Plaintext != "": 
            st.error('Plaintext out of range.', icon="🚨")
            Correct_Length = False
        elif len(Plaintext) > 10 and len(Plaintext) < 30 and len(Plaintext) != 0 and Plaintext != "":
            Correct_Length = True

    Correct_Key = False
    Choice = st.text_input("Input your own key (1) or a random key (2)? ", value="")
    if Choice == "1":
        Key = st.text_input("Please enter the key: ", value="")
        if Key.isdigit() == True:
            st.write("The key is ", Key)
            Key = int(Key)
            Correct_Key = True
        elif Key.isdigit() == False and Key != "": 
            st.error('Invalid input.', icon="🚨")
            Correct_Key = True
    elif Choice == "2": 
        Key = random.randrange(1, 26)
        st.write("The key is ", Key)
        Key = int(Key)
        Correct_Key = True
    elif Choice != 1 and Choice != 2 and Choice != "": 
        st.error('Invalid input.', icon="🚨")
        Correct_Key = False

    if Correct_Plaintext == True and Correct_Key == True and Correct_Length == True:
       Ciphertext = ["The ciphertext is "]

       for x in Plaintext:
         if x == " ":
             Ciphertext.append(Letter)
         else: 
             Letter_index = int(Alphabet.index(x))
             Letter_index += 1
             Letter_index += Key
             if Letter_index >= 26: 
                 Letter_index = Letter_index - 26
             Letter = Alphabet[Letter_index]
             Ciphertext.append(Letter)
         st.write(*Ciphertext)
       # st.write("".join(Ciphertext))


with tab3:
    st.header("Decrypt a ciphertext")






with tab4: 
    st.header("Weakness")


    # Occurence = {}
    # for x in Plaintext:
    #   Total_occurence = len(Plaintext)
    #   Count = Plaintext.count(x)
    #   Character_occurence = round(Count/ Total_occurence * 100)
    #   Occurence[x] = Character_occurence, '%'
    # st.write(Occurence)




