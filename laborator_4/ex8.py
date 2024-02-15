#a)
def liste_x_a(x, *liste, nr=0):
    for L in liste:
        if x in L:
            nr += 1
    return nr

nr = liste_x_a(3, [1, 5, 7], [3], [1, 8, 3], [4, 3, 3], [])
print(nr)
#b)
def liste_x_b(x, *liste):
    global rez
    for L in liste:
        if x in L:
            rez += 1

rez = 0
liste_x_b(3, [1, 5, 7], [3], [1, 8, 3], [4, 3, 3])
print(rez)

