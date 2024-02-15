#List comprehensions:
#a)
L=[chr(x) for x in range(ord('a'),ord('z')+1)]
print(L)
#b)
L2=[(x if x%2!=0 else -x) for x in range(1, int(input("n=")) +1)]
#L2=[x * (-1) ** (x+1) for x in range(1, int(input("n=")) +1)]
print(L2)
#c)
L3=[4,7,2,5,9,10,6]
L4=[(x) for x in L3 if x%2!=0]# nu fol op ternar pt ca nu se alterneaza valorile
print(L4)
#d)
L5=[L3[i] for i in range(len(L3)) if i%2!=0]
#L5=[L3[i] for i in range(1, len(L3), 2)]
#L5=L3[1::2]
print(L5)
#e)
L6=[2,4,1,7,5,1,8,10]
L7=[L6[i] for i in range(len(L6)) if i%2==L6[i]%2]
#L7=[val for poz, val in enumerate(L6) if poz%2==val%2]
print(list(enumerate(L6)))# se afiseaza poz alaturi de val coresp
print(L7)
#f)
L8=[1,2,3,4]
L9=[(L8[i], L8[i+1]) for i in range(len(L8)-1)]# lista de tupluri
print(L9)
#Matrice
M=[[(linie, coloana) for coloana in range(4)] for linie in range(3)]
# va contine 3 subliste formate fiecare din 4 tupluri
print(*M, sep='\n')
#g)
n=int(input("n="))
M1=[[f"{x}*{y}={x*y}" for y in range(1, n+1)] for x in range(1, n+1)]
for linie in M1:
    print(*linie, sep='\t')
#h)
sir="ABCDE"
l=[[sir[(i+j)%len(sir)] for i in range(len(sir))]for j in range(len(sir))]
# o lista de subliste fiecare avand orice element un caracter
l2=[sir[i:]+sir[:i] for i in range(len(sir))]
print(l, l2, sep="\n")
#i)
n=int(input("n="))
l3=[[i]*i for i in range(n)]
print(l3)
