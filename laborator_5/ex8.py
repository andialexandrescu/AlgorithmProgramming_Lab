def citire():
    fin = open("proiecte.txt")
    # lp = lista proiectelor în care un proiect este memorat
    # sub forma unui tuplu (denumire, termen limită, profit)
    Lproiecte = []
    for linie in fin:
        denumire, t_limita, profit = linie.split()
        Lproiecte.append((denumire, int(t_limita), float(profit)))
    fin.close()
    return Lproiecte
def cheieProfit(t):
    return -t[2] # desc profit
def greedy(Lproiecte):
    Lproiecte.sort(key=cheieProfit)
    # calculăm numărul maxim de zile în care putem să planificăm proiectele
    zi_max = max([t[1] for t in Lproiecte])
    # Planificarea optimă va fi construită folosind un dicționar cu intrări de forma zi: proiect
    Sol_planificare = {k: None for k in range(1, zi_max+1)}
    # Profit = profitul total al echipei
    profit = 0
    # Parcurgem lista proiectelor și încercăm să planificăm
    # fiecare proiect într-o zi cât mai apropiată de termenul său limită
    for proiect in Lproiecte:
        for z in range(proiect[1], 0, -1): # zi apropiata de termen limita
            if Sol_planificare[z] is None:
                Sol_planificare[z] = proiect
                profit += proiect[2]
                break
    return Sol_planificare, profit
def afisare(Sol_planificare, profit):
    fout = open("profit.txt", "w")
    for z in Sol_planificare:
        if Sol_planificare[z] is not None:
            fout.write("Ziua " + str(z) + ": " + Sol_planificare[z][0] +
                       " " + str(Sol_planificare[z][2]) + "\n")
    fout.write("\nProfit maxim: " + str(profit))
    fout.close()

Lp = citire()
print(Lp)
Sol_L, profit_total = greedy(Lp)
afisare(Sol_L, profit_total)
