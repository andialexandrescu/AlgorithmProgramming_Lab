def citire():
    f = open("obiecte.txt")
    G = float(f.readline())
    Lobiecte = []
    crt = 1
    for line in f.readlines():
        greutate, val_castig = line.split()
        Lobiecte.append((crt, int(greutate), int(val_castig)))# o lista formata din tupluri
        crt += 1
    f.close()
    return Lobiecte, G

def keyUnitProfit(obj):
    return obj[2] / obj[1]

def greedy(Lobiecte, G):
    Lobiecte.sort(key=keyUnitProfit, reverse=True)
    n = len(Lobiecte)
    Sol = [0] * n
    spatiu_liber = G
    for i in range(n):
        if Lobiecte[i][1] <= spatiu_liber:
            spatiu_liber -= Lobiecte[i][1]
            Sol[i] = 1
        else:
            Sol[i] = spatiu_liber / Lobiecte[i][1]
            break
    profit_total = sum([Sol[i] * Lobiecte[i][2] for i in range(n)])
    return profit_total, Sol

def afisare(Sol, profit_total, Lobiecte):
    fout = open("rucsac.txt", "w")
    fout.write("Castig maxim: " + str(profit_total) + "\n")
    fout.write("\nObiectele incarcate:\n")
    i = 0
    while i < len(Lobiecte) and Sol[i] != 0:
        percentage_loaded = format(Sol[i] * 100, '.2f')
        fout.write("Obiect " + str(Lobiecte[i][0]) + ": " + percentage_loaded + "%\n")
        i += 1
    fout.close()

Lobj, greut = citire()
print(Lobj, greut, sep="\n")
Lprofit, Sol_L = greedy(Lobj, greut)
print(Lprofit, Sol_L, sep="\n")
afisare(Sol_L, Lprofit, Lobj)