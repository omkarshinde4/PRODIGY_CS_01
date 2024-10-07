def encrypt(plain_text,key,cipher_text):
   for i in plain_text:
    if i== " ":
        cipher_text+=" "    
    else:
        cipher_text+=chr((ord(i)+key-65)%26+65)
   return cipher_text
def decrypt(plain_text,key,cipher_text):
   for i in cipher_text:
    if i== " ":
        plain_text+=" "    
    else:
        plain_text+=chr((ord(i)+key-65)%26-65)
   return plain_text
plain_text=input("enter string:")
plain_text=plain_text.upper()
key=int(input("enter key:"))
cipher_text=" "
e=encrypt(plain_text,key,cipher_text)
print("cipher_text(encrypted):",e)
d=decrypt(plain_text,key,cipher_text)
print("cipher_text(decrypt):", d)