#intarzierea maxima sa fie minima = mom la care s-a terminat activitatea - mom la care ar fi trebuit sa se termine
def citire():
    f=open("activitati.txt")
    n=int(f.readline())
    Lactiv=[]
    for linie in f:
        durata,termen=linie.split()
        Lactiv.append((int(durata),int(termen)))
    f.close()
    return Lactiv

def greedy(Lactivitati):
    Lactivitati.sort(key=lambda t: t[1])
    intarziere_max=0
    t_curent=0
    Sol=[] #(start,durata,termen,intarziere)
    for durata,termen in Lactivitati:
        intarziere=max(0,t_curent+durata-termen)
        if intarziere_max<intarziere:
            intarziere_max=intarziere
        Sol.append((t_curent,durata,termen,intarziere))
        t_curent+=durata
    return Sol,intarziere_max

def afisare(Lactivitati):
    g=open("intarzieri.txt", "w")
    g.write("Interval\tTermen\tIntarziere\n")
    for start,durata,termen,intarziere in Sol:
        #g.write(f"({start}-->{start+durata})\t\t\t{termen}\t\t{intarziere}\n")
        if len(str(start)) + len(str(start+durata)) == 2:
            s = "({}-->{})\t\t{}\t\t{}\n"
        else:
            s = "({}-->{})\t{}\t\t{}\n"
        g.write(s.format(start, start + durata, termen, intarziere))
    g.write(f"Intarziere maxima: {intarziere_max}")
    g.close()

Lactivitati=citire()
print(Lactivitati)

Sol,intarziere_max=greedy(Lactivitati)
print(Sol,intarziere_max)

afisare(Sol)