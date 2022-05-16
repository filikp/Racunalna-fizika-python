'''
Zadatak _8

napišite Python-kod koji nalazi korijene jednadžbe y=0 koristeći funkciju brentq iz modula scipy.optimize
Funkciju f(x)=y najprije nacrtajte kako biste vidjeli koje početne točke za traženje korijena treba odabrati.

Vaša jednadžba je c
na mrežnoj stranici
http://www.math-exercises.com/analysis-of-functions

Rješenja formatirano ispišite u terminalu i na samoj slici.
Točke u kojima funkcija siječe x-os nacrtajte pomoću funkcije scatter, uz parametar koji određuje veličinu.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def fun(x):
    return 3*x**5-5*x**3

r1 = opt.brentq(fun, -2, -1)    #Rješenje 1
r2 = opt.brentq(fun, -1, 1)     #Rješenje 2
r3 = opt.brentq(fun, 1, 2)      #Rješenje 3

print("Rješenja dane jednažbe za y = 0 su: \nr1 = %f \nr2 = %f \nr3 = %f" %(r1,r2,r3))  #Ispis rješenja

x = np.linspace(-1.5,1.5,100) #Za veći raspon x osi se ne vidi gdje funkcija sijeće os x, zato sam uzeo granice od -1.5 do 1.5

plt.plot(x,fun(x), color= "red")    #Crtanje funkcije

plt.axhline(color='gray', zorder = -1)  #apscisa siva, u pozadini
plt.axvline(color='gray', zorder = -1)  #ordinata siva, u pozadini
plt.xlabel('$x$')   #oznaka na apscisi
plt.ylabel('$y$')   #oznaka na y osi
plt.scatter(r1, 0, s = 50, label = ("x = %.5f" %r1))    #točka na grafu za rješenje 1
plt.scatter(r2, 0, s = 100, label = ("x = %.1f" %r2))   #točka na grafu za rješenje 2
plt.scatter(r3, 0, s = 75, label = ("x = %.5f" %r3))    #točka na grafu za rješenje 3
plt.grid()  #mreža
plt.legend() #legenda
plt.show()