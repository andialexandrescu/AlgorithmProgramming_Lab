#a)
def numere(*nr):
    d = dict()
    for x in nr:
        suma_cif = 0# suma curenta
        k = 0# nr cifre
        copie_x = x
        while copie_x != 0:
            suma_cif += copie_x % 10
            copie_x //= 10
            k += 1
        medie = round(suma_cif / k, 1)# o zecimala
        if medie not in d.keys():
            d[medie] = [x]
        else:
            d[medie].append(x)
    for cheie in d.keys():
        d[cheie].sort(reverse = True)
    return d

print(numere(82375, 201, 51, 73, 3456, 2855, 1021, 90, 153))

#b)
L = [int(x) for x in range(100,1000) if str(x) == "".join(sorted(str(x)))]
print(L)
