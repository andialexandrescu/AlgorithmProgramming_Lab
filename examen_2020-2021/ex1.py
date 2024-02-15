# a)
def litere(*cuvinte):
    d = dict()
    for cuv in cuvinte:
        dcuv = dict()
        copie_cuv = "".join(sorted(list(cuv)))# pas optional
        for l in copie_cuv:
            if l not in dcuv:
                dcuv[l] = 1
            else:
                dcuv[l] += 1
        if cuv not in d:
            d[cuv] = dcuv
    return d

print(litere("teste", "programare"))

#b)
numere = [int(x) for x in range(10, 100) if x % 2 == 0 and x % 6 != 0]
print(numere)
