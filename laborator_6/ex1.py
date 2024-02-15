def munte(L, st, dr):
    mij = (st+dr)//2
    if len(L)<3:
        return None
    if L[mij-1]<L[mij]>L[mij+1]:
        return L[mij]
    if L[mij-1]<L[mij]: # panta ascendenta
        return munte(L, mij, dr)
    if L[mij]>L[mij+1]: # panta descendenta
        return munte(L, st, mij)

with open("date.in") as f:
    n = int(f.readline())
    L_v = [int(i) for i in f.readline().split()]

print(L_v)
vf_munte = munte(L_v, 0, len(L_v)-1)

with open("date.out", "w") as g:
    g.write(str(vf_munte))


