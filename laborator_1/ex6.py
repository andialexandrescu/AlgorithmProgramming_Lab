n = int(input("n="))
rez_c = rez_d = 0

for c in range(9, 0, -1):
    aux = n
    while aux != 0:
        if c == aux%10:
            rez_d = rez_d*10+c # nr format din cifrele lui n in ord descrescatoare
        aux = aux//10

aux_rez_d = rez_d
while aux_rez_d != 0:
    rez_c = rez_c*10+aux_rez_d%10 # nr din cif ordine cresc e inversul celui cu cif descrescatoare
    aux_rez_d = aux_rez_d//10
# altfel:
'''for c in range(1, 10):
    aux = n
    while aux != 0:
        if c == aux%10:
            rez_c = rez_c*10+c
        aux = aux//10'''

print(f"Cifrele lui n in ordine descrescatoare: {rez_d}")
print(f"Cifrele lui n in ordine crescatoare: {rez_c}")
