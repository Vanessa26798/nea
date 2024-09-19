import streamlit as st
import random
import pandas as pd
import numpy as np

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

st.header("Caesar cipher")


tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Level of security"])

with tab1:
    st.header("History")

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

    Correct_Encrypt_Key = False                
    if Correct_Plaintext_Length == True and Plaintext != "":
        Encrypt_Choice = st.text_input("Input your own key for encryption (1) or generate a random key (2)? ", value="")
        if Encrypt_Choice == "1":
            Encrypt_Key = st.text_input("Please enter the key for encryption, within 1-25: ", value="")
            if Encrypt_Key.isdigit() == True:
                Encrypt_Key = int(Encrypt_Key)
                if Encrypt_Key < 1 or Encrypt_Key > 25: 
                    st.error('Invalid input.', icon="🚨")
                    Correct_Encrypt_Key = False
                elif Encrypt_Key >= 1 and Encrypt_Key <= 25: 
                    st.write("The key is ", Encrypt_Key)
                    Correct_Encrypt_Key = True
            elif Encrypt_Key.isdigit() == False and Encrypt_Key != "": 
                st.error('Invalid input.', icon="🚨")
                Correct_Encrypt_Key = False
        elif Encrypt_Choice == "2": 
            Encrypt_Key = random.randrange(1, 26)
            Encrypt_Key = int(Encrypt_Key)
            st.write("The key is ", Encrypt_Key)
            Correct_Encrypt_Key = True
        elif Encrypt_Choice != 1 and Encrypt_Choice != 2 and Encrypt_Choice != "": 
            st.error('Invalid input.', icon="🚨")
            Correct_Encrypt_Key = False

    if Correct_Plaintext_Range == True and Correct_Encrypt_Key == True and Correct_Plaintext_Length == True:
       Ciphertext = ["The ciphertext is "]
       for x in Plaintext:
         if x == " ":
             Ciphertext.append(x)
         else: 
             Letter_index = int(Alphabet.index(x))
             Letter_index += Encrypt_Key
             while Letter_index >= 25: 
                 Letter_index -= 26
             Letter = Alphabet[Letter_index]
             Ciphertext.append(Letter)
       st.write("".join(Ciphertext))


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

    Correct_Decrypt_Key = False
    if Correct_Ciphertext_Length == True and Ciphertext != "":
        Decrypt_Choice = st.text_input("Input your own key for decryption (1) or generate a random key (2)? ", value="")
        if Decrypt_Choice == "1":
            Decrypt_Key = st.text_input("Please enter the key for decryption, within 1-25: ", value="")
            if Decrypt_Key.isdigit() == True:
                Decrypt_Key = int(Decrypt_Key)  
                if Decrypt_Key < 1 or Decrypt_Key > 25: 
                    st.error('Invalid input.', icon="🚨")
                    Correct_Decrypt_Key = False
                elif Decrypt_Key >= 1 and Decrypt_Key <= 25: 
                    st.write("The key is ", Decrypt_Key)
                    Correct_Decrypt_Key = True
            elif Decrypt_Key.isdigit() == False and Decrypt_Key != "": 
                st.error('Invalid input.', icon="🚨")
                Correct_Decrypt_Key = False
        elif Decrypt_Choice == "2": 
            Decrypt_Key = random.randrange(1, 26)
            Decrypt_Key = int(Decrypt_Key)            
            st.write("The key is ", Decrypt_Key)
            Correct_Decrypt_Key = True
        elif Decrypt_Choice != 1 and Decrypt_Choice != 2 and Decrypt_Choice != "": 
            st.error('Invalid input.', icon="🚨")
            Correct_Decrypt_Key = False

    if Correct_Ciphertext_Range == True and Correct_Decrypt_Key == True and Correct_Ciphertext_Length == True:
       Plaintext = ["The plaintext is "]
       for x in Ciphertext:
         if x == " ":
             Plaintext.append(x)
         else: 
             Letter_index = int(Alphabet.index(x))
             Letter_index -= Decrypt_Key
             while Letter_index >= 25: 
                 Letter_index -= 26
             Letter = Alphabet[Letter_index]
             Plaintext.append(Letter)
       st.write("".join(Plaintext))



with tab4: 
    st.header("Level of security")
    Plaintext = "AABCDE"
    Occurance = []
    # my_table = pd.DataFrame(np.randn(10, 5))
    # st.table(my_table)
    # df2 = pd.DataFrame(np.random.randn(10, 5))
    # my_table.add_rows(df2)
    for x in Plaintext:
      Total_occurance = len(Plaintext)
      Count = Plaintext.count(x)
      Character_occurance = round(Count/ Total_occurance * 100)
      if x not in Occurance:
          Occurance.append(x)
          Occurance.append(Character_occurance)
    st.write(Occurance)


    # chart_data = pd.DataFrame({"Letter": col0, "Occurance": col1})
    # #   Occurance.append(Character_occurance)
    # # st.write(Occurance)


    # st.bar_chart(chart_data, x = "Letter", y = "Occurance", horizontal = True)






