def k_biti(n):
    k = 0
    while n:
        k += n & 1
        n >>= 1
    return k
f = open("numere.in")
dict_nr = dict()
linii = f.readlines()
for linie in linii:
    sublista = [int(x) for x in linie.split()]
    for x in sublista:
        k = k_biti(x)
        if k not in dict_nr.keys():
            dict_nr[k] = [x]
        elif k in dict_nr.keys() and x not in dict_nr[k]:
            dict_nr[k].append(x)
f.close()
#print(dict_nr)
def cheieSortare(t):
    t[1].sort()
    return (-len(t[1]), -t[0])
L = sorted(dict_nr.items(), key = cheieSortare)
#print(L)
with open("numere.out", "w") as g:
    for t in L:
        numere_string = [str(x) for x in t[1]]
        g.write(f"{t[0]} biti nenuli: {','.join(numere_string)}\n")


