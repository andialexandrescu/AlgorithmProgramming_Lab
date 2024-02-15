#1)
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
l1[::2] = l2[::2]
#l1 = [l2[i] if i%2==0 else l1[i] for i in range(len(l1))]
print(l1)
#2)
l3 = [2, 3, 67, 78, 0, 90, 80, 0, 667, 0, 0]
poz1 = poz2 = None
for i in range(len(l3)):
    if l3[i]==0 and poz1 is None:
        poz1 = i
    elif l3[i]==0 and poz1 is not None and poz2 is None:
        poz2 = i
l3 = l3[:poz1:] + l3[poz2+1::]
print(l3)
#3)
l4 = [2, 3, 67, 78, 0, 90, 80, 0, 667, 0, 0]

#VAR1
#l4 = [x for x in l4 if x != 0]

#VAR2
for i in range(len(l4)-1, -1, -1):
    if l4[i]==0:
        l4 = l4[:i:] + l4[i+1::]

#VAR3
#while 0 in l4:
    #l4.remove(0)

print(l4)
#4)
l5 = [0, 1, 6, 8, 3, 2, 2, 9, 10, 3]
k = 3
poz1 = min_s = None
s = 0
#for x in l5[:len(l5)-k+1]: p = l5.index(x)
for p in range(len(l5)-k+1):
    s = sum(l5[p:p+k])
    #print(s)
    if min_s is None or min_s > s:
        min_s = s
        poz1 = p #poz2 = p+k-1
l5 = l5[:poz1] + l5[poz1+k:] #l5[:poz1] + l5[poz2+1:]
print(l5)
#5)
l6 = [int(x) for x in input("l6 = ").split()] # 2 2 3 3 3 4 4 4 5 5 5 5 6

#VAR1
#l6 = list(set(l6))

#VAR2
l6fin = [l6[0]] #init cu primul element din l6, care altfel in for loop e ignorat
for i in range(1, len(l6)):
    if l6[i] != l6[i-1]:
        l6fin.append(l6[i])
        # GRESIT l6.remove(l6[i]) - you can't modify the list while iterating over it
l6 = l6fin
print(l6)
#6)
l7 = [int(x) for x in input("l7 = ").split()] # -1 1 2 3 -9 -56 4 -5 -2 0
stop = len(l7)
while i < stop:
    if l7[i]<0:
        l7.insert(i+1, 0)
        stop = len(l7) #actualizam lungimea listei pt ca exista posibilitatea ca ultimele
        # valori negative din lista sa fie igmnorate, deoarece am inserat pana la acel moment
        # zerouri fara sa tinem cont de marirea listei si mutarea elementelor initiale cu
        # cateva pozitii mai la dreapta
        i += 2
    else:
        i += 1
print(l7)
