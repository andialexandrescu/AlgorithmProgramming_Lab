#a)
def memorare_dict(nume_fisier):
    f = open(nume_fisier)
    d = dict()
    linii = f.readlines()
    for linie in linii:
        sublista = linie.split()
        pereche = sublista[0]
        arc_st, arc_dr = pereche.split("-")
        x1, y1 = [int(x) for x in arc_st.strip("()").split(",")]
        x2, y2 = [int(x) for x in arc_dr.strip("()").split(",")]
        grosime = int(sublista[1])
        culoare = sublista[2]
        t_st = (x1, y1)
        t_dr = (x2, y2)
        t = (t_st, t_dr)
        if t not in d.keys():
            d[t] = [(grosime, culoare)]
        else:
            d[t].append((grosime, culoare))
    f.close()
    return d
d1 = memorare_dict("arce.in")
print(d1)
#b)
def modifica_arc(d, p1, p2, grosime, culoare):
    t = (p1, p2)
    if t not in d.keys():
        d[t] = [(grosime, culoare)]
    else:
        d[t].append((grosime, culoare))
    k = 0
    for arce in d.keys():
        if arce[0] == p1:
            k += len(d[arce])
    return k
k1 = modifica_arc(d1, (5,6), (7,8), 5, "verde")
print(d1, k1)
#modifica_arc(d1, (1,3), (0,0), 8, "maro-cacaniu")
#k2 = modifica_arc(d1, (1,3), (2,6), 7, "roz-bonbon")
#print(d1, k2)
#c)
def sterge_punct(d, pct):
    m = set()
    for arc in list(d.keys()):
        if pct in arc:
            d.pop(arc)
        else:
            m.add(arc)
    return m
m1 = sterge_punct(d1, (1,2))
print(d1, m1, sep="\n")
for pct in m1:
    print(f"{pct[0]}-{pct[1]}", end=" ")
    for x in d1[pct]:
        print(x[0], x[1], end=" ")
    print()


