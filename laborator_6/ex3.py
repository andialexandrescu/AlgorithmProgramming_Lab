def completare(M, i, j, d):
    # subprogramul va modifica tabloul numai daca d == 1
    global k
    if d == 1: # dimensiune minima, s-a terminat etapa de divide,
        # deci se vor completa valorile nule diun matrice
        #print(f"M[{i}][{j}] = {k}")
        M[i][j] = k
        k += 1
    else: # dupa ce se completeaza cate un element cand e indeplinita conditia,
        # se revine la adresa de intoarcere pt a continua sa parcurga urmatoarele linii de program
        #print("|", end="")
        # ordinea apelurilor este generalizata pt a completa
        # M[0][1] --> M[1][0] --> M[0][0] --> M[1][1]
        #print(f"completare(M[{i}][{j + d // 2}], d = {d // 2})", end="\t")
        completare(M, i, j + d // 2, d // 2)
        #print(f"completare(M[{i + d // 2}][{j}], d = {d // 2})", end="\t")
        completare(M, i + d // 2, j, d // 2)
        #print(f"completare(M[{i}][{j}], d = {d // 2})", end="\t")
        completare(M, i, j, d // 2)
        #print(f"completare(M[{i + d // 2}][{j + d // 2}], d = {d // 2})", end="\t")
        completare(M, i + d // 2, j + d // 2, d // 2)

n = int(input("n = "))
M = [[0] * (2**n) for i in range(2**n)]
k = 1 # contorul care va fi incrementat pt fiecare element din matrice
completare(M, 0, 0, 2**n)
# matricea e de dimensiune n*n
max_len = 0
for linie in M:
    aux = [len(str(x)) for x in linie]
    if max_len < max(aux):
        max_len = max(aux)
for linie in M:
    for x in linie:
        print(str(x).rjust(max_len), end=" ")
    print()
