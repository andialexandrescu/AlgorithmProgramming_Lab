n = int(input("n="))
aux = n
inv = 0
while aux != 0 :
    inv = inv*10 + aux%10
    aux = aux//10
if inv == n:
    print("Da, este palindrom")
else:
    print("Nu, nu este palindrom")
