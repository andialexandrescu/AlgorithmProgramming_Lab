def citire(nume_fisier):# citim datele de intrare din fișierul text "spectacole.txt"
    f = open(nume_fisier)
    lsp = [] # lsp = lista spectacolelor, fiecare spectacol fiind memorat
    # sub forma unui tuplu (ID, ora de început, ora de sfârșit)
    for linie in f:
        spectacol = linie.split(" ")
        aux = spectacol[0].split("-")
        nume = " ".join(spectacol[1::])
        # aux[0] = ora de început a spectacolului curent
        # aux[1] = ora de sfârșit a spectacolului curent
        lsp.append((nume, aux[0].strip(), aux[1].strip()))
    f.close()
    return lsp

def greedy(lsp):
    lsp.sort(key=lambda sp: sp[2])# sortăm spectacolele în ordinea crescătoare a timpilor de sfârșit
    # sol = o listă care conține o programare optimă a spectacolelor,
    # inițializată cu primul spectacol
    sol = [lsp[0]]
    # parcurgem restul spectacolelor
    for sp in lsp[1:]:
        # dacă spectacolul curent începe după ultimul spectacol
        # programat, atunci îl programăm și pe el
        if sp[1] >= sol[-1][2]:
            sol.append(sp)
    return sol

def afisare(sol):
    # scriem datele de ieșire în fișierul text "programare.txt"
    g = open("programare.txt", "w")
    g.write("Numarul maxim de spectacole: " + str(len(sol)) + "\n")
    g.write("Spectacolele programate:\n")
    for sp in sol:
        g.write(sp[1] + "-" + sp[2] + " " + sp[0])
    g.close()

L_spectacole = citire("spectacole.txt")
Sol_spectacole = greedy(L_spectacole)
afisare(Sol_spectacole)



