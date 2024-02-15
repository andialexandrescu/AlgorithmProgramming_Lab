n = int(input("n="))
ziua = difmax = 0
k = 1
ieri = float(input("nr="))
while k < n:
    azi = float(input("nr="))
    dif = azi - ieri
    if dif > difmax:
        difmax = dif
        ziua = k
    ieri = azi
    k += 1
if difmax == 0:
    print("Nu a existat nicio crestere")
else:
    print(f"Cea mai mare crestere a fost de {round(difmax, 2)} intre zilele {ziua} si {ziua+1}")
