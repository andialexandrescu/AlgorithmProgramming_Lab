#a)
def citire(nume_fisier):
    f = open(nume_fisier)
    M = []
    linii = f.readlines()
    n = len([int(x) for x in linii[0].split()])
    for i in range(n):
        linie = linii[i]
        M.append([int(x) for x in linie.split()])
    f.close()
    return M, n
M1, n = citire("date.in")
print(M1)
#b)
def modif_matrice(M, *x):
    global n
    l_poz = [*x]# despachetare tuplu si plasarea val intr-o lista

    lin_ult = []
    for j in range(n):
        if j not in l_poz:
            lin_ult.append(-1)
        else:
            col_j = [M[i][j] for i in range(n) if i<j]# strict deasupra diag principale
            lin_ult.append(sum(col_j))
    M.append(lin_ult)

    col_0 = []
    for i in range(n + 1):# avem cu o linie mai mult, adica incrementam nr de coloane
        if i not in l_poz:
            col_0.append(-1)
        else:
            linie_criteriu = [M[i][j] for j in range(n) if i + j >= n - 1]
            #linia e formata din elementul pt care i+j==n-1, dar si din elementele de
            # pe linia i aflate sub diag secundara
            #print(linie_criteriu)
            maxim = max(linie_criteriu)
            col_0.append(maxim)
    #print(col_0)

    for i in range(n+1):
        M[i].insert(0, col_0[i])

    return M

#M1 = modif_matrice(M1, 1, 3, 4)
#print(M1)

#c)
M1 = modif_matrice(M1, 0, 1, 6, 3)
# 0 prima; 1 a doua; 6 ultima; n=7 impar => una din mijloc,
# din ce trebuie sa se afisezeze pe ecran numarand liniile de
# sus in jos de la 0 rezulta ca pozitia apelata trebuie sa fie 3
for linie in M1:
    for x in linie:
        s = str(x).rjust(4, " ")# right justified
        print(s, end=" ")
    print()
