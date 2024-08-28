import streamlit as st

st.title("ENCRYPTION TEACHING TOOL")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)






import random 

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# caesar
Plaintext = input("Please enter the plaintext in upper case: ")
while Plaintext.isupper() == False:
  print("Invalid plaintext")
  Plaintext = input("Please enter the plaintext in upper case: ")

Key = input("Input your own key (1) or a random key (2)? ")
if Key == "1":
  Key = input("Please enter the key: ")
  while Key.isdigit() == False:
   print("Invalid key")
   Key = input("Please enter the key: ")
elif Key == "2": 
  Key = random.randrange(1, 26)
  print(Key)
while Key != 1 and Key != 2: 
  Key = input("input your own key (1) or a random key (2)")


if Plaintext.isupper() == True and Key.isdigit() == True:
   Key = int(Key)
   Ciphertext = []
   for x in Plaintext:
     Letter = int(Alphabet.index(x))
     Letter += Key
     if Letter >= 26: 
       Letter -= 26
     Letter = Alphabet[Letter]
     Ciphertext.append(Letter) 
print("The ciphertext is ", *Ciphertext)
Occurence = {}
for x in Plaintext:
  Total_occurence = len(Plaintext)
  Count = Plaintext.count(x)
  Character_occurence = round(Count/ Total_occurence * 100)
  Occurence[x] = Character_occurence, '%'
print(Occurence)


