key = "CIPHER"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = key + "".join(ch for ch in alphabet if ch not in key)

text = input("Enter plaintext: ").upper()
result = ""

for ch in text:
    if ch in alphabet:
        result += cipher[alphabet.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)
