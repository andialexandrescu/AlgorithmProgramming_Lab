'''Într-o propoziție a fost efectuată, posibil de mai multe ori, aceeași greșeală de ortografie.
a) Scrieți un program care citește propoziția, șirul greșit și șirul corect, după care afișează propoziția corectă. De exemplu, în propoziția "Problemele cu șiruri de caracteger nu sunt ggerle!"greșeală constă în faptul că în loc de șirul “re” a fost scris șirul “ger”.
b) Modificați programul astfel încât să corecteze maxim 2 astfel de greșeli, iar dacă sunt mai multe să afișeze mesajul: “textul contine prea multe greseli, doar 2 au fost corectate”
'''
prop=input("prop=")
sirc=input("corect=")
sirg=input("gresit=")
# subpunctul a)
rez=prop.replace(sirg, sirc)
print(rez)
#print(f"In prop '{prop}', sirul de corectat este '{sirg}', fiind scris gresit '{sirc}'")
# subpunctul b)
rez2=prop.replace(sirg, sirc, 2)
print(rez2)
nr=prop.count(sirg)
if nr>2:
    print(f"au fost mai mult de doua greseli, doar doua au fost corectate")
