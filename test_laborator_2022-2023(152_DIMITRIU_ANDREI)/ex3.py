#a)
def memorare_date(nume_fisier):
    f = open(nume_fisier)
    d = dict()
    linii = f.readlines()
    for linie in linii:
        sublista = linie.split("-")
        oras_st = sublista[0].strip()
        for i in range(len(sublista[1])):
            if sublista[1][i].isdigit() == True:
                poz = i
                break
        oras_dr = sublista[1][:poz:]
        oras_dr = oras_dr.strip()
        l_aux = [int(x) for x in sublista[1][poz::].split()]
        distanta = l_aux[0]
        stare_drum = l_aux[1]
        #print(oras_st, oras_dr, distanta, stare_drum)
        orase_cheie = (oras_st, oras_dr)
        if orase_cheie not in d.keys():
            d[orase_cheie] = [distanta, stare_drum]
        else:
            d[orase_cheie].append(distanta, stare_drum)
    f.close()
    return d
dict_traseu = memorare_date("drumuri.in")
print(dict_traseu)
#b)
def modifica_stare(d, s, o1, o2=""):
    k = 0
    if o2 != "":
        t = (o1, o2)
        if t in d.keys():
            d[t].pop()# stim ca starea drumului e pe ultima pozitie
            d[t].insert(1, s)
    else:
        for t in d.keys():
            if o1 == t[0]:
                d[t].pop()
                d[t].insert(1, s)
                k += 1
        return k
#modifica_stare(dict_traseu, 9, "Capitala", "Pol")
#print(dict_traseu)
#modifica_stare(dict_traseu, 4, "Satul Mare")
#print(dict_traseu)
#c)
def accesibil(d, *orase):
    m = set()
    for oras in orase:
        for traseu in d.keys():
            if oras == traseu[0]:
                m.add(traseu[1])
    return m
print(accesibil(dict_traseu, "Oraselul Mic", "Capitala"))