#Zadatak 5 - Geometrijski niz 1 + 1/3 + 1/9 + 1/27 + ...

stvarna_vrijednost = 1.5
lista = []
suma = 0
koraci = 0

for i in range(34):
    suma = suma + 1/(3**i)
    koraci += 1
    razlika = stvarna_vrijednost - suma
    lista.append([koraci, suma, razlika])

i = 0
print("Broj koraka" + ' '*11 + "Suma" + ' '*24 + "Razlika")
while i < koraci:
    print("%5.d %30.20f %28.20f" %(lista[i][0], lista[i][1], lista[i][2]))
    i += 1