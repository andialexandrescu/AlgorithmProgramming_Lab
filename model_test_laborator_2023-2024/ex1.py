#a)
def citire_subliste(nume_fisier):
    f = open(nume_fisier)
    L = []
    for linie in f.readlines():
        l = [int(x) for x in linie.split()]
        L.append(l)
    f.close()
    return L

L1 = citire_subliste("1.txt")
print(L1)
#b)
def prelucrare_lista(L):
    L_len_min = []# o lista aux formata din lungimile fiecarei
    # subliste modificate (din care s-au eliminat toate aparitiile valorii minime)
    for sublista in L:
        k = sublista.count(min(sublista))
        while k != 0:
            sublista.remove(min(sublista))
            k -= 1
        L_len_min.append(len(sublista))
    len_min = min(L_len_min)
    for x in range(len(L)):
        L[x] = L[x][:len_min:]
prelucrare_lista(L1)
print(L1)
#c)
# n elem pe o linie
M = citire_subliste("numere.in")
prelucrare_lista(M)
for linie in M:
    print(*linie)
#d)
L = citire_subliste("numere.in")
k = int(input("k="))# input: 2
m = set()# multime de valori (distincte) din L de k cifre
g = open("numere.out", "w")
for linie in L:
    for x in linie:
        if len(str(x)) == k:
            m.add(x)
aux = sorted([int(x) for x in m], reverse=True)
if len(aux) == 0:
    g.write("Imposibil!\n")
else:
    g.write(" ".join(str(x) for x in aux))
g.close()









