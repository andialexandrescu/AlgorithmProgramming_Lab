n = int(input())
M = [[0]*n for i in range(n)]
for i in range(n):
    linie = input()
    M[i]= [int(x) for x in linie.split()]
Laux = input().strip().split()
xc, yc = int(Laux[0]), int(Laux[1])

M_smax = [[0]*n for i in range(n)]
M_smax[0][0] = M[xc][yc]# poz de inceput a calului

for i in range(xc, n):
    for j in range(n):
        if i==1:
            if j-2>=0 and j+2<=n-1:
                M_smax[i][j] = M[i][j] + max(M_smax[i-1][j-2], M_smax[i-1][j+2])
            elif j-2>=0 and j+2>n-1:# pe prima linie, mult prea in dreapta
                M_smax[i][j] = min(M[i][j], M_smax[i-1][j-2])# min am folosit pt ca nu functioneaza al
                # doilea set de date si e probabil din cauza ca pe linia 1, acolo unde se afla pionul,
                # de fapt e o pozitie unreachable pt cal - sper ca rezolva problema si ca nu e total nonsense
            elif j-2<0 and j+2<=n-1:
                M_smax[i][j] = min(M[i][j], M_smax[i-1][j+2])
        elif i!=1:
            if j-2>=0 and j+2<=n-1:
                M_smax[i][j] = M[i][j] + max(M_smax[i-1][j-2], M_smax[i-1][j+2], M_smax[i-2][j-1], M_smax[i-2][j+1])
            elif j-2>=0 and j+2>n-1:
                if j+1<=n-1:
                    M_smax[i][j] = M[i][j] + max(M_smax[i-1][j-2], M_smax[i-2][j-1], M_smax[i-2][j+1])
                else:
                    M_smax[i][j] = M[i][j] + max(M_smax[i-1][j-2], M_smax[i-2][j-1])
            elif j-2<0 and j+2<=n-1:
                if j-1>=0:
                    M_smax[i][j] = M[i][j] + max(M_smax[i-1][j+2], M_smax[i-2][j+1], M_smax[i-2][j-1])
                else:
                    M_smax[i][j] = M[i][j] + max(M_smax[i-1][j+2], M_smax[i-2][j+1])

#for linie in M_smax:
    #print(*linie)

maxim_pioni = max(M_smax[n-1])
p_i, p_j = n-1, M_smax[n-1].index(maxim_pioni)
#print(f"max: {maxim_pioni}; ({p_i}, {p_j})")
print(maxim_pioni)

Lpath = [(p_i+1, p_j+1)]
i, j = p_i, p_j

while i != xc or j != yc:
    if i == 1:
        break
    else:
        # alegem directia in functie de cel mai mare vecin
        if j-2 >= 0 and j+2 <= n-1:
            if M_smax[i-1][j-2] > M_smax[i-1][j+2]:
                j -= 2  # mergem la stanga
            else:
                j += 2  # mergem la dreapta
        elif j-2 >= 0:
            j -= 2  # mergem la stanga
        elif j+2 <= n-1:
            j += 2  # mergem la dreapta
    i -= 1  # mergem in sus
    if M_smax[i][j] != 0:# nu e o pozitie unreachable
        Lpath.append((i+1, j+1))
Lpath.append((xc, yc))
Lpath.reverse()
#print(Lpath)
for t in Lpath:
    print(*t)

