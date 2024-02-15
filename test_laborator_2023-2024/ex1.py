#a)
def citire_numere():
    global n
    f = open("numere.in")
    L = []
    linii = f.readlines()
    n = int(len([int(x) for x in linii[0].split()]))
    for i in range(n):
        linie = [int(x) for x in linii[i].split()]
        L.append(linie)
    f.close()
    return L
n = 0
#b)
M = citire_numere()
#print(M)
k = int(input("k="))
d = {}
for i in range(n):
    for j in range(n):
        if M[i][j] not in d:
            d[M[i][j]] = 1
        else:
            k_elem = M[i].count(M[i][j])# nr de valori egale cu elem curent de pe linia curenta
            d[M[i][j]] = d[M[i][j]] + 1
            poz = M[i].index(M[i][j])
            if k_elem > 1 and j != poz:# se decrementeaza in mom in care elementul curent a mai fost in lista
                d[M[i][j]] = d[M[i][j]] - 1
#print(d)
l = []
for cheie in d.keys():
    if k <= d[cheie]:
        l.append(cheie)
l.sort(reverse = True)
with open("numere.out", "w") as g:
    for x in l:
        g.write(str(x) + "\n")
#c)
def insereaza_zerouri(M, x):
    for i in range(n):
        for j in range(n-1, -1, -1):
            if M[i][j] % (x+i) == 0:
                M[i].insert(j+1, 0)
    l_aux = []
    for i in range(n):
        if M[i].count(0) == n - M[i].count(0):
            l_aux.append(i)
    for x in range(len(l_aux)):
        M.remove(M[x])
#d)
insereaza_zerouri(M, 2)
for linie in M:
    print(*linie)