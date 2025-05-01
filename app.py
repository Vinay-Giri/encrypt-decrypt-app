import streamlit as st

# Vigenère Cipher Functions
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# Streamlit Interface
st.title("🔐 Message Encryption/Decryption Tool by Vinay")

option = st.radio("Choose Operation", ("Decrypt", "Encrypt"))

message = st.text_area("Enter the message")
key = st.text_input("Enter the key")

if st.button(option):
    if not message or not key:
        st.warning("Please enter both message and key.")
    else:
        if option == "Decrypt":
            result = decrypt(message, key)
            st.success(f"Decrypted Message: {result}")
        else:
            result = encrypt(message, key)
            st.success(f"Encrypted Message: {result}")
