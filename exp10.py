matrix = [
    "MFHIK",
    "UNOPQ",
    "ZVWXY",
    "ELARG",
    "DSTBC"
]

def encrypt(text):
    text = ''.join(c for c in text.upper() if c.isalpha())
    text = text.replace('J', 'I')

    if len(text) % 2:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

text = "Must see you over Cadogan West. Coming at once"
print("Ciphertext:", encrypt(text))
