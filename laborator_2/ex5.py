'''Scrieți un program care să înlocuiască într-o propoziție toate aparițiile unui cuvânt 𝑠𝑠 cu un cuvânt 𝑡𝑡 (!cuvânt, nu subșir). Cuvintele sunt separate prin unul sau mai multe spații.'''

prop=input("prop=")
s=input("s=")
t=input("t=")
lista=prop.split(" ")
for i in range(len(lista)):
    if lista[i] == s:
        lista[i] = t
print(lista)
rez=" ".join(lista)
print(rez)