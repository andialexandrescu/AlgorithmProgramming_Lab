n = int(input("n="))
k = 1
max1 = max2 = None
# max1 < max2
while k <= n:
    x = int(input("x="))
    if max2 is None or x > max2:
        max1 = max2
        max2 = x
    elif max1 is None or x > max1:
        max1 = x
    k += 1
if (max1 is not None and max2 is not None) and max1 != max2:
    print(f"Cele mai mari valori din sir sunt {max2} > {max1}")
else:
    print("Imposibil, nu exista valori distincte in sir")
