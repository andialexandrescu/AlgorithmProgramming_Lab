#a)
def citire_matrice(nume_fisier):
    global n
    f = open(nume_fisier)
    M = []
    linii = f.readlines()
    n = len([int(x) for x in linii[0].split()])
    for i in range(n):
        linie = linii[i]
        M.append([int(x) for x in linie.split()])
    f.close()
    return M
n = 0
M1 = citire_matrice("date.in")
print(M1)
#b)
def f(M, ch, x=0, y=0):
    if ch == "c":
        for i in range(n):
            M[i][x], M[i][y] = M[i][y], M[i][x]
    elif ch == "d":
        for i in range(n):
            M[i][i], M[i][n - 1 - i] = M[i][n - 1 - i], M[i][i]
#f(M1, "c", 2, 4)
#for linie in M1:
#    print(*linie)
#print()
#f(M1, "d")
#for linie in M1:
#    print(*linie)
#c)
for i in range(n // 2 + 1):# oglindire
    f(M1, "c", i, n-i-1)
f(M1, "d")# interschimbare diag
g = open("date.out", "w")
for i in range(n):
    if (i + 1) % 2 != 0:
        for j in range(n):
            g.write(str(M1[i][j]) + " ")
    else:
        for j in range(n-1, -1, -1):
            g.write(str(M1[i][j]) + " ")
g.close()