# var ineficienta in care nu fol queue
def citire():
    with open("lungimi.txt") as f:
        Lvectori = []
        for linie in f.readlines():
            denumire_crt, lungime = linie.split()
            crt = int(denumire_crt[1::])
            Lvectori.append((crt, int(lungime)))
        return Lvectori
def greedy_afisare_pasi(Lvectori):
    with open("interclasare.txt", 'w') as g:
        Lvectori.sort(key=lambda x: x[1]) # cresc lungime
        pas_crt = 1
        crt = len(Lvectori) + 1
        Solinterclasari = [] # lista formata numai din interclasarile obtinute
        Valdeplasari = []
        while len(Lvectori) > 1: # cat timp exista cel putin doi vectori care trebuie interclasati
            # (lungimea lui Lvectori se modifica treptat)
            g.write(f"Pas: {pas_crt}\n")
            Lvectori.sort(key=lambda x: x[1])
            g.write("Structura contine: ")
            for t in Lvectori[:len(Lvectori)-1:]:
                g.write(str(t) + ",")
            g.write(str(Lvectori[len(Lvectori)-1]) + ".\n")
            v1 = Lvectori.pop(0) # vor fi scosi din Lvectori perechea formata din primii doi vectori care au lungimile minime
            v2 = Lvectori.pop(0)
            lungime_aux = v1[1] + v2[1]
            nume_aux = crt # se vor crea noi vectori ca rezultat al interclasarii, deci vor avea alte numere de ordine decat cele deja existente
            v_interclasat = (nume_aux, lungime_aux)
            g.write(f"Din vectorii {v1} si {v2} rezulta {v_interclasat}.\n\n") # if len(Lvectori) >= 0:
            crt += 1
            pas_crt += 1
            Solinterclasari.append(v_interclasat)
            Lvectori.append(v_interclasat)
            Valdeplasari.append(lungime_aux)
        g.write(f"Pas: {pas_crt}\n" + "Structura contine: " + str(Lvectori[0]) + ".\n\n")
        g.write("Numar total de deplasari: ")
        for t in Valdeplasari[:len(Valdeplasari)-1:]:
            g.write(str(t) + " + ")
        g.write(str(Valdeplasari[len(Valdeplasari)-1]) + " = " + str(sum(Valdeplasari)))

L_v = citire()
print(L_v)
greedy_afisare_pasi(L_v)
