#1)
prop1 = input("prop = ")
L = prop1.split()
L2 = [cuv for cuv in L if len(cuv) >= 2]
prop2 = " ".join(sorted(L2, key=lambda cuv: -len(cuv)))
print(prop2)
#2)
l1 = [int(x) for x in input("l = ").split()] # 11 45 20 810 179 81 1000
l1 = sorted(l1, key=lambda n: (sum([int(c) for c in str(n)]),-n))
print(l1)
#3)
#a) citire date tastatura + memorare intr-o lista de subliste
n = int(input("n = "))
#VAR1 citire n linii
#linii = []
#for i in range(n):
    #linii += [input("linie = ")]
#VAR2 citire n linii
linii = [input("linie = ") for i in range(n)]

Lstudenti = []
for linie in linii:
    s = linie.split()
    L_student = [s[0], s[1], int(s[2]), [int(x) for x in s[3:]]]
    Lstudenti.append(L_student)
print(Lstudenti)
#b)
for s in Lstudenti:
    minim = min(s[3]) #s[3] va contine defapt intreaga sublista de note
    if minim >= 5:
        s.append("promovat")
    else:
        s.append("nepromovat")
print(Lstudenti)
#c)
L1 = sorted(Lstudenti, key=lambda s: (s[2], s[0], s[1]))
print(L1)
#d)
def sortare_medie(s):
    medie = sum(s[3])/len(s[3])
    if s[4] == "promovat":
        return -medie, s[0], s[1]
    else:
        nr_note_sub5 = 0
        for x in range(5):
            nr_note_sub5 += s[3].count(x)
        return nr_note_sub5, s[0], s[1]

L2 = sorted(Lstudenti, key=lambda s: (s[2], sortare_medie(s)))
print(*L2, sep="\n")
#4)
lnr = [1, 4, 8, 67, 44, 34, 33, 78, 99, 90, 11, 3, 6]
lnr = sorted(lnr, key=lambda x: (0, x) if x%2!=0 else (1, -x))
print(lnr)


