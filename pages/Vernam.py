
import streamlit as st
import random
import pandas as pd

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

def Get_Letter(val):
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
    st.header("Encrypt a plaintext")

    def Input_Plaintext():
        global Plaintext    
        Plaintext = st.text_input("Please enter the plaintext in upper case, within 10-30 characters: ", value="")    
        Plaintext = Plaintext.upper()

    def Check_Plaintext_in_Alphabet():        
        global Plaintext_in_Alphabet
        for x in Plaintext: 
            if (x in Alphabet or x == " ") and Plaintext[0] != " ":
                Plaintext_in_Alphabet = True
            else:
                Plaintext_in_Alphabet = False

    def Check_Plaintext_Range():
        global Correct_Plaintext_Range
        if Plaintext_in_Alphabet == False and Plaintext != "":
            st.error('Invalid plaintext.', icon="🚨")
            Correct_Plaintext_Range = False
        elif Plaintext_in_Alphabet == True or Plaintext == " ":
            Correct_Plaintext_Range = True

    def Check_Plaintext_Length():            
        global Correct_Plaintext_Length
        if Correct_Plaintext_Range == True:
            if (len(Plaintext) < 10 or len(Plaintext) > 30) and Plaintext != "": 
                st.error('Plaintext out of range.', icon="🚨")
                Correct_Plaintext_Length = False
            elif len(Plaintext) >= 10 and len(Plaintext) <= 30 and len(Plaintext) != 0 and Plaintext != "":
                Correct_Plaintext_Length = True

    def Plaintext_Baudot():
        global Plaintext_Baudot
        if Correct_Plaintext_Range == True and Correct_Plaintext_Length == True:
             Plaintext_Baudot = []
             for x in Plaintext:
                if x != " ":
                    Plaintext_Baudot.append(Baudot[x])
                elif x == " ": 
                    Plaintext_Baudot.append(" ")

    def Input_Key_Choice():
        global Encrypt_Choice
        Encrypt_Choice = ""
        if Correct_Plaintext_Range == True and Correct_Plaintext_Length == True:
            Encrypt_Choice = st.text_input("Input your own key for encryption (1) or generate a random key (2)? ", value="")

    def Get_Encrypt_Key(): 
        global Encrypt_Key_Input  
        global Correct_Encrypt_Key_Range
        global Correct_Encrypt_Key_Length
        Encrypt_Key_Input = ""
        if Encrypt_Choice == "1":
            Encrypt_Key_Input = st.text_input("Please input the key for encryption, with the same length as the plaintext: ", value="")
            Encrypt_Key_Input = Encrypt_Key_Input.upper()
        elif Encrypt_Choice == "2":
            Correct_Encrypt_Key_Range = True
            Correct_Encrypt_Key_Length = True
        elif Encrypt_Choice != "1" and Encrypt_Choice != "2" and Encrypt_Choice != "": 
            st.error('Invalid input.', icon="🚨")

    def Check_Encrypt_Key_Range():
        global Correct_Encrypt_Key_Range
        global Encrypt_Key
        Encrypt_Key = []
        Encrypt_Key_Index = 0
        if Encrypt_Choice == "1":
            for x in Encrypt_Key_Input: 
             if (x in Alphabet or x == " ") and Encrypt_Key_Input[0] != " " and type(x) == type(Plaintext_Baudot[Encrypt_Key_Index]):
                 Encrypt_Key.append(x)
                 Correct_Encrypt_Key_Range = True    
             elif (x not in Alphabet and Encrypt_Key_Input != "") or (Encrypt_Key_Input == " " or Encrypt_Key_Input[0] == " " or type(x) != type(Plaintext_Baudot[Encrypt_Key_Index])):
                 st.error('Invalid input.', icon="🚨")
                 Correct_Encrypt_Key_Range = False
                 break
    
    def Check_Encrypt_Key_Length():
        global Correct_Encrypt_Key_Length
        if Encrypt_Choice == "1" and Correct_Encrypt_Key_Range == True:
         if len(Encrypt_Key) != len(Plaintext) and Encrypt_Key_Input != "": 
             st.error('Key out of range.', icon="🚨")
             Correct_Encrypt_Key_Length = False
         elif len(Encrypt_Key) == len(Plaintext) and len(Encrypt_Key) != 0 and Encrypt_Key != "":
             Correct_Encrypt_Key_Length = True

    def Encryption():
        global Correct_Encrypt_Key
        global Correct_Encrypt_Key_Range
        global Correct_Encrypt_Key_Length
        global Encrypt_Key
        global Encrypt_Key_Baudot
        global Ciphertext_Baudot
        global Ciphertext
        if Correct_Encrypt_Key_Range == True and Correct_Encrypt_Key_Length == True:
            if Encrypt_Choice == "1":
                Encrypt_Key_Baudot = []
                Encrypt_Key_Index = 0
                Ciphertext_Baudot = []
                Ciphertext = []
                for x in Plaintext_Baudot:
                 if x == " ": 
                     Encrypt_Key.append(" ") 
                     Encrypt_Key_Baudot.append(" ") 
                     Encrypt_Key_Index = Encrypt_Key_Index + 1
                     Ciphertext_Baudot.append(" | ")
                     Ciphertext.append(" ")    
                 elif x != " ":
                     Encrypt_Key_Letter = Encrypt_Key[Encrypt_Key_Index]
                     Encrypt_Key_Baudot.append(Baudot[Encrypt_Key_Letter])
                     XOR = [x]
                     XOR.append(Encrypt_Key_Baudot[Encrypt_Key_Index])
                     XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                     XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                     XOR_Result = str(XOR_Result)
                     Ciphertext_Letter = Get_Letter(XOR_Result) 
                     if Ciphertext_Letter == "Key doesn't exist":
                         st.error('Invalid key.', icon="🚨")
                         Correct_Encrypt_Key = False
                         break
                     elif Ciphertext_Letter != "Key doesn't exist" and " ":
                         Ciphertext.append(Ciphertext_Letter)
                         Encrypt_Key_Index = Encrypt_Key_Index + 1
                     Ciphertext_Baudot.append(XOR_Result)
                     Ciphertext_Baudot.append(" | ")
                Correct_Encrypt_Key = True
                Correct_Encrypt_Key_Range = True
                Correct_Encrypt_Key_Length = True
            elif Encrypt_Choice == "2":
                Encrypt_Key = []
                Encrypt_Key_Baudot = []
                Encrypt_Key_Index = 0
                Ciphertext_Baudot = []
                Ciphertext = []
                for x in Plaintext_Baudot:
                    if x == " ": 
                        Encrypt_Key.append(" ") 
                        Encrypt_Key_Baudot.append(" ") 
                        Encrypt_Key_Index = Encrypt_Key_Index + 1
                        Ciphertext_Baudot.append(" | ")
                        Ciphertext.append(" ")
                    elif x != " ":
                        Encrypt_Key_Letter = random.choice(Alphabet)
                        Encrypt_Key.append(Encrypt_Key_Letter)
                        Encrypt_Key_Baudot.append(Baudot[Encrypt_Key_Letter])
                        XOR = [x]
                        XOR.append(Encrypt_Key_Baudot[Encrypt_Key_Index])
                        XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                        XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                        XOR_Result = str(XOR_Result)
                        Ciphertext_Letter = Get_Letter(XOR_Result) 
                        while Ciphertext_Letter == "Key doesn't exist":
                            Encrypt_Key_Letter = random.choice(Alphabet)
                            Encrypt_Key[Encrypt_Key_Index] = Encrypt_Key_Letter
                            Encrypt_Key_Baudot[Encrypt_Key_Index] = Baudot[Encrypt_Key_Letter]
                            Encrypt_Key_LetterBaudot = Encrypt_Key_Baudot[Encrypt_Key_Index]
                            XOR = [x]
                            XOR.append(Encrypt_Key_LetterBaudot)
                            XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                            XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                            XOR_Result = str(XOR_Result)
                            Ciphertext_Letter = Get_Letter(XOR_Result)
                            if Ciphertext_Letter != "Key doesn't exist" and " ":
                                Ciphertext.append(Ciphertext_Letter)
                                Encrypt_Key_Index = Encrypt_Key_Index + 1   
                                break
                        else:
                            Ciphertext.append(Ciphertext_Letter)
                            Encrypt_Key_Index = Encrypt_Key_Index + 1 
                        Ciphertext_Baudot.append(XOR_Result)
                        Ciphertext_Baudot.append(" | ")
                    Correct_Encrypt_Key = True
            elif Encrypt_Choice != "1" and Encrypt_Choice != "2" and Encrypt_Choice != "":
                st.error('Invalid input.', icon="🚨")

    def Output_Plaintext_Baudot():
     if (Encrypt_Choice == "1" or "2") and Correct_Encrypt_Key == True and Correct_Encrypt_Key_Range == True and Correct_Encrypt_Key_Length == True:
        if len(Ciphertext) == len(Plaintext):
            Spaced_Plaintext_Baudot = []
            for x in Plaintext_Baudot:
                if x == " ": 
                    Spaced_Plaintext_Baudot.append(" | ")
                elif x != " ":
                    Spaced_Plaintext_Baudot.append(x)
                    Spaced_Plaintext_Baudot.append(" | ")
            st.write("The key is ", "".join(Encrypt_Key))
            st.write("The plaintext and key of each character are converted to Baudot, and XOR is carried out:") 
            st.write("".join(Spaced_Plaintext_Baudot), " - Plaintext")
            Spaced_Encrypt_Key_Baudot = []
            for x in Encrypt_Key_Baudot:
                if x == " ": 
                    Spaced_Encrypt_Key_Baudot.append(" | ")
                elif x != " ":
                    Spaced_Encrypt_Key_Baudot.append(x)
                    Spaced_Encrypt_Key_Baudot.append(" | ")
            st.write("".join(Spaced_Encrypt_Key_Baudot), " - Key")
            st.write("".join(Ciphertext_Baudot), " - Ciphertext")
            st.write("Therefore, the ciphertext is ", "".join(Ciphertext))   

    
    Plaintext_in_Alphabet = False
    Correct_Plaintext_Range = False
    Correct_Plaintext_Length = False
    Correct_Encrypt_Key_Range = False
    Correct_Encrypt_Key_Length = False
    Correct_Encrypt_Key = False
    
    Input_Plaintext()
    Check_Plaintext_in_Alphabet()
    Check_Plaintext_Range()
    Check_Plaintext_Length()
    Plaintext_Baudot()
    Input_Key_Choice()
    Get_Encrypt_Key()
    Check_Encrypt_Key_Range()
    Check_Encrypt_Key_Length()
    Encryption()
    Output_Plaintext_Baudot()


