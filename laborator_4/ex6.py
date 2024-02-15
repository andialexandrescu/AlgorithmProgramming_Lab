import random
import string
#a)
def memorare_date(nume_fisier):
    f = open(nume_fisier)
    d = {}
    for linie in f:
        L = linie.split()
        d[int(L[0])] = (L[1], L[2], [int(x) for x in L[3::]])
        # nu e nevoie de a trata cazul in care cheia ar exista deja in dictionar
        # pt ca orice cnp e unic
        # cheia e cnp-ul, valoarea coresp cnp-ului e tuplul format din nume,
        # prenume si lista de note obt
    f.close()
    return d

d_elevi = memorare_date("elevi.in")
for x in d_elevi.keys():
    cnp = x
    nume, prenume, L_note = d_elevi.get(x)# despachetare tuplu atribuit ca valoare
    # a cnp-ului (care e cheia)
    print(f"cnp: {cnp}, nume: {nume}, prenume: {prenume}, note: {L_note}")
#b)
def modif_nota(d_elevi, cnp):
    if cnp in d_elevi.keys():
        d_elevi[cnp][2][0] += 1
        return d_elevi[cnp][2][0]
    else:
        return None

print(modif_nota(d_elevi, 2402900000041))
#c)
def modif_lista_note(d_elevi, cnp, lista_note):
    if cnp in d_elevi.keys():
        d_elevi[cnp][2].extend(lista_note)
        return d_elevi[cnp][2]
    else:
        return None

l_note=[10,8]
print(modif_lista_note(d_elevi, 1412900000041, l_note))
#d)
def sterge_elev(d_elevi, cnp):
    mesaj = d_elevi.pop(cnp, None)
    if mesaj is None:
        print(f"Elevul cu cnp-ul {cnp} nu exista in baza de date")

sterge_elev(d_elevi, 40000010000)
print(d_elevi)
#e) var1
def dict_to_list(d_elevi):
    lista_elevi = [[d_elevi[x][0], d_elevi[x][1], d_elevi[x][2]] for x in d_elevi.keys()]
    return lista_elevi

l_elevi = dict_to_list(d_elevi)
print(l_elevi)
def calcul_medie(l_elevi):
    medie = []
    for x in range(len(l_elevi)):
        medie_x = float(round(sum([int(n) for n in l_elevi[x][2]])/len(l_elevi[x][2]), 2))
        sublista_elev_medie = (l_elevi[x][0], medie_x)# sublista e un tuplu
        medie.append(sublista_elev_medie)
    return medie

l_medie = calcul_medie(l_elevi)# afiseaza lista de medii obtinute
print(l_medie)
l_medie_ord = sorted(l_medie, key=lambda x: (-x[1], x[0]))
print("Ordonare descrescatoare l_medie dupa medie:", *l_medie_ord)
l_elevi_ord = sorted(l_elevi, key=lambda x: (-next(y[1] for y in l_medie if y[0]==x[0]), x[0]))
# are loc o unificare y[0]==x[0]!!!
print("Ordonare descrescatoare l_elevi dupa medie:", *l_elevi_ord)

with open("elevi.out", "w") as g:
    g.write("\n".join(" ".join(str(x) for x in elev) for elev in l_elevi_ord))

#e) var2
L = [[d_elevi[i][0], d_elevi[i][1], d_elevi[i][2]] for i in d_elevi]
L = sorted(L, key=lambda x: (-sum(int(nota) for nota in x[2])/len(x[2]), x[0]))
print("Ordonare descrescatoare:", *L)

#with open("elevi.out", "w") as g:
    #g.write("\n".join(" ".join(str(x) for x in elev) for elev in L))
#f)
def genereaza_coduri(d_elevi):
    for cnp in list(d_elevi.keys()):
        cod = ("".join(random.choice(string.ascii_letters) for x in range(3))
               + str(random.randint(100,999)))
        d_elevi[cnp] += (cod,)

genereaza_coduri(d_elevi)
print(d_elevi)