import math

cipher = input("Enter ciphertext: ").upper()

# Assume most frequent plaintext letters are E and T
for a in range(1, 26):
    if math.gcd(a, 26) == 1:
        for b in range(26):
            result = ""
            for ch in cipher:
                if ch.isalpha():
                    c = ord(ch) - ord('A')
                    inv = pow(a, -1, 26)
                    p = (inv * (c - b)) % 26
                    result += chr(p + ord('A'))
                else:
                    result += ch

            if result.count('E') > 0 and result.count('T') > 0:
                if a == 1 and b == 1:
                    print("Possible plaintext:", result)