with tab3:
    st.header("Decrypt a ciphertext")

    def Input_Ciphertext():
        global Ciphertext    
        Ciphertext = st.text_input("Please enter the ciphertext in upper case, within 10-30 characters: ", value="")    
        Ciphertext = Ciphertext.upper()

    def Check_Ciphertext_in_Alphabet():        
        global Ciphertext_in_Alphabet
        for x in Ciphertext: 
            if (x in Alphabet or x == " ") and Ciphertext[0] != " ":
                Ciphertext_in_Alphabet = True
            else:
                Ciphertext_in_Alphabet = False

    def Check_Ciphertext_Range():
        global Correct_Ciphertext_Range
        if Ciphertext_in_Alphabet == False and Ciphertext != "":
            st.error('Invalid ciphertext.', icon="🚨")
            Correct_Ciphertext_Range = False
        elif Ciphertext_in_Alphabet == True or Ciphertext == " ":
            Correct_Ciphertext_Range = True

    def Check_Ciphertext_Length():            
        global Correct_Ciphertext_Length
        if Correct_Ciphertext_Range == True:
            if (len(Ciphertext) < 10 or len(Ciphertext) > 30) and Ciphertext != "": 
                st.error('Ciphertext out of range.', icon="🚨")
                Correct_Ciphertext_Length = False
            elif len(Ciphertext) >= 10 and len(Ciphertext) <= 30 and len(Ciphertext) != 0 and Ciphertext != "":
                Correct_Ciphertext_Length = True

    def Ciphertext_Baudot():
        global Ciphertext_Baudot
        if Correct_Ciphertext_Range == True and Correct_Ciphertext_Length == True:
             Ciphertext_Baudot = []
             for x in Ciphertext:
                if x != " ":
                    Ciphertext_Baudot.append(Baudot[x])
                elif x == " ": 
                    Ciphertext_Baudot.append(" ")

    def Input_Key_Choice():
        global Decrypt_Choice
        Decrypt_Choice = ""
        if Correct_Ciphertext_Range == True and Correct_Ciphertext_Length == True:
            Decrypt_Choice = st.text_input("Input your own key for decryption (1) or generate a random key (2)? ", value="")

    def Get_Decrypt_Key(): 
        global Decrypt_Key_Input  
        global Correct_Decrypt_Key_Range
        global Correct_Decrypt_Key_Length
        Decrypt_Key_Input = ""
        if Decrypt_Choice == "1":
            Decrypt_Key_Input = st.text_input("Please input the key for decryption, with the same length as the ciphertext: ", value="")
            Decrypt_Key_Input = Decrypt_Key_Input.upper()
        elif Decrypt_Choice == "2":
            Correct_Decrypt_Key_Range = True
            Correct_Decrypt_Key_Length = True
        elif Decrypt_Choice != "1" and Decrypt_Choice != "2" and Decrypt_Choice != "": 
            st.error('Invalid input.', icon="🚨")

    def Check_Decrypt_Key_Range():
        global Correct_Decrypt_Key_Range
        global Decrypt_Key
        Decrypt_Key = []
        Decrypt_Key_Index = 0
        if Decrypt_Choice == "1":
            for x in Decrypt_Key_Input: 
             if (x in Alphabet or x == " ") and Decrypt_Key_Input[0] != " " and type(x) == type(Ciphertext_Baudot[Decrypt_Key_Index]):
                 Decrypt_Key.append(x)
                 Correct_Decrypt_Key_Range = True    
             elif (x not in Alphabet and Decrypt_Key_Input != "") or (Decrypt_Key_Input == " " or Decrypt_Key_Input[0] == " " or type(x) != type(Ciphertext_Baudot[Decrypt_Key_Index])):
                 st.error('Invalid input.', icon="🚨")
                 Correct_Decrypt_Key_Range = False
                 break
    
    def Check_Decrypt_Key_Length():
        global Correct_Decrypt_Key_Length
        if Decrypt_Choice == "1" and Correct_Decrypt_Key_Range == True:
         if len(Decrypt_Key) != len(Ciphertext) and Decrypt_Key_Input != "": 
             st.error('Key out of range.', icon="🚨")
             Correct_Decrypt_Key_Length = False
         elif len(Decrypt_Key) == len(Ciphertext) and len(Decrypt_Key) != 0 and Decrypt_Key != "":
             Correct_Decrypt_Key_Length = True

    def Decryption():
        global Correct_Decrypt_Key
        global Correct_Decrypt_Key_Range
        global Correct_Decrypt_Key_Length
        global Decrypt_Key
        global Decrypt_Key_Baudot
        global Plaintext_Baudot
        global Plaintext
        if Correct_Decrypt_Key_Range == True and Correct_Decrypt_Key_Length == True:
            if Decrypt_Choice == "1":
                Decrypt_Key_Baudot = []
                Decrypt_Key_Index = 0
                Plaintext_Baudot = []
                Plaintext = []
                for x in Ciphertext_Baudot:
                 if x == " ": 
                     Decrypt_Key.append(" ") 
                     Decrypt_Key_Baudot.append(" ") 
                     Decrypt_Key_Index = Decrypt_Key_Index + 1
                     Plaintext_Baudot.append(" | ")
                     Plaintext.append(" ")    
                 elif x != " ":
                     Decrypt_Key_Letter = Decrypt_Key[Decrypt_Key_Index]
                     Decrypt_Key_Baudot.append(Baudot[Decrypt_Key_Letter])
                     XOR = [x]
                     XOR.append(Decrypt_Key_Baudot[Decrypt_Key_Index])
                     XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
                     XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
                     XOR_Result = str(XOR_Result)
                     Plaintext_Letter = Get_Letter(XOR_Result) 
                     if Plaintext_Letter == "Key doesn't exist":
                         st.error('Invalid key.', icon="🚨")
                         Correct_Decrypt_Key = False
                         break
                     elif Plaintext_Letter != "Key doesn't exist" and " ":
                         Plaintext.append(Plaintext_Letter)
                         Decrypt_Key_Index = Decrypt_Key_Index + 1
                     Plaintext_Baudot.append(XOR_Result)
                     Plaintext_Baudot.append(" | ")
                Correct_Decrypt_Key = True
                Correct_Decrypt_Key_Range = True
                Correct_Decrypt_Key_Length = True
            elif Decrypt_Choice == "2":
                Decrypt_Key = []
                Decrypt_Key_Baudot = []
                Decrypt_Key_Index = 0
                Plaintext_Baudot = []
                Plaintext = []
                for x in Ciphertext_Baudot:
                    if x == " ": 
                        Decrypt_Key.append(" ") 
                        Decrypt_Key_Baudot.append(" ") 
                        Decrypt_Key_Index = Decrypt_Key_Index + 1
                        Plaintext_Baudot.append(" | ")
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
                        Plaintext_Letter = Get_Letter(XOR_Result) 
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
                            Plaintext_Letter = Get_Letter(XOR_Result)
                            if Plaintext_Letter != "Key doesn't exist" and " ":
                                Plaintext.append(Plaintext_Letter)
                                Decrypt_Key_Index = Decrypt_Key_Index + 1   
                                break
                        else:
                            Plaintext.append(Plaintext_Letter)
                            Decrypt_Key_Index = Decrypt_Key_Index + 1 
                        Plaintext_Baudot.append(XOR_Result)
                        Plaintext_Baudot.append(" | ")
                    Correct_Decrypt_Key = True
            elif Decrypt_Choice != "1" and Decrypt_Choice != "2" and Decrypt_Choice != "":
                st.error('Invalid input.', icon="🚨")

    def Output_Plaintext_Baudot():
     if (Decrypt_Choice == "1" or "2") and Correct_Decrypt_Key == True and Correct_Decrypt_Key_Range == True and Correct_Decrypt_Key_Length == True:
        if len(Ciphertext) == len(Plaintext):
            Spaced_Ciphertext_Baudot = []
            for x in Ciphertext_Baudot:
                if x == " ": 
                    Spaced_Ciphertext_Baudot.append(" | ")
                elif x != " ":
                    Spaced_Ciphertext_Baudot.append(x)
                    Spaced_Ciphertext_Baudot.append(" | ")
            st.write("The key is ", "".join(Decrypt_Key))
            st.write("The ciphertext and key of each character are converted to Baudot, and XOR is carried out:") 
            st.write("".join(Spaced_Ciphertext_Baudot), " - Ciphertext")
            Spaced_Decrypt_Key_Baudot = []
            for x in Decrypt_Key_Baudot:
                if x == " ": 
                    Spaced_Decrypt_Key_Baudot.append(" | ")
                elif x != " ":
                    Spaced_Decrypt_Key_Baudot.append(x)
                    Spaced_Decrypt_Key_Baudot.append(" | ")
            st.write("".join(Spaced_Decrypt_Key_Baudot), " - Key")
            st.write("".join(Plaintext_Baudot), " - Plaintext")
            st.write("Therefore, the plaintext is ", "".join(Plaintext))   

    
    Ciphertext_in_Alphabet = False
    Correct_Ciphertext_Range = False
    Correct_Ciphertext_Length = False
    Correct_Decrypt_Key_Range = False
    Correct_Decrypt_Key_Length = False
    Correct_Decrypt_Key = False
    
    Input_Ciphertext()
    Check_Ciphertext_in_Alphabet()
    Check_Ciphertext_Range()
    Check_Ciphertext_Length()
    Ciphertext_Baudot()
    Input_Key_Choice()
    Get_Decrypt_Key()
    Check_Decrypt_Key_Range()
    Check_Decrypt_Key_Length()
    Decryption()
    Output_Plaintext_Baudot()
         

