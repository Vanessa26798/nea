

import streamlit as st
import random

import string
Alphabet = string.ascii_uppercase

Baudot = {

    Alphabet[0]: "00011", 
    Alphabet[1]: "11001",
    Alphabet[2]: "01110", 
    Alphabet[3]: "01001",
    Alphabet[4]: "00001", 
    Alphabet[5]: "01101",
    Alphabet[6]: "11010", 
    Alphabet[7]: "10100",
    Alphabet[8]: "00110", 
    Alphabet[9]: "01011",
    Alphabet[10]: "01111", 
    Alphabet[11]: "10010",
    Alphabet[12]: "11100", 
    Alphabet[13]: "01100",
    Alphabet[14]: "11000", 
    Alphabet[15]: "10110",
    Alphabet[16]: "10111", 
    Alphabet[17]: "01010",
    Alphabet[18]: "00101", 
    Alphabet[19]: "10000",
    Alphabet[20]: "00111",
    Alphabet[21]: "11110",
    Alphabet[22]: "10011", 
    Alphabet[23]: "11101",
    Alphabet[24]: "10101", 
    Alphabet[25]: "10001"
    }     

key_list = list(Baudot.keys())
value_list = list(Baudot.values())


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

    # if Correct_Plaintext_Range == True and Correct_Plaintext_Length == True:
    Plaintext_Baudot = []
    for x in Plaintext:
        Plaintext_Baudot.append(Baudot[x])
        st.write(Plaintext_Baudot)

    Key = []
    while len(Key) < (len(Plaintext)):
        Key.append(random.choice(Alphabet))
    st.write("The key is ", "".join(Key))

    Key_Baudot = []
    for x in Key:
        Key_Baudot.append(Baudot[x])
    st.write(Key_Baudot)

    
    Ciphertext_Baudot = []
    Key_index = 0
    for x in Plaintext_Baudot:
        XOR = [x]
        XOR.append(Key_Baudot[Key_index])
        st.write("xor", XOR)
        Result = int(XOR[0]) ^ int(XOR[1])
        st.write("Result", Result)
        Ciphertext_Baudot.append(Result)
        Key_index = Key_index + 1
    st.write(Ciphertext_Baudot)


    
    Ciphertext_LetterBaudot = []
    Ciphertext = []
    for x in Ciphertext_Baudot:
            Ciphertext_LetterBaudot.append(Ciphertext_Baudot[0])
            Ciphertext_Baudot.remove(Ciphertext_Baudot[0])
            Ciphertext_LetterBaudot = str(Ciphertext_LetterBaudot)
            st.write(Ciphertext_LetterBaudot)
        # else:
            if len(Ciphertext_LetterBaudot) % 5 == 0:
                def get_key(val):
                    for key, value in Baudot.items():
                        if val == value:
                            return key
                    return "key doesn't exist"
                Bye = get_key(Ciphertext_LetterBaudot)
                st.write("bye", Bye)
                Ciphertext.append(Bye)
    st.write(Ciphertext)
            
    


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





