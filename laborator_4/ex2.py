
def p_rimeaza(nume_fisier):
    f = open(nume_fisier)
    l = f.read().split()
    p = int(input("p = "))
    sufixe = []# lista tuturor sufixelor posibile de p litere
    lfin = []
    for cuv in l:
        if cuv[-1:-p-1:-1][::-1] not in sufixe:# cuv[-1:-p-1:-1] va intoarce ultimele p litere citite
            # de la dreapta la stanga, de aceea e nevoie de o inversare in plus
            sufixe.append(cuv[-1:-p-1:-1][::-1])
    for i in range(len(sufixe)):# se parcurge pe baza sufixelor deoarece construim tuplurile in
        # functie de sufixe (cuv grupate dupa sufixe identice)
        t = tuple()
        for cuv in l:
            if cuv.endswith(sufixe[i]):
                t += (cuv,)
        t = tuple(sorted(t, reverse=True))# sortam cuv din tuplu inainte de a sorta subtuplurile
        # din lista (subtupluri intr-o lista = lista form din tupluri; "sub" - evitare impas mintal
        # pt a intelege prioritatea)
        lfin.append(t)

    lfin_sortat = sorted(lfin, key = lambda t: -len(t))# ordine descrescatoare a lungimii fiecarui tuplu
    f.close()
    return lfin_sortat

def afisare(L_p):
    g = open("rime.txt", "w")
    L_afisare = []
    for t in L_p:
        L_afisare.append(" ".join(str(x) for x in t))# linie din fisierul de iesire
    g.writelines("\n".join(L_afisare))
    g.close()

nume_fisier = input("Numele fisierului din care se citesc cuv: ")# intrare_rime.txt
L_p = p_rimeaza(nume_fisier)
afisare(L_p)

