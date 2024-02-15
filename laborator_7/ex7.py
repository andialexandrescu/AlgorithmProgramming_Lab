def dp():
    global medie_cadouri, n, Lcadouri
    sume = [[0]*(medie_cadouri+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, medie_cadouri+1):
            if Lcadouri[i-1] <= j:
                sume[i][j] = max(sume[i-1][j], Lcadouri[i-1] + sume[i-1][j - Lcadouri[i-1]])
            else:
                sume[i][j] = sume[i-1][j]
    return sume
def reconstituire(S, sume):
    global Lcadouri, n
    if S == sume[n][S]:
        Laux = []
        i, j = n, S
        while i != 0:
            if sume[i][j] != sume[i-1][j]:
                Laux.append(Lcadouri[i-1])
                # indexul e i-1 pt ca incep sa indexez valorile cadourilor de la 1, in loc de 0
                j = j - Lcadouri[i-1]
            i -= 1
        Laux.reverse()
        return Laux

with open("cadouri.in") as f:
    n = int(f.readline().strip())
    Lcadouri = [int(x) for x in f.readline().strip().split()]

medie_cadouri = sum(Lcadouri)//2 # doua pers vor imparti cadourile

Lsume1 = dp()
suma1 = Lsume1[n][medie_cadouri]
for linie in Lsume1:
    print(*linie)
Lcadouri_pers1 = reconstituire(suma1, Lsume1)
Lcadouri_pers2 = []
for x in Lcadouri:
    if x not in Lcadouri_pers1:
        Lcadouri_pers2.append(x)

with open("cadouri.out", "w") as g:
    for x in Lcadouri_pers1:
        g.write(str(x) + " ")
    g.write("\n")
    for x in Lcadouri_pers2:
        g.write(str(x) + " ")

