#a)
def frecventa(*nume_fisiere):
    d = {}
    for nume in nume_fisiere:
        f = open(nume)
        L_cuv = f.read().split()# va contine continutul intregului fisier curent, ale carui cuvinte sunt elementele listei L_cuv
        for cuv in L_cuv:
            #if cuv not in d:
            #    d[cuv] = 1
            #else:
            #    d[cuv] += 1
            d[cuv] = d.get(cuv, 0) + 1# va furniza val asociata lui cuv (cheie), insa ne amintim ca
            # construim un dictionar de frecvente\ daca cheia cuv nu exista deja, se va furniza valoarea 0, la care adaugam 1
    f.close()
    return d
#b)
# cuv care apar in cel putin unul dintre fisiere (sortate lexicografic)
d12 = frecventa("cuvinte1.in", "cuvinte2.in")
print(d12)
print(sorted(d12.keys()))#d12.keys() furnizeaza o lista, de aceea e sortata folosind sorted(L, reverse=False)
print(" ".join(sorted(d12.keys())))
#c)
d1 = frecventa("cuvinte1.in")
print(d1)
print(sorted(d1.items(), key = lambda t: -t[1])) # minus in fata unui criteriu de tip numeric, minus unar
#d) VAR1
d2 = frecventa("cuvinte2.in")
print(d2)
print(sorted(d2.items(), key = lambda t: (-t[1], t[0])))# afiseaza o lista de tupluri
print(min(d2.items(), key = lambda t: (-t[1], t[0]))[0])# min[0] va afisa doar cuvantul minim al listei sortate
# dupa frecvente descrescatoare, fara a afisa si frecventa lui (maxima), adica min[1]
# d) VAR2
d3 = frecventa("cuvinte2.in")
#print(max(d3.values()))
print([(cheie, val) for cheie, val in d3.items() if val==max(d3.values())])
print(min((cheie,val) for cheie, val in d3.items() if val==max(d3.values()))[0])
#e)
s12 = sum([d1.get(cuv, 0) * d2.get(cuv, 0) for cuv in d12.keys()])
s1 = sum([frecv ** 2 for frecv in d1.values()])**0.5
s2 = sum([frecv ** 2 for frecv in d2.values()])**0.5
rez = round(s12 / (s1*s2), 2)# round - aprox cu 2 zecimale
print(rez)
