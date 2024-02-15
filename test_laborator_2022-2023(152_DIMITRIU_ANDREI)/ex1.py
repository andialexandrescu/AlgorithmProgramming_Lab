f = open("teatru.in")
dict_piesa = dict()
m_cuv = set()
linii = f.readlines()
for linie in linii:
    sublista = linie.split(":")
    personaj = sublista[0]
    replica = sublista[1].strip()
    for sep in ";,.?!":
        replica = replica.replace(sep, "")
    l_cuv = [x.lower() for x in replica.split()]
    for cuv in l_cuv:
        if cuv not in dict_piesa.keys():
            dict_piesa[cuv] = [personaj]
        elif personaj not in dict_piesa[cuv]:
            dict_piesa[cuv].append(personaj)
f.close()
#print(dict_piesa)
l_aux = []
for cuv in dict_piesa.keys():
    l_aux.append((cuv, dict_piesa[cuv]))
l_aux.sort(key = lambda t: (-len(t[1]), t[0]))
print(l_aux)
with open("teatru.out", "w") as g:
    for t in l_aux:
        g.write(t[0] + ": ")
        for x in t[1]:
            g.write(x + " ")
        g.write("\n")

