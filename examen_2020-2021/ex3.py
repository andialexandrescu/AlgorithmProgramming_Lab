n = int(input())
Lcuv = [cuv for cuv in input().split()]

# daca secventa care respecta proprietatea e maxima,
# atunci se va elimina un nr minim de cuvinte
Lsecv1 = [-1]*n
Lsecv2 = [-1]*n
Laparitii = [0]*n

for i in range(1, n):
    for j in range(0, i):
        max_l = len(Lcuv[j])
        if ord(Lcuv[j][max_l-1]) + 1 == ord(Lcuv[i][0]) or ord(Lcuv[j][max_l-1]) - 1 == ord(Lcuv[i][0]):
            Lsecv1[i] = j
            if Laparitii[j]>=Laparitii[i]:
                Lsecv2[i] = j
            Laparitii[i] = Laparitii[j] + 1# si Lsecv1 si Lsecv2 vor avea aceeasi lista de aparitii

# daca arat ca exista cel putin doua solutii (cu toate ca pot exista mai multe), voi afisa mesajul coresp
p = Laparitii.index(max(Laparitii))
Laux1 = []
while p != -1:
    Laux1.append(p)
    p = Lsecv1[p]
p = Laparitii.index(max(Laparitii))
Laux2 = []
while p != -1:
    Laux2.append(p)
    p = Lsecv2[p]

for poz in Laux1:# Laux2
    Lcuv.remove(Lcuv[poz])
for cuv_sters in Lcuv:
    print(cuv_sters, end=" ")
if Laux1 != Laux2:
    print("\nSolutia nu e unica")

