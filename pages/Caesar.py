import streamlit as st
import random
import pandas as pd


Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
st.header("Caesar cipher")
tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Level of security"])

with tab1:
    st.header("History")
    col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn.britannica.com/17/193717-050-030D75E3/Julius-Caesar-statue-Rome-Italy.jpg?w=300", caption="Bronze sculpture of Julius Caesar in Rome")


with col2:
    st.write("The Caesar Cipher is one of the oldest cryptographic algorithms. It is named after Julius Caesar who initially used it to protect sensitive military messages, allowing him to communicate with his military generals.  ")



with tab2:
    st.header("Encryt a plaintext")

    

    
#     class Input:
#         def __init__(self):
#             self.Plaintext = st.text_input("Please enter the plaintext in upper case, within 10-30 characters: ", value="")
#             self.Plaintext = self.Plaintext.upper()
            
#             self.Plaintext_Range = False
#             self.Plaintext_in_Alphabet = False
#             self.Plaintext_Length = False
            
#             for x in self.Plaintext: 
#                 if (x in Alphabet or x == " ") and self.Plaintext[0] != " ":
#                   self.Plaintext_in_Alphabet = True
#                 else:
#                   self.Plaintext_in_Alphabet = False
#                   if self.Plaintext_in_Alphabet == False and self.Plaintext != "":
#                     st.error('Invalid plaintext.', icon="🚨")
#                     self.Plaintext_Range = False
#                     break
#                   elif self.Plaintext_in_Alphabet == True or self.Plaintext == " ":
#                     self.Plaintext_Range = True
#             return self.Plaintext_Range

#             if self.Plaintext_Range == True:
#                 if (len(self.Plaintext) < 10 or len(self.Plaintext) > 30) and self.Plaintext != "": 
#                     st.error('Plaintext out of range.', icon="🚨")
#                     self.Plaintext_Length = False
#                 elif len(self.Plaintext) >= 10 and len(self.Plaintext) <= 30 and len(self.Plaintext) != 0 and self.Plaintext != "":
#                     self.Plaintext_Length = True
#             return self.Plaintext_Length


# class Input:
#     def __init__(self):
#         self.Plaintext = st.text_input("Please enter the plaintext in upper case, within 10-30 characters: ", value="")
#         self.Plaintext = self.Plaintext.upper()
        
#         self.Plaintext_Range = False
#         self.Plaintext_in_Alphabet = False
#         self.Plaintext_Length = False

#     def check_plaintext_range(self):
#         for x in self.Plaintext: 
#             if (x in Alphabet or x == " ") and self.Plaintext[0] != " ":
#               self.Plaintext_in_Alphabet = True
#             else:
#               self.Plaintext_in_Alphabet = False
#               if self.Plaintext_in_Alphabet == False and self.Plaintext != "":
#                 st.error('Invalid plaintext.', icon="🚨")
#                 self.Plaintext_Range = False
#                 break
#               elif self.Plaintext_in_Alphabet == True or self.Plaintext == " ":
#                 self.Plaintext_Range = True
#         return self.Plaintext_Range

#     def check_plaintext_range(self):
#         if self.Plaintext_Range == True:
#             if (len(self.Plaintext) < 10 or len(self.Plaintext) > 30) and self.Plaintext != "": 
#                 st.error('Plaintext out of range.', icon="🚨")
#                 self.Plaintext_Length = False
#             elif len(self.Plaintext) >= 10 and len(self.Plaintext) <= 30 and len(self.Plaintext) != 0 and self.Plaintext != "":
#                 self.Plaintext_Length = True
#         return self.Plaintext_Length


    
# class Key: 
#   def __init__(self):
#     self.Choice = st.text_input("Input your own key for encryption (1) or generate a random key (2)? ", value="")
#     self.Key = 0
#     self.Check_Key = False

#     def check_key_choice(self):
#         if self.Choice == "1":
#             self.Key = st.text_input("Please enter the key for encryption, within 1-25: ", value="")
#             if self.Key.isdigit() == True:
#                 self.Key = int(self.Key)
#                 if self.Key < 1 or self.Key > 25: 
#                     st.error('Invalid input.', icon="🚨")
#                     self.Check_Key = False
#                 elif self.Key >= 1 and self.Key <= 25:
#                     st.write("The key is ", self.Key)
#                     self.Check_Key = True
#             elif self.Key.isdigit() == False and self.Key != "": 
#                  st.error('Invalid input.', icon="🚨")
#                  self.Check_Key = False
#         elif self.Choice == "2": 
#             self.Key = random.randrange(1, 26)
#             self.Key = int(self.Key)
#             st.write("The key is ", Key)
#             self.Check_Key = True
#         elif self.Encrypt_Choice != 1 and self.Encrypt_Choice != 2 and self.Encrypt_Choice != "": 
#             st.error('Invalid input.', icon="🚨")
#             self.Check_Encrypt_Key = False

