def citire():
    f = open("intervale.txt")
    Lintervale = []
    for linie in f:
        aux = linie.split()
        Lintervale.append((int(aux[0]), int(aux[1])))
        # (min_interval, max_interval)
    f.close()
    return Lintervale
def greedy(Lintervale):
    Lintervale.sort(key = lambda x: (x[0],-x[1])) # cresc capete st, desc capete dreapta
    extrema_stg = Lintervale[0][0]
    extrema_dr = Lintervale[0][1]
    Sol = [[extrema_stg, extrema_dr]]
    for interval_crt in Lintervale:
        if interval_crt[0]<=extrema_dr and interval_crt[1] <= extrema_dr:
            continue # daca intervalul curent e inclus in ultimul din multimea solutiilor,
            # inseamna ca face parte din reuniunea curenta
        if interval_crt[0] <= extrema_dr and interval_crt[1] >= extrema_dr: # nu e interval disjunct
            # cazul in care extrema dreapta e inafara reuniunii stabilite anterior,
            # deci se va actualiza extrema dreapta a solutiei de reuninuni, dar si extrema_dr
            Sol[-1][1] = interval_crt[1]
            extrema_dr = interval_crt[1]
        else: # intervale disjuncte, deci intervalul curent se va adauga la multimea de solutii
            extrema_stg = interval_crt[0]
            extrema_dr = interval_crt[1]
            Sol.append([extrema_stg,extrema_dr])
    return Sol

def afisare(Sol):
    lungime_totala = 0
    with open("reuniune.txt",'w') as g:
        g.write("Reuniunea intervalelor:\n")
        for i in Sol:
            lungime_totala += i[1] - i[0]
            g.write(f"{str(i)}\n")

        g.write(f"\nLungimea reuniunii: {lungime_totala}")

L = citire()
Sol_L = greedy(L)
afisare(Sol_L)