# 3 -2 5 -1 4
# 7 8 -5 2 -4 -1 5
def greedy():
    global A, B, m, n
    A.sort(reverse = True)
    B.sort(reverse = True)
    copie_n = n

    Lsol = [(A[0], B[0])]
    suma_max = A[0] * B[0]
    for i in range(1, m):
        if A[i] > 0 and B[i] > 0:
            suma_max += A[i] * B[i]
            Lsol.append((A[i], B[i]))
        else:
            p = m - i
            suma_max += A[i] * B[copie_n - p]
            Lsol.append((A[i], B[copie_n - p]))
    return Lsol, suma_max

A = [float(x) for x in input("A: ").strip().split()]
B = [float(x) for x in input("B: ").strip().split()]
m = len(A)
n = len(B)
print(greedy())

