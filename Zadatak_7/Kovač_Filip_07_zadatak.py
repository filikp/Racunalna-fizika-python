'''
Zadatak 7

Napišite kod u Pythonu koji koristi vašu vlastitu funkciju 
(ne gotovu funkciju iz nekog modula) za računanje parametara 
pravca (koeficijenta smjera i odsječka na osi y) prilagođenog 
podacima
x              y            dy
-5.000     6.326     0.94257
-4.500     5.706     0.85015
-4.000     5.352     0.79752
-3.500     4.241     0.63187
-3.000     4.295     0.63989
-2.500     3.014     0.44907
-2.000     2.782     0.41452
-1.500     2.465     0.36732
-1.000     2.353     0.35066
-0.500     1.179     0.17571
0.000      0.919     0.13700
0.500      0.605     0.09018
1.000      0.454     0.06772
1.500     -0.645     -0.09611
2.000     -0.858     -0.12785
2.500     -1.552     -0.23132
3.000     -1.619     -0.24117
3.500     -2.160     -0.32177
4.000     -2.875     -0.42837
4.500     -3.538     -0.52719
5.000     -4.240     -0.63178
Koristite formule koje NE uključuju težinske faktore 
(weighted linear fit)
(pogledajte priloženi dokument linearfit.pdf)
Nacrtajte zadane podatke s pogreškama (error bars) i dobiveni 
pravac.
'''

import numpy as np
import matplotlib.pyplot as plt

def koeficijenti(xx,yy):
    a = (len(xx)*sum(xx*yy) - sum(xx)*sum(yy))/(len(xx)*sum(xx**2)-(sum(xx))**2) #koeficijent a
    b = y_sred - a*x_sred   #koeficijent b
    return a,b          #vraća koeficijente a i b

xx,yy,dy = np.loadtxt('Zadatak7.txt', skiprows=2, unpack=True) #vadi podatke iz txt dokumenta

x_sred = sum(xx)/len(xx)    #srednja vrijednost x koordinata
y_sred = sum(yy)/len(yy)    #srednja vrijednost y koordinata

x = np.linspace(-6, 6,100)

a,b = koeficijenti(xx,yy)   #spremi koeficijente iz funkcije 'koeficijenti' u a i b
y = a*x + b         #jednadžba pravca

plt.plot(x,y, color='blue', zorder=-1)  #pravac 
plt.errorbar(xx, yy, yerr=dy, fmt = 'ro') #greške
plt.axhline(color='black', zorder = -1) #horizontalna os x, boja crna, neka je u pozadini
plt.axvline(color='black', zorder = -1) #vertikalna os y, boja crna, u pozadini
plt.xlabel('$x$') #oznaci x os sa x nakošeno
plt.ylabel('$y$') #oznaci y os sa y nakoseno
plt.grid()  #crta mrežu
plt.show()  

