# reinterpretare suma maxima intr-un triunghi de numere
# varianta inapoi/ bottom-up

#(i, j) --> (i+1, j) SAU (i, j+1)
# the bottom-up approach (prefer var asta):
""" M_smax[i][j] =
{
    M[0][0], i==0 and j==0
    M[i][j] + M_smax[i][j-1], i==0 and 0<j<=n-1
    M[i][j] + M_smax[i-1][j], j==0 and 0<i<=n-1
    M[i][j] + max(M_smax[i-1][j], M_smax[i][j-1]) (restul cazurilor)
} """

with open("robot.in") as f:
    aux = f.readline().strip().split()
    m, n = int(aux[0]), int(aux[1])# m linii, n coloane
    M = []
    for linie in f.readlines():
        l = [int(x) for x in linie.strip().split()]
        M.append(l)

M_smax = [[0]*m for i in range(n)]
M_smax[0][0] = M[0][0]# primul element nu se va modifica

for i in range(m):
    for j in range(n):
        if i == 0:
            M_smax[i][j] = M[i][j] + M_smax[i][j-1]
        elif j == 0 and i != 0:
            M_smax[i][j] = M[i][j] + M_smax[i-1][j]
        elif i != 0 and j != 0:
            M_smax[i][j] = M[i][j] + max(M_smax[i-1][j], M_smax[i][j-1])

for linie in M_smax:
    print(*linie) # my beautiful child is alive

# robotul va ajunge in coltul (m-1, n-1),
# deci acolo se afla maximul indiferent de datele de intrare (sper)

# reconstituire drum:
i, j = m-1, n-1  # pornim de la coltul din dreapta jos si salvam
Lpath = [(i+1, j+1)]

while i > 0 or j > 0:
    if i == 0:
        # suntem pe prima linie, deci mergem la stanga
        j -= 1
    elif j == 0:
        # suntem pe prima coloana, deci mergem in sus
        i -= 1
    else:
        # alegem directia in functie de cel mai mare vecin
        if M_smax[i-1][j] > M_smax[i][j-1]:
            i -= 1  # mergem in sus
        else:
            j -= 1  # mergem la stanga
    Lpath.append((i+1, j+1))
Lpath.reverse()
print(Lpath)

with open("robot.out", "w") as g:
    g.write(str(M_smax[n-1][m-1]) + "\n")
    for t in Lpath:
        x, y = t
        g.write(str(x) + " " + str(y) + "\n")



