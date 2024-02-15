def cautare_cuvant_fisiere(cuv, nume_fisier_out, *nume_fisiere_in):
    g = open(nume_fisier_out, "w")
    for fisier in nume_fisiere_in:
        g.write(fisier + ' ')
        f = open(fisier, "r")
        l_linii = f.readlines()
        for linie in l_linii:
            if cuv in linie or cuv.capitalize() in linie:
                g.write(str(l_linii.index(linie)+1) + ' ')
        g.write('\n')
        f.close()
    g.close()

cautare_cuvant_fisiere("floare", "rez.txt", "eminescu.txt", "paunescu.txt")

