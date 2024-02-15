#a)
def citire_lista():
    n = int(input("n="))
    L = []
    for i in range(n):
        L.append(int(input(f"elementul{i+1}: ")))
    return L
#b)
def functie(s, x, i=0, j=None):
    if j is None:
        j = len(s)
    for poz in range(i, j):
        if s[poz] > x:
            return poz
    return -1

L = citire_lista()
n = len(L)
print(L)
#c)
ok = True
for i in range(n - 1):
    if functie(L, L[i], i+1) != -1:
    # L[i+1]>L[i] unde s[poz]==L[i+1] si x==L[i]; daca e sortata crescator
        ok = False
if ok == True:
    print("Da, e sortata descrescator")# [9, 5, 4, 2, 2]
else:
    print("Nu, nu e sortata descrescator")# [7, 5, 1, 5, 3]
