x = int(input("x=")) # lungime saritura
n = int(input("n=")) # dupa cate sarituri se reduce x
p = int(input("p=")) # procente
m = int(input("m=")) # sarituri

aux_m = m
dist = 0
while aux_m != 0:
    if aux_m >= n:
        dist += n*x
    else:
        dist += aux_m*x
        break
    x = ((100-p)/100)*x # cand aux_m == m-k*n, unde k>=0
    aux_m -= n
print(f"Distanta parcursa de greiere este {int(dist)}")
