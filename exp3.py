key = input("Key: ").upper().replace("J","I")
text = input("Text: ").upper().replace("J","I")

s = ""
for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if c not in s: s += c

m = [s[i:i+5] for i in range(0,25,5)]

p = ""
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else "X"
    if a == b: p += a+"X"; i += 1
    else: p += a+b; i += 2

if len(p)%2: p += "X"

c = ""
for i in range(0,len(p),2):
    a,b = p[i],p[i+1]
    r1,c1 = next((r,c) for r in range(5) for c in range(5) if m[r][c]==a)
    r2,c2 = next((r,c) for r in range(5) for c in range(5) if m[r][c]==b)

    if r1 == r2:
        c += m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
    elif c1 == c2:
        c += m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
    else:
        c += m[r1][c2] + m[r2][c1]

print("Cipher:", c)
