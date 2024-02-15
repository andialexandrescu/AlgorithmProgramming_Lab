f = open("text.in")
l_text = []
w = f.readline()
for linie in f:
    for sep in ".,:;?!":
        linie = linie.replace(sep, "")
    l_text.extend(linie.split())
f.close()
#print(l_text)
L = []

for cuv in l_text:
    for p in range(len(w) - 1, -1, -1):
        if cuv.startswith(w[:p+1]) == True and cuv not in L:
            L.append((cuv, p+1))
            break# fara acest break un cuvant ar fi inregistrat de mai
            # multe ori in cazul in care exista cel putin doua subsecvente
            # ale lui w care sa fie prefixe ale cuv din l_text
#print(L)
L.sort(key = lambda t: (-t[1], t[0]))# descresc lungime subsecv prefix, cresc nume
with open("text.out", "w") as g:
    g.writelines("\n".join([t[0] for t in L]))




