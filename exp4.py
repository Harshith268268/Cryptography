text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

cipher = ""

for i in range(len(text)):
    if text[i].isalpha():
        x = (ord(text[i]) - 65 + ord(key[i % len(key)]) - 65) % 26
        cipher += chr(x + 65)

print("Ciphertext:", cipher)
