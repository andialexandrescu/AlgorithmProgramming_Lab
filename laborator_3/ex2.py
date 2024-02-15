L=[46,4,6,23,10,15,53,155]
#a)
print(sorted(L, key=lambda x: str(x)))
#print(sorted(L, key=str))
#b)
print(sorted(L, key=lambda x: str(x)[::-1]))
# realizeaza sortarea intre fiecare invers coresp elem din lista, fara a schimba val elem
#c)
L2=[27, 533, 44, 111, 5757, 234234]
print(sorted(L2, key=lambda x: len(str(x)), reverse=True))
#sortare stabila = in fct de cum se afla in lista initiala
#d)
print(sorted(L2, key=lambda x: len(set(str(x)))))
#e)
print(sorted(L2, key=lambda x: (len(str(x)), x)))
'''sortam in fct de 2 criterii, cel de-al doilea e verificat numai daca 
exita 2 elem din lista care respecta primul criteriu, respectiv au ac 
grad de importanta referitor la primul criteriu'''
