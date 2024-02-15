def citire():
    f = open("intervale.txt")
    Lintervale = []
    for linie in f:
        aux = linie.split()
        Lintervale.append((int(aux[0]), int(aux[1])))
    f.close()
    return Lintervale
def greedy(Lintervale):
    Lintervale.sort(key = lambda t: t[1]) # cheie extremitatea dreapta
    # lista Sol va conține extremitatea dreaptă a intervalelor
    Sol = [Lintervale[0][1]]
    # parcurgem intervalele și construim lista M
    for interval_crt in Lintervale[1:]:
        if interval_crt[0] > Sol[-1]:
            Sol.append(interval_crt[1])
    return Sol
def afisare(Sol):
    g = open("acoperire.txt", "w")
    g.write("\n".join(map(str, Sol)))
    g.close()

L = citire()
Sol_L = greedy(L)
afisare(Sol_L)
