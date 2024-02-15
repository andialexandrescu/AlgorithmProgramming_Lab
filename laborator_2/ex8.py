'''Numele Pre-Nume
Scrieți un program care citește un șir de caractere și decide dacă acesta este un nume complet corect al unei persoane. Se consideră că un nume complet este corect dacă respectă următoarele proprietăți:
• persoana poate avea cel mult doua prenume, iar dacă sunt două atunci sunt despărțite printr-o cratimă (‘-’). La fel și în cazul numelui de familie
• numele de familie sau prenume conține doar litere și cel mult o cratimă.
• orice nume de familie sau prenume este format din cel puțin 3 litere.
• orice nume sau prenume începe cu literă mare.
Exemplu de nume complete corecte: Ionescu-Cherea Mihai-Adrian, Popescu Elena-Maria, Vlad Matei și de nume incorecte: Ionescu - Cherea Mihai, Vlad Matei Alexandru'''

sir = input("sir=")
nume = prenume = rez = ""
ok = False
if len(sir.split()) == 2:# partitia e formata din nume si prenume
    nume = sir.split()[0]# sir de caractere care retine o sublista
    prenume = sir.split()[1]
    #print("sublista0:", nume, "sublista1:", prenume)
    if nume.count("-") <= 1 and prenume.count("-") <= 1:# fiecare subpartitie are cel mult o cratima
        nume = nume.replace("-", " ")
        prenume = prenume.replace("-", " ")
        for cuv in nume.split():
            if cuv.isalpha() and len(cuv) >= 3:
                rez += cuv + " "
        for cuv in prenume.split():
            if cuv.isalpha() and len(cuv) >= 3:
                rez += cuv + " "
        if rez == rez.title():
            print("da, e nume complet")
            ok = True
if ok == False:
    print("nu e nume complet")
