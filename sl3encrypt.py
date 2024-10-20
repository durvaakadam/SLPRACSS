def generate_key(plaintext, key):
    key_list = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_list.append(key[key_index % len(key)].upper())
            key_index += 1
        else:
            key_list.append(char)  # Preserve non-alphabet characters

    return "".join(key_list)

def print_keystream(key):
    keystream = [ord(char) - ord('A') for char in key if char.isalpha()]
    print(f"Keystream: {keystream}")

def encrypt_vigenere(plaintext, key):
    ciphertext = []
    generated_key = generate_key(plaintext, key)

    print(f"Generated Key: {generated_key}")  # Print the repeating key
    print_keystream(generated_key)  # Print the keystream

    key_index = 0  # Initialize key index for mapping to key
    for i in range(len(plaintext)):
        char = plaintext[i]
        
        if char.isalpha():  # Only process alphabetic characters
            key_char = generated_key[key_index]
            if char.isupper():
                cipher_shift = (ord(char) - ord('A') + ord(key_char) - ord('A')) % 26
                ciphertext.append(chr(cipher_shift + ord('A')))
            else:
                cipher_shift = (ord(char) - ord('a') + ord(key_char) - ord('A')) % 26
                ciphertext.append(chr(cipher_shift + ord('a')))
            key_index += 1  # Increment key index only for alphabetic characters
        else:
            ciphertext.append(char)  # Preserve non-alphabet characters (like spaces)

    return "".join(ciphertext)

# Input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ").upper()
ciphertext = encrypt_vigenere(plaintext, key)
print(f"Ciphertext: {ciphertext}")
