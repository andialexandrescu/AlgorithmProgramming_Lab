# reinterpretare descompunerea unui nr nat ca suma de nr nat nenule
def bkt(i):
    global G, n, k, sol

    for v in range(1, G-i+2):
        sol[i] = v
        suma_crt = sum(sol[:i+1:])
        length = len(sol[1:i+1:])
        minim_crt = min(sol[1:i+1:])
        maxim_crt = max(sol[1:i+1:])
        if suma_crt <= G and abs(maxim_crt-minim_crt)<=k:
        # modulul diferentei dintre oricare doua numere se rezuma la a calcula modulul
        # diferentei dintre val maxima curenta din solutia partiala pana la acest moment si val minima curenta
            if suma_crt == G and length == n:#and 1 in sol[1:i+1:]: subpunctul b)
                print(*sol[1:i+1], sep="+")
            else:
                bkt(i+1)

G = int(input("G = "))
n = int(input("n = "))
k = int(input("k = "))
sol = [0]*(G+1)
bkt(1)
