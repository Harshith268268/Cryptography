import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) == 1:
    print("Valid values")
    text = input("Enter plaintext: ").upper()
    cipher = ""

    for ch in text:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            cipher += chr(c + ord('A'))
        else:
            cipher += ch

    print("Ciphertext:", cipher)
else:
    print("Invalid value of a")
