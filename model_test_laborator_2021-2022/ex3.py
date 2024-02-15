#a)
def cifra_control(n):
    while n >= 10:
        cif_control = 0
        while n > 0:
            cif_control += n % 10
            n //= 10
        n = cif_control
    return n
n = int(input("n="))
print(cifra_control(n))
#b)
def insereaza_cifra_control(L):
    for i in range(len(L)-1, -1, -1):
        cif = cifra_control(L[i])
        L.insert(i + 1, cif)
    return L
L1 = [345, 654, 12, 7895, 3499]
print(insereaza_cifra_control(L1))
#c)
def egale(*liste):
    lista_x = liste[0]
    for lista in liste[1::]:
        if (set(lista) != set(lista_x) or
                (set(lista) == set(lista_x) and len(lista_x) != len(lista))):
            return False
    return True
print(egale([1, 2, 3, 4, 7], [7, 3, 4, 1, 2], [2, 7, 4, 3, 1, 1, 7, 7]))# False
print(egale([1, 2, 3, 4, 7], [7, 3, 4, 1, 2], [2, 7, 4, 3, 1]))# True
#d)
f = open("numere.in")
L = [int(x) for x in f.read().split()]
insereaza_cifra_control(L)
for i in range(0, len(L), 2):
    print(L[i], L[i+1])
f.close()
#e)
ok = False
f1 = open("numere1.in")
f2 = open("numere2.in")
L_nr1 = sorted(set([int(x) for x in f1.read().split()]))
L_nr2 = sorted(set([int(x) for x in f2.read().split()]))
insereaza_cifra_control(L_nr1)
insereaza_cifra_control(L_nr2)

if len(L_nr1) == len(L_nr2):
    length = len(L_nr1)
    if egale(L_nr1[1:length:2], L_nr2[1:length:2]) == True:
        ok = True

if ok == False:
    print("Nu")
else:
    print("Da")

f1.close()
f2.close()



