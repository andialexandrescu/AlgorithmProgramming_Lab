#a)
def min_max(L):
    return min(L), max(L)
print(min_max([3, -3, 1, 7, 3, 2]))
#b)
def incarca_fisier(nume_fisier):
    f = open(nume_fisier)
    L = []
    for linie in f.readlines():
        L.append([int(x) for x in linie.split()])
    f.close()
    return L
l1 = incarca_fisier("in.txt")
print(l1)
#c) am fol incarca_fisier
nume_fis = input("nume fisier: ")# in.txt
poz = []
for sublista in l1:
    k = 0
    x = sublista[0]
    for y in sublista[1::]:
        if x == y:
            k += 1
    if k + 1 == len(sublista) or len(sublista) == 1:
        poz.append(l1.index(sublista))

with open("egale.txt", "w") as g:
    if len(poz) != 0:
        g.write(" ".join(str(x) for x in poz))
    else:
        g.write("Nu exista!")
#d) am fol min_max
l_min = []
l_max = []
for sublista in l1:
    min_curent, max_curent = min_max(sublista)
    l_min.append(min_curent)
    l_max.append(max_curent)
print(min(l_min), max(l_max))

