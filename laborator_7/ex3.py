with open("date.in") as f:
    l = [int(x) for x in f.readline().strip().split()]

sume = []
sume.append([l[0],l[0]])

for i in range(1,len(l)):
    if sume[i-1][0] + l[i] > l[i]:
        sume.append([sume[i-1][0]+l[i]])
        sume[i].extend(sume[i-1][1:])
        sume[i].append(l[i])
    else:
        sume.append([l[i]])
        sume[i].append(l[i])
    print(sume)

Lsol = [sublista[0] for sublista in sume]
sol = max(Lsol)
print(Lsol)

with open("date.out",'w') as g:
    for sublista in sume:
        if sol == sublista[0]:
            for x in sublista[1::]:
                g.write(str(x) + " ")

