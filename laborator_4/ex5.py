def negative_pozitive(lista):
    l_poz = [x for x in lista if x>0]
    l_neg = [x for x in lista if x<0]
    return l_neg, l_poz

nume = input("nume fisier=")# numere.txt
with open(nume, "r") as f:
    l_nr = [int(x) for x in f.read().split()]
    print(l_nr)
l_neg, l_poz = negative_pozitive(l_nr)

with open(nume, "a") as g:
    g.write("\n" + " ".join([str(x) for x in sorted(l_neg)]))
    g.write("\n" + " ".join([str(x) for x in sorted(l_poz)]))
