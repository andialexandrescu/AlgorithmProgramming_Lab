'''Se citește un cuvânt. Să se șteargă din cuvânt toate aparițiile primei litere.
Se va afișa un mesaj de forma: După ștergerea literei 'X' șirul obținut este "S"
de lungime L folosind diferite tipuri de formatare (cu parametri poziționali și
f-stringuri)'''

sir=input("sir=")
rez=sir.replace(sir[0], "")
print(f"După ștergerea literei '{sir[0]}' șirul obținut este \"{rez}\" de lungime {len(rez)}")
print(sir.split(sir[0]))
rez2="".join(sir.split(sir[0]))# ce e in stanga primului caracter
print("După ștergerea literei '{}' șirul obținut este \"{}\" de lungime {}".format(sir[0], rez2, len(rez2)))
#formatare cu parametri pozitionali
