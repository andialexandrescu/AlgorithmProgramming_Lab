s = "SUBSIR"
t = "RUSTICE"
M = [[0] * (len(t)+1) for i in range(len(s)+1)]

for i in range(1, len(s)+1):
    for j in range(len(t)+1):
        if s[i-1] == t[j-1]:
            M[i][j] = 1 + M[i-1][j-1]
        else:
            M[i][j] = max(M[i][j-1], M[i-1][j])

for linie in M:
    print(*linie)

print(f"Lungimea subsirului maxim de litere comune este: {M[len(s)][len(t)]}")
rez = ""
i = len(s)
j = len(t)
while i!=0 and j!=0:
    if s[i-1]==t[j-1]:# afisarea subsirului comun prin concatenare
        rez = s[i-1]+rez
        i -= 1
        j -= 1
    elif M[i-1][j]>=M[i][j-1]:
        i -= 1
    else:
        j -= 1

print(rez)
