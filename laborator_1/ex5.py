# ec a ∗ x^2 + b ∗ x + c = 0
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
x1 = x2 = 0
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print(f"Functia are doua radacini reale x1={int(x1)} si x2={int(x2)}")
elif d == 0:
    x1 = (-b+d**0.5)/(2*a)
    print(f"Functia are o sg radacina reala x={int(x1)}")
else:
    print("Functia nu are radacini reale")

