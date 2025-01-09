


import streamlit as st
import random
import pandas as pd
import time
import numpy as np

import string
Alphabet = string.ascii_uppercase

Baudot = {
    Alphabet[0]: '00011', 
    Alphabet[1]: '11001',
    Alphabet[2]: '01110', 
    Alphabet[3]: '01001',
    Alphabet[4]: '00001', 
    Alphabet[5]: '01101',
    Alphabet[6]: '11010', 
    Alphabet[7]: '10100',
    Alphabet[8]: '00110', 
    Alphabet[9]: '01011',
    Alphabet[10]: '01111', 
    Alphabet[11]: '10010',
    Alphabet[12]: '11100', 
    Alphabet[13]: '01100',
    Alphabet[14]: '11000', 
    Alphabet[15]: '10110',
    Alphabet[16]: '10111', 
    Alphabet[17]: '01010',
    Alphabet[18]: '00101', 
    Alphabet[19]: '10000',
    Alphabet[20]: '00111',
    Alphabet[21]: '11110',
    Alphabet[22]: '10011', 
    Alphabet[23]: '11101',
    Alphabet[24]: '10101', 
    Alphabet[25]: '10001'
    }     

def get_key(val):
    for key, value in Baudot.items():
        if val == value:
            return key
    return "Key doesn't exist"


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


    if Correct_Plaintext_Range == True and Correct_Plaintext_Length == True:
        Plaintext_Baudot = []
        for x in Plaintext:
            if x != " ":
                Plaintext_Baudot.append(Baudot[x])
            elif x == " ": 
                Plaintext_Baudot.append(" ")
        Key = []
        Key_Baudot = []
        Key_Index = 0
        Ciphertext = []
        for x in Plaintext_Baudot:
            if x == " ": 
                Key.append(" ") 
                Key_Baudot.append(" ") 
                Key_Index = Key_Index + 1
                Ciphertext.append(" ")    
            elif x != " ":
                Key_Letter = random.choice(Alphabet)
                Key.append(Key_Letter)
                Key_Baudot.append(Baudot[Key_Letter])
                XOR = [x]
                XOR.append(Key_Baudot[Key_Index])
                XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                XOR_Result = str(XOR_Result)
                Ciphertext_Letter = get_key(XOR_Result) 
                while Ciphertext_Letter == "Key doesn't exist":
                    Key_Letter = random.choice(Alphabet)
                    Key[Key_Index] = Key_Letter
                    Key_Baudot[Key_Index] = Baudot[Key_Letter]
                    Key_LetterBaudot = Key_Baudot[Key_Index]
                    XOR = [x]
                    XOR.append(Key_LetterBaudot)
                    XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                    XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                    XOR_Result = str(XOR_Result)
                    Ciphertext_Letter = get_key(XOR_Result)
                    if Ciphertext_Letter != "Key doesn't exist" and " ":
                        Ciphertext.append(Ciphertext_Letter)
                        Key_Index = Key_Index + 1   
                        break
                else:
                    Ciphertext.append(Ciphertext_Letter)
                    Key_Index = Key_Index + 1  


        Plaintext_Baudot_two = []
        for x in Plaintext_Baudot:
            if x == " ": 
                Plaintext_Baudot_two.append(x)
            elif x != " ":
                Plaintext_Baudot_two.append(x)
                Plaintext_Baudot_two.append(" ")
        # Plaintext_Baudot = Plaintext_Baudot.split(" ")
        st.write(Plaintext_Baudot_two)
        st.write("".join(Plaintext_Baudot_two))
        st.write("The key is ", "".join(Key)) 
        
        # Plaintext = ' '.join(Plaintext)
        # Plaintext = Plaintext.split(" ")
        # st.write(Plaintext)
        # Plaintext_table = pd.DataFrame(columns = Plaintext)
        # Table = st.table(Plaintext_table)
            
            # Encrypted_Alphabet_List_PartOne = Alphabet[Encrypt_Key:26]
            # Encrypted_Alphabet_List_PartTwo = Alphabet[0:Encrypt_Key]
            # Encrypted_Alphabet_List = Encrypted_Alphabet_List_PartOne + Encrypted_Alphabet_List_PartTwo
            # Encrypted_Alphabet_List = ' '.join(Encrypted_Alphabet_List)
            # Encrypted_Alphabet_List = Encrypted_Alphabet_List.split(" ")
            # Encrypted_Alphabet = pd.DataFrame(columns = Encrypted_Alphabet_List)
            # st.write("Encryted alphabet list:")
            # Encrypted_table = st.table(Encrypted_Alphabet)


        # baudot of original
        # xor baudot of key
        # = encrypted baudot 
        # encrypted text 
        
        st.write( "The ciphertext is ", "".join(Ciphertext))          
    



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
 
    
    if Correct_Ciphertext_Range == True and Correct_Ciphertext_Length == True:
        Ciphertext_Baudot = []
        for x in Ciphertext:
            if x != " ":
                Ciphertext_Baudot.append(Baudot[x])
            elif x == " ": 
                Ciphertext_Baudot.append(" ")

        Key_in_Alphabet = False
        Correct_Decrypt_Key_Range = False
        Correct_Decrypt_Key_Length = False
        Decrypt_Choice = st.text_input("Input your own key for encryption (1) or generate a random key (2)? ", value="")
        if Decrypt_Choice == "1":
            DecryptKey = st.text_input("Please enter the key for decryption, with the same length as the ciphertext : ", value="")
            DecryptKey = DecryptKey.upper()
            Decrypt_Key = []
            Decrypt_Key_Index = 0
            for x in DecryptKey: 
                if (x in Alphabet or x == " ") and DecryptKey[0] != " " and type(x) == type(Ciphertext_Baudot[Decrypt_Key_Index]):
                    Decrypt_Key.append(x)
                    Decrypt_Key_Index = Decrypt_Key_Index + 1
                    Key_in_Alphabet = True
                    Correct_Decrypt_Key_Range = True    
                elif DecryptKey == " " or DecryptKey[0] == " " or type(x) != type(Ciphertext_Baudot[Decrypt_Key_Index]):
                    st.error('Invalid input.', icon="🚨")
                    Correct_Decrypt_Key_Range = False
        
            Correct_Decrypt_Key_Length = False
            if Correct_Decrypt_Key_Range == True:
                if len(Decrypt_Key) != len(Ciphertext) and DecryptKey != "": 
                    st.error('Key out of range.', icon="🚨")
                    Correct_Decrypt_Key_Length = False
                elif len(Decrypt_Key) == len(Ciphertext) and len(Decrypt_Key) != 0 and DecryptKey != "":
                    Correct_Decrypt_Key_Length = True
        
        
            if Correct_Decrypt_Key_Range == True and Correct_Decrypt_Key_Length == True:
                Decrypt_Key_Baudot = []
                Decrypt_Key_Index = 0
                Plaintext = []
                for x in Ciphertext_Baudot:
                    if x == " ": 
                        Decrypt_Key.append(" ") 
                        Decrypt_Key_Baudot.append(" ") 
                        Decrypt_Key_Index = Decrypt_Key_Index + 1
                        Plaintext.append(" ")    
                    elif x != " ":
                        Decrypt_Key_Letter = Decrypt_Key[Decrpyt_Key_Index]
                        Decrypt_Key_Baudot.append(Baudot[Decrypt_Key_Letter])
                        XOR = [x]
                        XOR.append(Decrypt_Key_Baudot[Decrypt_Key_Index])
                        XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                        XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                        XOR_Result = str(XOR_Result)
                        Plaintext_Letter = get_key(XOR_Result) 
                        while Plaintext_Letter == "Key doesn't exist":
                            Decrypt_Key = st.text_input("Please enter the key for decryption, with the same length as the ciphertext : ", value="")
                            Decrypt_Key_Baudot[Decrypt_Key_Index] = Baudot[Decrypt_Key_Letter]
                            Decrypt_Key_LetterBaudot = Decrypt_Key_Baudot[Decrypt_Key_Index]
                            XOR = [x]
                            XOR.append(Decrypt_Key_LetterBaudot)
                            XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                            XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                            XOR_Result = str(XOR_Result)
                            Plaintext_Letter = get_key(XOR_Result)
                            if Plaintext_Letter != "Key doesn't exist" and " ":
                                Plaintext.append(Plaintext_Letter)
                                Decrypt_Key_Index = Decrypt_Key_Index + 1   
                                break
                        else:
                            Plaintext.append(Plaintext_Letter)
                            Decrypt_Key_Index = Decrypt_Key_Index + 1  
            elif Decrypt_Choice == "2": 
                Ciphertext_Baudot = []
                for x in Ciphertext:
                    if x != " ":
                        Ciphertext_Baudot.append(Baudot[x])
                    elif x == " ": 
                        Ciphertext_Baudot.append(" ")
                Decrypt_Key = []
                Decrypt_Key_Baudot = []
                Decrypt_Key_Index = 0
                Plaintext = []
                for x in Ciphertext_Baudot:
                    if x == " ": 
                        Decrypt_Key.append(" ") 
                        Decrypt_Key_Baudot.append(" ") 
                        Decrypt_Key_Index = Decrypt_Key_Index + 1
                        Plaintext.append(" ")    
                    elif x != " ":
                        Decrypt_Key_Letter = random.choice(Alphabet)
                        Decrypt_Key.append(Decrypt_Key_Letter)
                        Decrypt_Key_Baudot.append(Baudot[Decrypt_Key_Letter])
                        XOR = [x]
                        XOR.append(Decrypt_Key_Baudot[Decrypt_Key_Index])
                        XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                        XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                        XOR_Result = str(XOR_Result)
                        Plaintext_Letter = get_key(XOR_Result) 
                        while Plaintext_Letter == "Key doesn't exist":
                            Decrypt_Key_Letter = random.choice(Alphabet)
                            Decrypt_Key[Decrypt_Key_Index] = Decrypt_Key_Letter
                            Decrypt_Key_Baudot[Decrypt_Key_Index] = Baudot[Decrypt_Key_Letter]
                            Decrypt_Key_LetterBaudot = Decrypt_Key_Baudot[Decrypt_Key_Index]
                            XOR = [x]
                            XOR.append(Decrypt_Key_LetterBaudot)
                            XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                            XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                            XOR_Result = str(XOR_Result)
                            Plaintext_Letter = get_key(XOR_Result)
                            if Plaintext_Letter != "Key doesn't exist" and " ":
                                Plaintext.append(Plaintext_Letter)
                                Decrypt_Key_Index = Decrypt_Key_Index + 1   
                                break
                        else:
                            Plaintext.append(Plaintext_Letter)
                            Decrypt_Key_Index = Decrypt_Key_Index + 1  
        
            elif Decrypt_Choice != 1 and Decrypt_Choice != 2 and Decrypt_Choice != "": 
                st.error('Invalid input.', icon="🚨")
                Correct_Decrypt_Key = False
        
        st.write("The key is ", "".join(Decrypt_Key))
        st.write( "The plaintext is ", "".join(Plaintext))   


with tab4: 
    st.header("Level of security")
    st.write("Theoratically, Vernam cipher offers perfect security due to the unique key, making it mathematically impossible to break. ")





