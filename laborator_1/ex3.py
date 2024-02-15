l1 = int(input("l1="))
l2 = int(input("l2="))
d = d1 = d2 = 0
def cmmdc(a, b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    r = a
    return r

d = cmmdc(l1, l2) # dimensiunea unei placute astfel incat sa nu fie modificata (taiata etc)
d1 = l1 // d # cate placute incap pe lungimea l1
d2 = l2 // d # cate placute incap pe l2
arie = d1 * d2 # aria reprez nr total de placute
print (f"Fiecare placuta are dimensiunea de {d}, fiind necesare {arie} placute")

'''cmmdc(280, 440)=40
280:40=7
440:40=11
arie=7*11=77'''

