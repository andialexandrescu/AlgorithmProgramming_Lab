#a)
def deviruseaza(prop_virusata):
    l_cuv_init = []
    l_cuv = prop_virusata.split()
    if len(l_cuv) % 2 == 0:
        stop = len(l_cuv)//2
    else:
        stop = len(l_cuv)//2 + 1
    for i in range(stop):
        l_cuv[i], l_cuv[len(l_cuv)-1-i] = l_cuv[len(l_cuv)-1-i], l_cuv[i]
    for cuv in l_cuv:
        if len(cuv) > 1:
            cuv = cuv[len(cuv)-1] + cuv[1:len(cuv)-1:] + cuv[0]
        l_cuv_init.append(cuv)
    prop_init = " ".join(l_cuv_init)
    return prop_init
print(deviruseaza("aorectc aropozitip este aceasta"))
#b)
def prime(n, numar_maxim=0):
    l_prime = []
    for x in range(2, n):
        ok = True
        for div in range(2, x):
            if x % div == 0:
                ok = False
        if ok == True:
            l_prime.append(x)
    if numar_maxim == 0:
        return l_prime
    else:
        return l_prime[:numar_maxim:]
n = int(input("n="))
print(prime(n))
#c)
f = open("intrare.in")
g = open("intrare_devirusata.out", "w")
l_linii = [str(x).strip("\n") for x in f.readlines()]
#print(l_linii)
l_nr_prime = prime(len(l_linii)+1)
#print(l_nr_prime)
for prop in l_linii:
    if l_linii.index(prop)+1 in l_nr_prime:
        g.write(str(deviruseaza(prop)))
    else:
        g.write(str(prop))
    g.write("\n")
f.close()
g.close()
