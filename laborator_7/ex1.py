#se ia o structura intermediara in care salvam calculele anterioare,
# insa se poate rezolva aceasta problema si recursiv

n = int(input("n="))
v = [0] * (n+1)
print(v)
v[0] = v[1] = 1 # la scarile 0 si 1 se poate ajunge intr-o modalitate
v[2] = 2 # la scara 2 se ajunge in 2 modalitati (1+1 sau 0+2)
for i in range(3, n+1):# valorile a, b sau c
    for j in range(1, 4):
        v[i] += v[i-j]
        # v[i] = v[i-1] + v[i-2] + v[i-3]
#print(v)

print(v[n])
# la pozitia n se afla rezultatul posibilitatilor
# de a sari scarile pentru a ajunge la treapta n

