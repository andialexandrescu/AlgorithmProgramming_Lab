# reinterpretare discrete knapsack problem
f = open("multime.in")
n = int(f.readline().strip())
Laux = [int(x) for x in f.readline().strip().split()]
M = int(f.readline().strip())
f.close()
L = [0]
L.extend(Laux)
sume = [[0]*(M+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, M+1):
        if L[i] <= j: # are loc elementul in suma curenta/ in ghiozdan
            sume[i][j] = max(sume[i-1][j], L[i] + sume[i-1][j - L[i]])
        else:# daca nu incape nu se modifica suma
            sume[i][j] = sume[i-1][j]

for linie in sume:
    print(*linie)

with open("multime.out", "w") as g:
    if M == sume[n][M]:
        Laux = []
        i, j = n, M
        while i != 0:
            if sume[i][j] != sume[i-1][j]:
                Laux.append(L[i])
                j = j - L[i]
            i -= 1
        for x in Laux[::-1]:
            g.write(str(x) + " ")
    else:
        g.write("Nu exista nicio submultime de suma M")


