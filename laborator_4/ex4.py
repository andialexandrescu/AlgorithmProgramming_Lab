import random
import string
def creare_email(nume_fisier):
    f = open(nume_fisier)
    L = []
    L_email = []
    for linie in f:
        x = linie.split()
        L.append(x)
    f_email = "{prenume}.{nume}@s.unibuc.ro"
    for x in L:
        L_email.append(f_email.format(prenume=x[1].lower(), nume=x[0].lower()))
    f.close()
    return L_email

def creare_parola(L_stu):
    L_fin = []# email + parole
    for i in range(len(L_stu)):
        parola = (random.choice(string.ascii_uppercase) +
        "".join(random.choice(string.ascii_lowercase) for x in range(3)) +str(random.randint(1000,9999)))
        L_fin.append([L_stu[i], parola])
    return L_fin

def afisare(L_credentials):
    g = open("date.out", "w")
    for stu in L_credentials:
        g.write(", ".join(stu) + "\n")
    g.close()

L_stu = creare_email("date.in")
L_credentials = creare_parola(L_stu)
afisare(L_credentials)
