def citire():
    f=open("evenimente.txt")
    Lspectacole=[]
    for linie in f.readlines():
        interval,nume=linie.split()
        ora_inceput,ora_sfarsit=interval.split("-")
        Lspectacole.append((ora_inceput,ora_sfarsit,nume))
    f.close()
    return Lspectacole

def greedy(Lspectacole): # ineficient, var eficienta care fol queue e in cursul 10
    Lspectacole.sort(key = lambda t: t[0])
    crt = 1 # nr de ordin al salii in care va fi programat un spectacol
    Sol = {crt: [Lspectacole[0]]} # programare primul specatcol in prima sala, mereu va exista o solutie
    # spcrt = spectacol curent, care de fapt e un tuplu
    for spcrt in Lspectacole[1::]: # nu mai verificam si primul spectacol
        for sala in Sol.values(): # sala e o lista form din mai multe tupluri ce reprez spectacolele
            if spcrt[0] >= sala[-1][1]: # timpul de inceput al spectacolului curent e mai mare decat finalul ultimului spectacol planificat in sala
                sala.append(spcrt)
                break
        else: # daca for-ul se termina "natural" inseamna ca trebuie sa adaugam un nou elem in dictionar
            crt += 1
            Sol[crt] = [spcrt]
    minim = list(Sol.keys())[-1] # ultima cheie indica nr minim de sali folosite
    return minim, Sol

def afisare(Sol, minim):
    with open("sali.txt", "w") as g:
        g.write(f"Numar minim de sali: {minim}" + "\n")
        for cheie in Sol.keys():
            g.write("\n" + f"Sala {cheie}:" + "\n")
            for sala in Sol[cheie][:len(Sol[cheie])-1:]:
                 g.write("(" + "-".join(sala[0:2:]) + f" {sala[2]}" + "),")
            sala = Sol[cheie][len(Sol[cheie])-1]
            g.write("(" + "-".join(sala[0:2:]) + f" {sala[2]}" + ")" + "\n")

L = citire()
print(L)

minim_sali, Sol_L = greedy(L)
print(minim_sali, Sol_L, sep="\n")

afisare(Sol_L, minim_sali)

