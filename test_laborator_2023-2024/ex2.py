#a)
f = open("melodii.in")
d = {}
linii = f.readlines()
for linie in linii:
    if ">>" in linie:
        l1 = linie.split(">>")
        gen = l1[1].strip()
    else:
        sublista = linie.split("/")
        melodie = sublista[0].strip()
        artist = sublista[1].strip()
        durata = sublista[2].strip()
        if gen not in d:
            d[gen] = [(melodie, artist, durata)]
        else:
            d[gen].append((melodie, artist, durata))
print(d)
f.close()
#b)
def playlist(d, *genuri, durata_minima = "02:00", durata_maxima = "03:30"):
    L = []
    for gen in genuri:
        for t in d[gen]:
            #hh_min, mm_min = durata_minima.split(":")
            #hh_max, mm_max = durata_maxima.split(":")
            #hh, mm = t[2].split(":")
            if durata_minima <= t[2] <= durata_maxima:
                L.append((gen, t[0], t[1], t[2]))
    return L
L1 = playlist(d,"Rock", "Hip-hop", durata_minima = "02:20", durata_maxima = "03:30")
L1.sort(key = lambda t: (-int(t[3].split(":")[0] * 60 + t[3].split(":")[1]), t[2], t[1]))# (desc durata, cresc artist, cresc titlu)
for t in L1:
    print(t)
#c)
def adauga_melodie(d, gen, titlu, artist, durata):
    if gen in d.keys():
        d[gen].append((titlu, artist, durata))
        mesaj = "Genul {gen_muz} contine acum {nr} melodii"
        mesaj = mesaj.format(gen_muz=gen, nr=len(d[gen]))
        return mesaj
    else:
        mesaj = "Nu exista acest gen muzical"
        return mesaj

g = str(input("genul: "))
t = str(input("titlu: "))
a = str(input("artist: "))
dur = str(input("durata: "))
print(adauga_melodie(d, g, t, a, dur))