#functie folosita pentru sortarea crescătoare a persoanelor
# în raport de timpii de servire (cheia)
def cheieTimpServire(t):
    return t[1]
# funcția afișează, într-un format tabelar, timpii de servire
# și timpii de așteptare ai persoanelor
# ts = o listă cu timpii individuali de servire
def afisareTimpi(ts, nume_fisier_output):
    with open(nume_fisier_output, "w") as g:
        g.write("Persoana\tTimp de servire\tTimp de asteptare" + '\n')
        tcrt = 0# timpul de așteptare al persoanei curente
        ttotal = 0# timpul total de așteptare

        for t in ts:
            tcrt = tcrt + t[1]
            ttotal = ttotal + tcrt
            g.write(str(t[0]).center(len("Persoana")) + '\t')
            g.write(str(t[1]).center(len("Timp de serivire")) + '\t')
            g.write(str(tcrt).center(len("Timp de asteptare")) + '\n')

        g.write("Timpul mediu de asteptare:")
        g.write(str(round(ttotal/len(ts), 2)))

# timpii de servire ai persoanelor se citesc de la tastatură
# Citim timpii de servire din fișierul "tis.txt"
with open("tis.txt", "r") as f:
    aux = [int(x) for x in f.read().split()]

# asociem fiecărui timp de servire numărul de ordine al persoanei
tis = [(i+1, aux[i]) for i in range(len(aux))]
#print("Varianta inițială:")
afisareTimpi(tis, "tis_init.txt")

# sortăm persoanele în ordinea crescătoare a timpilor de servire
tis.sort(key=cheieTimpServire)
#print("\nVarianta optimă:")
afisareTimpi(tis, "tis_fin.txt")

