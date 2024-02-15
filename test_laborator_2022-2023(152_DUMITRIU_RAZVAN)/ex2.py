#a)
def citire_matrice(nume_fisier):
    global n
    f = open(nume_fisier)
    M = []
    n = int(f.readline().strip())
    s_nr = f.readline()
    linii = [int(x) for x in s_nr.split()]
    poz = 0
    for i in range(len(s_nr.split()) // n):
        linie = linii[poz:poz+n:]
        M.append(linie)
        poz += n
        #print(i, linie, sep=" -> ")
    f.close()
    return M
n = 0
M1 = citire_matrice("matrice.in")
print(M1)
#b)
def duplicare(M, *indici):
    for i in range(n-1, -1, -1):
        if i in indici:
            M.insert(i+1, M[i].copy())
#duplicare(M1, 0, 2)
#print(M1)
#c)
duplicare(M1, 0, 1)
M1[0][0] += 1
for linie in M1:
    print(*linie)

