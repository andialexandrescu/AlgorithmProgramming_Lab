'''Se citesc doua cuvinte formate doar din litere mici. Să se verifice dacă sunt anagrame'''

x = input("x=")
y = input("y=")
if sorted(x) == sorted(y):
    print("sunt anagrame")
else:
    print("nu sunt anagrame")