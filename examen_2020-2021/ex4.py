def bkt(k):
    global nrf, nrb, sol, k_fete, k_baieti, len_crt
    n = nrf + nrb
    for v in range(sol[k-1]+1, n+1):# sol partiala e cuprinsa aici
        sol[k] = v
        len_crt.append(len(sol))
        k_fete = 0
        for val in range(1, nrf+1):
            if val in sol[1:k + 1:]:
                k_fete += 1
        if k == s:# sol finala
            if k_fete == s//2:# and 1 in sol[1:k+1:] and nrf+1 in sol[1:k+1:]:
                # subpunctul b)
                print(*sol[1:], sep=",")
        else:
            bkt(k+1)

nrf = int(input("nrf = "))
nrb = int(input("nrb = "))
s = int(input("s = "))
sol = [0] * (s+1)# va avea lungimea s+1
k_fete = 0
len_crt = []
bkt(1)
