#CUBURI
def citire():
    f=open("cuburi.txt")
    L=[]
    n=int(f.readline())
    for linie in f:
        lat,cul=linie.split()
        L.append((int(lat),cul))
        # o lista de tupluri
    f.close()
    return n,L

def greedy(Lcuburi):
    #sortarea cuburilor in ordine descrescatoare a dimensiunilor
    Lcuburi.sort(key=lambda t: -t[0])
    #Lcuburi.sort(reverse=True)

    h=Lcuburi[0][0] #h e inaltimea totala, init cu dim initiala a
    # cubului cu cea mai mare lungime, deoarece problema greedy mereu are solutie

    Sol=[Lcuburi[0]] # la baza turnului se aseaza cubul de latura maxima

    #pentru fiecare cub ramas se verifica daca culoarea cubului curent
    # difera de cea a celui anterior si se adauga sau nu
    for lat,cul in Lcuburi[1:]:# despachetare pe rand a tuplurilor din Lcuburi
        if cul!=Sol[-1][1]:# difera de culoarea sol anterioare (accesata prin indexul -1)
            Sol.append((lat,cul))
            h+=lat# creste inaltimea turnului

    return Sol,h# se returneaza sol finala si inaltimea totala, ceea ce se cere
    # a fi scris ca rezultat al problemei greedy

def afisare(Sol,h):
    g=open("turn.txt", "w")
    Lafisare=[]
    for cub in Sol:
        Lafisare.append("{} {}\n".format(*cub)) #despachetare
    Lafisare.append(f"\nInaltime totala: {h}")
    g.writelines(Lafisare)
    g.close()

# fiecare cub are o lungime si latura
# cuburi de dimensiuni diferite, pot avea ac culoare
# sa se determine turnul de lungime maxima - ord desc a dimensiunilor,
# culori diferite doua cate doua

n,Lcuburi=citire()
print(Lcuburi)
Turn,h2=greedy(Lcuburi)
print(Turn, h2)
afisare(Turn,h2)