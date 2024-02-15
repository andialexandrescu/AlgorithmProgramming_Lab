'''a) Se citește de la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat astfel: după fiecare vocală se adaugă litera p și încă o dată acea vocală (după a, e, i, o, u se adaugă respectiv pa, pe, pi, po, pu). Exemplu: “Ana are mere.” devine “Apanapa aparepe meperepe.” Fiind dat un astfel de text în limba păsărească, se poate obține textul original? Dacă da, scrieți un program care primind un text în limba păsărească construiește în memorie și afișează textul inițial.
b) Se citește de la tastatură un text în care cuvintele sunt despărțite în silabe cu ajutorul cratimelor. Se cere să se “traducă” textul dat în limba păsărească astfel: după fiecare silabă se adaugă litera p și se repetă ultima literă din acea silabă. Afișați traducerea și cu cratime, dar și fără.
Exemplu: “a-na a-re mul-te me-re ro-sii si de-li-cioa-se.” devine
“apa-napa apa-repe mulpl-tepe mepe-repe ropo-siipi sipi depe-lipi-cioapa-sepe.” și
“apanapa aparepe mulpltepe meperepe roposiipi sipi depelipicioapasepe.”
Fiind dat un astfel de text în limba păsărească (cel care conține și cratime), se poate obține textul original? Dacă da, scrieți un program care decodifică un astfel de text.'''

#a)1
s = input("s=")
aux = ""
voc = "aeiouAEIOU"
p = 0
for i in range(len(s)):
    if s[i] in voc:
        aux += s[p:i+1] + 'p' + s[i]
    else:
        aux += s[i]
    p = i + 1
print(aux)
#a)2
#var1
t = input("t=")
aux2 = ""
i = 0
while i < len(t):
    if t[i] in voc:
# daca e in lb pasareasca va fi o constructie de
# forma t[i]+'p'+t[i] implicit pt orice vocala din text
        aux2 += t[i]
        i += 3
    else:
        aux2 += t[i]
        i += 1
print(aux2)
#a)2
#var2
t2 = input("t2=")
for x in voc:
    t2 = t2.replace(x + 'p' + x, x)
print(t2)
#b)1
text = input("text=")
sol = sol2 = ""
for i in range(len(text)):
    if text[i] == ' ' or text[i] == '-':
        sol += text[p:i] + 'p' + text[i-1:i+1]
    else:
        sol += text[i]
    p = i + 1
sol2 = sol.replace('-', '')
print(sol, sol2, sep='\n')
#b)2
sir = input("sir=")
sol3 = sir.replace('-', '')
for x in sir:
    sol3 = sol3.replace(x+'p'+x, x)
print(sol3)