with tab4: 
    st.header("Level of security")
    Plaintext = "VERNAM ENCRYPTION"
    Plaintext_Baudot = []
    Key = list("KWOFQC MYDXPRPGIJ")
    Key_Baudot = []    
    Ciphertext_Baudot = []
    Ciphertext = []
    for x in Plaintext:
        if x != " ":
            Plaintext_Baudot.append(Baudot[x])
        elif x == " ": 
            Plaintext_Baudot.append(" ")
    for x in Key:
        if x != " ":
            Key_Baudot.append(Baudot[x])
        elif x == " ": 
            Key_Baudot.append(" ")
    Key_Index = 0
    for x in Plaintext_Baudot:
        if x == " ": 
            Key.append(" ") 
            Key_Index = Key_Index + 1
            Ciphertext.append(" ")    
        elif x != " ":
            XOR = [x]
            XOR.append(Key_Baudot[Key_Index])
            XOR_Result = int(XOR[0], 2) ^ int(XOR[1], 2)
            XOR_Result = bin(XOR_Result)[2:].zfill(len(XOR[0]))
            XOR_Result = str(XOR_Result)
            Ciphertext_Letter = Get_Letter(XOR_Result) 
            Ciphertext.append(Ciphertext_Letter)
            Key_Index = Key_Index + 1 
    st.write("If the plaintext is " + Plaintext + ", the key is " + "".join(Key) + ", the ciphertext is " + "".join(Ciphertext) + ":")
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
    st.write("However, even though some character has higher occurrence, it is mathematically impossible to break due to the unique key for each character which offers prefect security.") 
    st.write("Therefore, level of security for Vernam cipher is higher.")





