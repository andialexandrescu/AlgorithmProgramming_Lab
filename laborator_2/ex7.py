'''Jurnalul electronic al Anei conține, în fiecare zi, câte o frază cu informații despre cheltuielile pe care ea le-a efectuat în ziua respectivă. Scrieți un program care să citească o frază de acest tip din jurnalul Anei și apoi să afișeze suma totală cheltuită de ea în ziua respectivă. De exemplu, pentru fraza “Astazi am cumparat paine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumparat niste cascaval. De asemenea, mi-am cumparat si niste papuci cu 50 RON!”, programul trebuie să afișeze suma totală de 80 RON. Fraza se consideră corectă, adică toate numerele care apar în ea sunt numere naturale reprezentând sume cheltuite de Ana în ziua respectivă!'''

# extragem nr si insumam
s=input("s=")
suma=0
l=s.split(" ")
for i in range(len(l)):
    if l[i].isdigit():
        suma += int(l[i])
print(suma)

