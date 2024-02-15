#a)
def alipire(*numere):
# nr obt prin alipirea cifrelor maxime din fiecare numar
# specificat (nr variabil de parametri)
    rez = "".join([max(str(x)) for x in numere])
    return rez

print(alipire(4251, 73, 8, 133))
#b)
def binary(a, b, c):
    aux = alipire(a, b, c)
    return alipire(aux) == '1'
# va returna True pentru 1 (cifra maxima obtinuta dupa concatenarea lui a, b si c),
# altfel False pentru orice alta valoare (maximul unui secv de 0 si 1 va fi numai 1,
# altfel secventa nu e scris in binar)
print(binary(1001,11,100))
print(binary(1001,17,100))

