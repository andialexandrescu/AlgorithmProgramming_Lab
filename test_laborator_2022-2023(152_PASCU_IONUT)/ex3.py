#a)
def citire_date(nume_fisier):
    global cheie
    f = open(nume_fisier)
    cheie = f.readline()
    d = dict()
    for linie in f.readlines():
        sublista = [str(x) for x in linie.split()]
        nume = sublista[0]
        cuv_cript = sublista[1]
        ora = sublista[2]
        if nume not in d:
            d[nume] = [(cuv_cript, ora)]
        else:
            d[nume].append((cuv_cript, ora))
    f.close()
    return d
cheie = ""
dict_mesaje = citire_date("comunicare.in")
print(dict_mesaje)
#b)
def decodificare(cuv, cheie_criptare):
    #l_alpha = [chr(97+x) for x in range(26)]
    d = {cheie_criptare[x] : chr(97+x)  for x in range(26)}
    l_aux = []
    for lit in cuv:
        if lit != "-":
            l_aux.append(d[lit])
        else:
            l_aux.append("-")
    cuv_decript = "".join(l_aux)
    return cuv_decript
#cuv1 = decodificare("odtoyi", "obcgsefhizjklmnpqrdtuvawxy")
#print(cuv1)
#c)
L_fin = []
for nume in dict_mesaje.keys():
    l_prop = []
    l_ore = []
    for t in dict_mesaje[nume]:
        l_ore.append(t[1])
    ora_inceput = min(l_ore)
    #print(l_ore, ora_inceput)
    lista = sorted(dict_mesaje[nume], key = lambda t: t[1])
    for t in lista:
        l_prop.append(t[0])
    for i in range(len(l_prop)):
        l_prop[i] = decodificare(l_prop[i], cheie)
    prop = " ".join(l_prop)
    L_fin.append((nume, prop, ora_inceput))
L_fin.sort(key = lambda t: t[2])# sortare dupa cine a inceput conversatia primul
with open("comunicare.out", "w") as g:
    for i in range(len(L_fin)):
        g.write(L_fin[i][0] + " : " + L_fin[i][1] + "\n")

