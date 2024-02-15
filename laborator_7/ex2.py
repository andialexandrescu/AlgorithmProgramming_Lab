# var 1 - recursiv
def f(n):
    if n == 1:
        return 0
    if n%2==0:
        return 1 + f(n // 2)
    else:
        return 1 + f(3 * n + 1)

n = int(input("n="))
print(f(n))

# var 2 - programare dinamica
def f2(d, n):
    if n == 1:
        d[1] = 0
        return d[n]
    if n % 2 == 0:
        if n // 2 not in d:
            f2(d, n // 2)
        d[n] = 1 + d[n // 2]
        return d[n]
    else:
        if 3 * n + 1 not in d:
            f2(d, 3 * n + 1)
        d[n] = 1 + d[3 * n + 1]
        return d[n]

d = dict()
n = int(input("n="))
f2(d, n)
print(d)
print(d[n])
