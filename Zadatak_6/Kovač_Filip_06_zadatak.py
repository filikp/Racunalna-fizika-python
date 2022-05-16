'''
napišite kod u Pythonu koji će nacrtati graf kao na slici

https://en.wikipedia.org/wiki/Planck%27s_law#/media/File:Black_body.svg
za Planckov zakon zračenja crnog tijela

Ne morate vjerno reproducirati baš svaki detalj (primjerice, na osima mogu biti numeričke vrijednosti u odabranom intervalu).
Važno je da odaberete odgovarajući matematički model (formulu), raspon vrijednosti varijable i nekoliko odgovarajućih vrijednosti parametara.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

#Funkcija koja računa radijaciju, tj zračenje crnog tijela
def plank(T,lmbd):
    B = ((2*h*c**3)/(lmbd**5))*(1/(np.exp((h*c)/(lmbd*k_B*T))-1))
    return B

h = cons.h      #Planckova konstanta
c = cons.c      #brzina svjetlosti
k_B = cons.k    #Boltzmanova konstanta

lmbd = np.linspace(0,3,200) #Valna duljina
lmbd = lmbd*10**(-6)        #Valna duljina u mikrometrima
f = c/lmbd                  #frekvencija

plt.plot(lmbd,plank(3000,lmbd), color='red', label = 'T=3000K')    #T=3000K
plt.plot(lmbd,plank(4000,lmbd), color='green', label = 'T=4000K')  #T=4000K
plt.plot(lmbd,plank(5000,lmbd), color='blue', label = 'T=5000K')   #T=5000K
plt.plot(lmbd,plank(6000,lmbd), color='black', label = 'T=6000K')  #T=6000K

plt.axhline(color='gray', zorder = -1)  #apscisa siva, u pozadini
plt.axvline(color='gray', zorder = -1)  #ordinata siva, u pozadini
plt.xlabel('Valna duljina (\u03BCm)')   #oznaka na apscisi
plt.ylabel('$B$')                       #oznaka na y osi

plt.grid()      #mreža
plt.legend()    #legenda
plt.show()
