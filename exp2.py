import string

plaintext = input("Enter the plaintext: ")

# Substitution alphabet
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

result = ""

for ch in plaintext:
    if ch.isalpha():
        if ch.isupper():
            result += key[ord(ch) - ord('A')]
        else:
            result += key[ord(ch.upper()) - ord('A')].lower()
    else:
        result += ch

print("Ciphertext:", result)
