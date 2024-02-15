#a)
def memorare_dict(nume_fisier):
    f = open(nume_fisier)
    d = dict()
    linii = f.readlines()
    for linie in linii:
        item = linie.split()
        spiridus = item[0]
        buc = int(item[1])
        jucarie = " ".join(item[2:])
        if spiridus not in d.keys():
            d[spiridus] = [(buc, jucarie)]
        else:
            d[spiridus].append((buc, jucarie))
    f.close()
    return d
dict_cadouri = memorare_dict("spiridus.txt")
print(dict_cadouri)
#b)
def despre_spiridus(d, cod_spiridus):
    L = []
    if cod_spiridus in d:
        for val in d[cod_spiridus]:
            L.append((val[1], val[0]))
    L.sort(key = lambda t: (-int(t[1]), t[0]))
    return L
print(despre_spiridus(dict_cadouri, "S1"))
#c)
def jucarii(d):
    m_jucarii = set()
    for x in d.values():
        for t in x:
            if t[1] not in m_jucarii:
                m_jucarii.add(t[1])
    return m_jucarii
print(jucarii(dict_cadouri))
#d)
def spiridusi(d):
    L = []
    for spiridus in d.keys():
        cantitate = 0
        for t in d[spiridus]:
            cantitate += t[0]
        L.append((spiridus, len(d[spiridus]), cantitate))
    L.sort(key = lambda t: (-t[1], -t[2], t[0]))
    return L
print(*spiridusi(dict_cadouri), sep="\n")
#e)
def actualizare(d, cod_spiridus, jucarie):
    for x in d[cod_spiridus]:
        if len(d[cod_spiridus]) >= 2 and jucarie == x[1]:
            d[cod_spiridus].pop(x.index(jucarie))
            return True
    return False
print(actualizare(dict_cadouri, "S1", "trenulet"))
print(despre_spiridus(dict_cadouri, "S1"))
