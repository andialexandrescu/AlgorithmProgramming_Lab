import copy
def greedy(M):
    j_min = M[0].index(min(M[0]))
    M2 = copy.deepcopy(M)# nu vrem ca modif asupra elementelor lui M2
    # sa fie realizate in subprogram si asupra lui M
    for linie in M2:
        linie.sort()# ca valoarea totala a bijuteriilor
        # sa fie maxima, vom progresa cu furtul de la mic
        # la mare fiind respectata acea conditie de
        # antecedenta a solutiilor posibile

    Lcastig = [M2[0][0]]
    Lpoz = [(1, j_min+1)]
    Lsol = [M2[0][0]]
    maxim = M2[0][0]
    crt = 1
    for linie in M2[1::]:
        for i in range(n):
            if linie[i] > maxim and linie[i] > Lsol[-1]:
                Lsol.append(linie[i])
                Lcastig.append(Lcastig[-1] + linie[i])
                maxim = max(Lcastig)
                Lpoz.append((crt+1, M[crt].index(Lsol[-1])+1))
                break
        else:
            Lsol.append(linie[n-1])
            Lcastig.append(Lcastig[-1] + linie[n-1])
            Lpoz.append((crt+1, M[crt].index(Lsol[-1])+1))
        crt += 1
    return round(Lcastig[m-1], 2), Lpoz

Laux = input().strip().split()
m, n = int(Laux[0]), int(Laux[1])
M = [[0]*n for i in range(m)]
for i in range(m):
    linie = input()
    M[i]= [float(x) for x in linie.split()]

suma, Lpozitii = greedy(M)
if suma == 0 or Lpozitii == []:
    print("Imposibil")
else:
    print(suma)
    for t in Lpozitii:
        print(*t)