# class Encrypt(Key):
#     def __init__(self):
#         self.Check_Key = False
#         self.Key = ""


# class Encrypt(Input):
#     def __init__(self):
#         self.Check_Key = False


#     def get_length(self):
#         return self.Plaintext_Length
#         if self.Plaintext_Length == True and self.Plaintext != "":
#             st.write("123")
#             Encrypt(Key) 


# def Main():
#   Input(self)

# if __name__ == "__main__":
#   Main()

    
    # self.Encrypt_Choice = st.text_input("Input your own key for encryption (1) or generate a random key (2)? ", value="")
    # if self.Encrypt_Choice == "1":
    #     self.Encrypt_Key = st.text_input("Please enter the key for encryption, within 1-25: ", value="")
    #     if self.Encrypt_Key.isdigit() == True:
    #         self.Encrypt_Key = int(self.Encrypt_Key)
    #         if self.Encrypt_Key < 1 or self.Encrypt_Key > 25: 
    #             st.error('Invalid input.', icon="🚨")
    #             self.Check_Encrypt_Key = False
    #         elif self.Encrypt_Key >= 1 and self.Encrypt_Key <= 25:
    #             st.write("The key is ", Encrypt_Key)
    #             self.Check_Encrypt_Key = True
    #     elif self.Encrypt_Key.isdigit() == False and self.Encrypt_Key != "": 
    #         st.error('Invalid input.', icon="🚨")
    #         self.Check_Encrypt_Key = False
    # elif self.Encrypt_Choice == "2": 
    #     self.Encrypt_Key = random.randrange(1, 26)
    #     self.Encrypt_Key = int(self.Encrypt_Key)
    #     st.write("The key is ", Encrypt_Key)
    #     self.Check_Encrypt_Key = True
    # elif self.Encrypt_Choice != 1 and self.Encrypt_Choice != 2 and self.Encrypt_Choice != "": 
    #         st.error('Invalid input.', icon="🚨")
    #         self.Check_Encrypt_Key = False

    # if Correct_Plaintext_Range == True and Correct_Encrypt_Key == True and Correct_Plaintext_Length == True:
    #    Ciphertext = ["The ciphertext is "]
    #    for x in Plaintext:
    #      if x == " ":
    #          Ciphertext.append(x)
    #      else: 
    #          Letter_index = int(Alphabet.index(x))
    #          Letter_index += Encrypt_Key
    #          while Letter_index >= 25: 
    #              Letter_index -= 26
    #          Letter = Alphabet[Letter_index]
    #          Ciphertext.append(Letter)
    #    st.write("".join(Ciphertext))



    # if Correct_Plaintext_Range == True and Correct_Encrypt_Key == True and Correct_Plaintext_Length == True:
    #    Ciphertext = ["The ciphertext is "]
    #    for x in Plaintext:
    #      if x == " ":
    #          Ciphertext.append(x)
    #      else: 
    #          Letter_index = int(Alphabet.index(x))
    #          Letter_index += Encrypt_Key
    #          while Letter_index >= 25: 
    #              Letter_index -= 26
    #          Letter = Alphabet[Letter_index]
    #          Ciphertext.append(Letter)
    #    st.write("".join(Ciphertext))





    

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
    Plaintext = "AAABCDE"
    st.write("The plaintext is " + Plaintext)
    Character = []
    Occurance = []
    for x in Plaintext:
      Total_occurance = len(Plaintext)
      Count = Plaintext.count(x)
      Character_occurance = round(Count/ Total_occurance * 100)
      if x not in Character:
          Character.append(x)
          Occurance.append(Character_occurance)
          if Character.index(x) > 0:
              Last_Character_Index = Character.index(x) - 1
              if int(Occurance[Last_Character_Index]) > int(Occurance[Character.index(x)]):
                  Highest_Occurance_Character = Character[Last_Character_Index]
                  Highest_Occurance = Occurance[Last_Character_Index]
              elif int(Occurance[Last_Character_Index]) < int(Occurance[Character.index(x)]):
                  Highest_Occurance_Character = Character[x]
                  Highest_Occurance = Occurance[x]
    
    chart_data = pd.DataFrame({"Character": Character, "Occurance": Occurance})
    st.bar_chart(chart_data, x = "Character", y = "Occurance", horizontal=True)
    st.write("The character with the highest occurance is " + Highest_Occurance_Character)









