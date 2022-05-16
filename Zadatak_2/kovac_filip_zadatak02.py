'''
napišite program u Pythonu koji od korisnika traži unos vrijednosti jedne ili više fizičkih veličina
(ovisno o formuli koja je zadana za vaš zadatak) tako da za jednu od tih veličina (po vašem izboru)
program traži unos dvije vrijednosti, donje i gornje granice, a za ostale veličine (ako u formuli postoje)
traži unos samo jedne vrijednosti.

Nastojte da zadane vrijednosti imaju fizički smisao.

Zatim treba napraviti dvije liste. U listi x je 10 članova, vrijednosti one veličine za koju je unešena
gornja i donja granica (prvi član je donja granica, zadnji je gornja, a ostalih 8 su ekvidistantne vrijednosti).
U listi y je također 10 članova izračunatih po zadanoj formuli, tako da svakom članu liste y odgovara vrijednost
liste x s istim indeksom.

Konačno treba ispisati naziv fizičke veličine za koju su bile zadane donja i gornja granica te njezinu listu vrijednosti.
Ispod toga treba ispisati naziv fizičke veličine čija se vrijednost računala po zadanoj formuli te njezinu listu vrijednosti.

Evo primjera unosa i ispisa, ako je zadani izraz za tlak (kao omjer sile i površine):

Unesite površinu u kvadratnim metrima: 0.2
Unesite silu u njutnima (donja granica): 11
Unesite silu u njutnima (gornja granica): 20
Sila (N):  [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
Tlak (Pa):  [55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0]

Rješenje šaljite kao prilog mailu (attachment)
pod nazivom prezime_ime_zadatak02.py gdje su "prezime" i "ime" vaše prezime i ime
pisani malim slovima i bez dijakritičkih znakova.

Mail šaljite kao reply na ovaj mail tako da subject bude "Re: individualni zadatak 2/15 (nakon nastave održane 9. ožujka 2022.)".

Izraz (formula) za vaš zadatak je: moment sile = sila x krak x sin(kut)
'''

import numpy as np

#Unos
Fmin=float(input("Unesite MINIMALNI iznos sile u njutnima: "))
while Fmin<0:
    Fmin=float(input("Unesite MINIMALNI iznos sile veci od 0N: "))
Fmax=float(input("Unesite MAKSIMALNI iznos sile u njutnima: "))
while Fmax<Fmin:
    Fmax=float(input("Unesite MAKSIMALNI iznos sile veci od minimalnog: "))
r=float(input("Unesite duljinu kraka sile u metrima: "))
while r<=0:
    r=float(input("Unesite duljinu kraka sile veceg od 0m: "))
kut=float(input("Unesite kut u radijanima od 0 do 6.28: "))
while kut<0 or kut>6.28:
    kut=float(input("Unesite kut u radijanima od 0 do 6.28: "))

dio=(Fmax-Fmin)/9

F=[(round(Fmin+dio*(i),2)) for i in range(10)]  #lista sila
M=[(round(i*r*np.sin(kut),2)) for i in F]       #lista momenata sila

print("Sila (N): ", F)
print("Moment sile (Nm): ", M)

input("Press enter to close.")