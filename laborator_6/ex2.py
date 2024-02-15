# nu facem interclasarea - ar fi o complexitate O(2n) - fiecare vector are lungimea n
# pastram mereu secv in care nu cunoastem inegalitatea intre cei doi vectori - O(logn)
# v1: 1 12 15 16 38 - 15 mij
# v2: 2 13 17 30 45 - 17 mij
# v1: 15 16 17 - 16 mij
# v2: 2 13 17 - 13 mij
# v1: 15 16
# v2: 13 17...
def mediana(L1, L2, st1, dr1, st2, dr2):
    #print(L1[st1:dr1 + 1:], L2[st2:dr2 + 1:], sep="\n")
    if dr1 == st1+1: # daca s-a terminat prelucrarea elementelor/
        # etapa de divide a celor doua liste, le vom interclasa
        Laux = sorted(L1[st1:dr1+1:] + L2[st2:dr2+1:])
        # lista rezultata prin interclasare va avea lungime 3 sau 4
        #print("Laux: ", Laux)
        n = len(Laux)
        if n % 2 == 0:
            #print(f"(Laux[n // 2 - 1]:{Laux[n // 2 - 1]} + Laux[n // 2]:{Laux[n // 2]}) // 2")
            return (Laux[n // 2 - 1] + Laux[n // 2]) // 2
        else:
            #print(f"Laux[n // 2]: {Laux[n // 2]}")
            return Laux[n // 2]
    poz_mij1 = (st1+dr1)//2
    #print(f"mij_L1: {poz_mij1}")
    poz_mij2 = (st2+dr2)//2
    #print(f"mij_L2: {poz_mij2}")
    if L1[poz_mij1]==L2[poz_mij2]:
        #print(f"L1[poz_mij1]: {L1[poz_mij1]}")
        return L1[poz_mij1]
    if L1[poz_mij1]<L2[poz_mij2]:
        #print("mediana(L1(mij,dr), L2(st,mij))")
        return mediana(L1,L2,poz_mij1,dr1,st2,poz_mij2)
    if L1[poz_mij1]>L2[poz_mij2]:
        #print("mediana(L1(st,mij), L2(mij,dr))")
        return mediana(L1,L2,st1,poz_mij1,poz_mij2,dr2)

L1 = [1, 12, 15, 16, 38, 66, 67, 89]
L2 = [1, 13, 20, 30, 45]
print(mediana(L1, L2,0, len(L1)-1,0, len(L2)-1))
