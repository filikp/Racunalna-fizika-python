'''
Filip Kovač, zadatak 3

Napišite program u Pythonu koji 10 stringova, koje unese korisnik, 
posprema u listu. Zatim napravi dvije nove liste s nazivima: imena i brojevi.
U listi imena trebaju biti samo oni elementi izvorne liste koji nisu tipa int 
ili float, a u drugoj listi ostali elementi.
'''

unos = []
imena = []
brojevi = []

for i in range(10):
    unos.append(input("Unesite string: ")) #Svaki input je string
    
for i in unos:
    try:
        float(i)            #probaj 'i' tipa string pretvoriti u float
    except ValueError:      #Ako ne moze, dodaj taj elemenat u listu imena
        imena.append(i)
    else:                   #Ako moze, dodaj taj elemenat u listu brojevi
        brojevi.append(i)
print(imena)
print(brojevi)
