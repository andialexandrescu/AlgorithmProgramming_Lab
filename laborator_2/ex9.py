'''Cifrul lui Cezar
a) Se citește un text și un număr natural k. Să se afișeze textul cifrat cu cifrul lui Cezar, prin care fiecare literă (!doar literele) este înlocuită cu litera aflată peste 𝑘𝑘 poziții la dreapta în alfabet în mod circular (valoarea 𝑘𝑘 reprezintă cheia secretă comună pe care trebuie să o cunoască atât expeditorul, cât și destinatarul mesajului criptat). b) Se citește un număr natural k și text criptat cu cifrul lui Cezar cu cheia k. Să se afișeze textul decriptat'''

text = input("mesaj=")
text = text.upper()
k = int(input("k="))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rez1 = rez2 = ""

# subpunctul a) CRIPTARE
for x in text:
    if x in alpha:
        x_index = (alpha.find(x) + k) % len(alpha)
        rez1 = rez1 + alpha[x_index]
    else:
        rez1 = rez1 + x
print("criptare:", rez1)

# subpunctul b) DECRIPTARE
for x in text:  # Decrypt the encrypted message
    if x in alpha:
        x_index = (alpha.find(x) - k) % len(alpha)
        rez2 = rez2 + alpha[x_index]
    else:
        rez2 = rez2 + x
print("decriptare:", rez2)
