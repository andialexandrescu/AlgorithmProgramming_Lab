def citire(nume_fisier):
    with open(nume_fisier) as f:
        linii = f.readlines()
        B = [int(x) for x in linii[0].split()]
        s = int(linii[1])
    return B, s

def greedy(B, s):
    #se sorteaza lista de bancnote descrescator
    B.sort(reverse=True)
    k = 0# nr total bancnote (va fi minim)
    cnt = 0# cnt * val
    Sol = []
    for val in B:
        if s!=0:
            cnt = s//val
            s = s % val
            Sol.append((val, cnt))
            k += cnt
    return Sol, k

def afisare(Sol, k, s):
    with open("plata.txt", "w") as g:
        g.write(str(s) + ' = ')
        for x in range(len(Sol)-1):
            if Sol[x][1]!=0:
                g.write(str(Sol[x][0]) + ' * ' + str(Sol[x][1]) + ' + ')
        if Sol[len(Sol)-1][1]!=0:
            g.write(str(Sol[len(Sol)-1][0]) + ' * ' + str(Sol[len(Sol)-1][1]) + '\n')
        g.write("Nr minim de bancnote este: " + str(k))

l_bancnote, suma = citire("bani.txt")
print(l_bancnote, suma)
L_sol, minim = greedy(l_bancnote, suma)
print(L_sol, minim)
afisare(L_sol, minim, suma)

