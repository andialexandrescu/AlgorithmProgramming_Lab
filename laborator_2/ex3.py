'''Se citește un cuvânt s de cel mult 10 de caractere.
Sa se afișeze (folosind s[i:j]) pe câte o linie cuvintele
obținute succesiv din s tăind prima și ultima literă (afișate
centrat pe 10 de caractere):
algoritm
 lgorit
  gori
   or    '''

sir=input("sir=")
k=0
for i in range(len(sir)//2+len(sir)%2):# sir de lungime para vs impara
    print(sir[i:len(sir)-i].center(len(sir),' '))
