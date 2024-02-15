'''Se citește un text codificat după regula: În fata fiecărui caracter este scris un număr de cel mult 2 cifre care reprezintă numărul de apariții consecutive ale acestui.
a) Scrieți un program care decodifica textul. De exemplu textul 1G10o4l se va decodifica Goooooooooollll
b) Scrieți un program care, dat un text, îl codifică după regula de la a)'''

sir=input("sir=")
output=""
nr=0
#subpunctul a)
for c in sir:
    if c.isdigit():
        nr = nr * 10 + int(c)
    else:
        output += c * nr
        nr = 0
print(output)
#subpunctul b)
s="Gooooooolll"
nr=1
rez=""

for i in range(1,len(s)):
    if s[i] == s[i+1]:
        nr=nr+1
    else:
        rez=rez+str(nr)+s[i-1]
        nr=1
rez=rez+str(nr)+s[-1]
print(rez)
