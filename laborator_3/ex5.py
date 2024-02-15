#1)
#citire matrice cu m linii, n coloane - de la tastatura: elem unei linii
# pe acelasi rand (de pe linii diferite -> randuri diferite) si separate prin spatiu
m = int(input("m="))
n = int(input("n="))
M = []
for i in range(m):
    linie = list(map(int, input().split()))
    M.append(linie)

transpusa = [[M[i][j] for i in range(m)] for j in range(n)]
#explicatie: sublistele reprezinta cate o coloana din M[i][j], din moment ce
# parcurgem intai raportat la i linii, apoi la j coloane

#afisare
for linie in transpusa:
    print(*linie)
#2)
#citire fiecare element pe un rand diferit de la tastatura
#EXEMPLU de input: m=3 n=5
#6 4 8 9 9
#7 7 1 3 2
#5 4 9 1 0
m = int(input("m="))
n = int(input("n="))
M = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        M[i][j] = int(input("elem = "))

#ordonare cresc a elem din prima coloana prin interschimbari de linii
for i1 in range(m-1):
    for i2 in range(i1+1, m):
        if M[i2][0] < M[i1][0]:
            M[i1], M[i2] = M[i2], M[i1] #atribuire compusa interschimbam toata
            # linia (vizualizeaza ca matricea e o lista de subliste)
#fiecare element e afisat pe 5 caractere
for linie in M:
    print(*[f"{elem:5}" for elem in linie])# despachetare
#3)
def triunghi_pascal(n):
    T = [[1] * (i + 1) for i in range(n)]
    # nr variabil de elemente pe fiecare linie umpluta cu 1
    # (pastram val de 1 numai din extrema stanga si dreapta, celelalte vor fi modif ulterior)
    for i in range(2, n):# nu ma ating de primele doua linii,
        # le modific pe urm n-2 linii (de la nr de ordine 2 pana la n-1)
        for j in range(1, i):
            T[i][j] = T[i-1][j-1] + T[i-1][j]
    return T

def afisare(T):
    c = 0
    for j in range(n):
        if c < len(str(T[-1][j])):# cu siguranta elementul cu cele mai multe cifre se afla pe ultimul rand
            c = len(str(T[-1][j]))# max lungimea unui numar
    for linie in T:
        for nr in linie:
            print(f"{nr:>{c+1}}", end="")
        print()

n = int(input("n="))
T_pascal = triunghi_pascal(n)
afisare(T_pascal)
#4)
def ciur_eratostene(n):
    nrprime = [True] * (n+1)# pp ca toate nr sunt prime
    nrprime[0] = nrprime[1] = False
    for x in range(2, n):
        for d in range(2, x):
            if x % d == 0:
                nrprime[x] = False
    return [x for x in range(n) if nrprime[x] == True]

n = int(input("n="))# ex: 18 -> [2, 3, 5, 7, 11, 13, 17]
L_nrprime = ciur_eratostene(n)
print(L_nrprime)
#5)
def union_and_intersection(A, B):
    i = j = 0
    I = []# intersectie
    U = []# reuniune
    # alg interclasare (de aceea e specificat ca multimile sunt ordonate crescator)
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            U.append(A[i])
            i += 1
        elif A[i] > B[j]:
            U.append(B[j])
            j += 1
        else:
            U.append(A[i])
            I.append(A[i])
            i += 1
            j += 1
    while i < len(A):
        U.append(A[i])
        i += 1
    while j < len(B):
        U.append(B[j])
        j += 1
    return U, I

A = [int(x) for x in input("A: ").split()]
B = [int(x) for x in input("B: ").split()]
Ufin, Ifin = union_and_intersection(A, B)
print("Reuniunea:", Ufin)
print("Intersectia:", Ifin)
# A = 1 4 6 11 23 35 56 101 123 203
# B = 1 2 3 6 8 11 34 56 57
