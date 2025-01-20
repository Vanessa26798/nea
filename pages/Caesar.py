import streamlit as st
import random
import pandas as pd

import string
Alphabet = string.ascii_uppercase

st.header("Caesar cipher")

tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Level of security"])

with tab1:
    st.header("History")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn.britannica.com/17/193717-050-030D75E3/Julius-Caesar-statue-Rome-Italy.jpg?w=300", caption="Bronze sculpture of Julius Caesar in Rome")
    with col2:
        st.write("Caesar Cipher, also known as substitution cipher, is one of the oldest cryptographic algorithms. It is named after Julius Caesar who initially used it to protect sensitive and secret military messages, allowing him to communicate with his army generals in the war front.  ")


with tab2:
    st.header("Encrypt a plaintext")

def my_function():
  print("Hello from a function")

my_function()
    
    Plaintext_in_Alphabet = False
    Correct_Plaintext_Range = False
    Correct_Plaintext_Length = False
    Correct_Encrypt_Key = False 

    Input_Plaintext()
    Check_Plaintext_in_Alphabet()
    Check_Plaintext_Range()
    Check_Plaintext_Length()

    def Input_Plaintext():
        Plaintext = st.text_input("Please enter the plaintext in upper case, within 10-30 characters: ", value="")
        Plaintext = Plaintext.upper()
        return Plaintext

    def Check_Plaintext_in_Alphabet():
        for x in Plaintext: 
            if (x in Alphabet or x == " ") and Plaintext[0] != " ":
                Plaintext_in_Alphabet = True
            else:
                Plaintext_in_Alphabet = False
            return Plaintext_in_Alphabet

    def Check_Plaintext_Range():
        if Plaintext_in_Alphabet == False and Plaintext != "":
            st.error('Invalid plaintext.', icon="🚨")
            Correct_Plaintext_Range = False
            break
        elif Plaintext_in_Alphabet == True or Plaintext == " ":
            Correct_Plaintext_Range = True
        return Correct_Plaintext_Range
            
    def Check_Plaintext_Length():
        if Correct_Plaintext_Range == True:
            if (len(Plaintext) < 10 or len(Plaintext) > 30) and Plaintext != "": 
                st.error('Plaintext out of range.', icon="🚨")
                Correct_Plaintext_Length = False
            elif len(Plaintext) >= 10 and len(Plaintext) <= 30 and len(Plaintext) != 0 and Plaintext != "":
                Correct_Plaintext_Length = True
            return Correct_Plaintext_Length

    def Check_Encrypt_Choice():
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
        elif Encrypt_Choice != "1" and Encrypt_Choice != "2" and Encrypt_Choice != "": 
            st.error('Invalid input.', icon="🚨")
            Correct_Encrypt_Key = False

    if Correct_Encrypt_Key == True:    
        st.write("The alphabet list is shifted to the right by ", Encrypt_Key)
        Alphabet_List = ' '.join(Alphabet)
        Alphabet_List = Alphabet_List.split(" ")
        Original_Alphabet = pd.DataFrame(columns = Alphabet_List)
        st.write("Original alphabet list:")
        Original_table = st.table(Original_Alphabet)
        Encrypted_Alphabet_List_PartOne = Alphabet[Encrypt_Key:26]
        Encrypted_Alphabet_List_PartTwo = Alphabet[0:Encrypt_Key]
        Encrypted_Alphabet_List = Encrypted_Alphabet_List_PartOne + Encrypted_Alphabet_List_PartTwo
        Encrypted_Alphabet_List = ' '.join(Encrypted_Alphabet_List)
        Encrypted_Alphabet_List = Encrypted_Alphabet_List.split(" ")
        Encrypted_Alphabet = pd.DataFrame(columns = Encrypted_Alphabet_List)
        st.write("Encrypted alphabet list:")
        Encrypted_table = st.table(Encrypted_Alphabet)

    if Correct_Plaintext_Range == True and Correct_Encrypt_Key == True and Correct_Plaintext_Length == True:
       Ciphertext = ["Therefore, the ciphertext is "]
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
        elif Decrypt_Choice != "1" and Decrypt_Choice != "2" and Decrypt_Choice != "": 
            st.error('Invalid input.', icon="🚨")
            Correct_Decrypt_Key = False

    if Correct_Decrypt_Key == True:    
        st.write("The alphabet list is shifted to the left by ", Decrypt_Key)
        Alphabet_List = ' '.join(Alphabet)
        Alphabet_List = Alphabet_List.split(" ")
        Original_Alphabet = pd.DataFrame(columns = Alphabet_List)
        st.write("Original alphabet list:")
        Original_table = st.table(Original_Alphabet)
        Decrypted_Alphabet_List_PartOne = Alphabet[(26-Decrypt_Key):26]
        Decrypted_Alphabet_List_PartTwo = Alphabet[0:(26-Decrypt_Key)]
        Decrypted_Alphabet_List = Decrypted_Alphabet_List_PartOne + Decrypted_Alphabet_List_PartTwo
        Decrypted_Alphabet_List = ' '.join(Decrypted_Alphabet_List)
        Decrypted_Alphabet_List = Decrypted_Alphabet_List.split(" ")
        Decrypted_Alphabet = pd.DataFrame(columns = Decrypted_Alphabet_List)
        st.write("Decryted alphabet list:")
        Decrypted_table = st.table(Decrypted_Alphabet)

    if Correct_Ciphertext_Range == True and Correct_Decrypt_Key == True and Correct_Ciphertext_Length == True:
       Plaintext = ["Therefore, the plaintext is "]
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

    Plaintext = "CAESAR"
    Key = 12
    Ciphertext = []
    for x in Plaintext:
        Letter_index = int(Alphabet.index(x))
        Letter_index += Key
        while Letter_index >= 25: 
            Letter_index -= 26
        Letter = Alphabet[Letter_index]
        Ciphertext.append(Letter)
    st.write("If the plaintext is ", Plaintext, ", the key is ", Key, ", the ciphertext is ", "".join(Ciphertext), ":")
    st.write(" ")
    Character = []
    Occurrence = []
    for x in Plaintext:
      if x != " ":
          Total_occurrence = len(Plaintext)
          Count = Plaintext.count(x)
          Character_occurrence = round(Count / Total_occurrence * 100)
          if x not in Character:
              Character.append(x)
              Occurrence.append(Character_occurrence)
              if Character.index(x) > 0:
                  Last_Character_Index = Character.index(x) - 1
                  if int(Occurrence[Last_Character_Index]) > int(Occurrence[Character.index(x)]):
                      Highest_Occurrence_Character = Character[Last_Character_Index]
                      Highest_Occurrence = Occurrence[Last_Character_Index]
                  elif int(Occurrence[Last_Character_Index]) < int(Occurrence[Character.index(x)]):
                      Highest_Occurrence_Character = [x]
                      Highest_Occurrence = [x]

    chart_data = pd.DataFrame({"Character": Character, "Occurrence": Occurrence})
    st.bar_chart(chart_data, x = "Character", y = "Occurrence", horizontal=True)
    st.write("The character with the highest occurrence is " + Highest_Occurrence_Character + ".")
    st.write("This graph shows how easy it is to guess the key as the length of plaintext increases, the more obvious it is to identify the common patterns. Furthermore, there are only 25 possible keys so they can all be easily tested.")
    st.write("Therefore, level of security for Caesar cipher is lower.")



