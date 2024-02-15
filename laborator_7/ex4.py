with open("sir.in") as f:
    Lcuv = f.readline().strip().split()
print(Lcuv)

Lpoz = [-1] * len(Lcuv)
Laparitii = [1] * len(Lcuv)

for i in range(1,len(Lcuv)):
    #print(f"i: {Lcuv[i][:2:]}")
    for j in range(i):# 0 <= j <= i-1
        #print(f"\tj: {Lcuv[j][-2::]}")
        if Lcuv[j][-2::] == Lcuv[i][:2:]:
            Lpoz[i] = j
            Laparitii[i] = Laparitii[j] + 1
            #print(f"\tLpoz: {Lpoz}, Lsecv: {Laparitii}")

p = Laparitii.index(max(Laparitii))# indicele ultimului cuvant din subsirul maxim
Laux = []
while p != -1:
    Laux.append(p)# va avea cuvintele de la sfarsit la inceput scrise
    p = Lpoz[p]
#print(Laux)

g = open("sir.out", "w")
for poz_cuv in Laux[::-1]:
    g.write(str(Lcuv[poz_cuv]) + "\n")
g.close()



