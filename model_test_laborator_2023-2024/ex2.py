#a)
f = open("cinema.in")
d = dict()
for linie in f.readlines():
    sublista = [elem for elem in linie.split("%")]
    cinema, film = sublista[:2:]
    cinema = cinema.strip()
    film = film.strip()
    ore = set(sublista[2].split())# la b) se cere o multime de ore
    if cinema not in d:
        d[cinema] = [(film, ore)]# tuplu
    else:
        d[cinema].append((film, ore))# tupluri diferite = filme diferite la ac cinema
f.close()
print(d)
#b)
def sterge_ore(d, cinema, film, ore):
    l_filme_modif = []
    if cinema in d.keys():
        for t in d[cinema]:
            if t[0] == film:
                for h in ore:
                    t[1].remove(h)
            if len(t[1])==0:
                d[cinema].remove(t)
            else:
                l_filme_modif.append(t)
    print(l_filme_modif)
c = input("Cinema: ")
f = input("Film: ")
o = input("Ore: ")
sterge_ore(d, c, f, {o})
#sterge_ore(d, "Cinema 1", "Buna dimineata", {"09:30"})
#sterge_ore(d, "Cinema 4", "Minionii 2", {"16:00", "20:30"})
print(d)
#c)
def cinema_film(d, ora_minima, ora_maxima, *nume_cinematografe):
    l = []
    for cinema in nume_cinematografe:
        for t in d[cinema]:
            lista_de_ore = []
            for x in t[1]:
                if ora_minima <= x <= ora_maxima:
                    lista_de_ore.append(x)
            lista_de_ore.sort()
            if len(lista_de_ore) != 0:
                l.append((t[0], cinema, lista_de_ore))
    return l
l1 = cinema_film(d, "14:00", "22:00", "Cinema 1", "Cinema 2")
def cheieSortare(t):
    return (t[0], -len(t[2]))# cresc dupa nume film, descresc nr elem lista_de_ore
l1.sort(key = cheieSortare)
print(l1)


