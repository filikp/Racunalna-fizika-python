'''
riješite zadatak Revision 13  iz zbirke "Exercises in Mechanics – Cambridge University",
koju možete naći u privitku.

Zatim napišite program u Pythonu kojim se numerički potvrđuje i vizualizira vaše rješenje.
'''

import numpy as np
import scipy.optimize as opt
import scipy.integrate as ing
import matplotlib.pyplot as plt 

a = lambda t: 6*t - 3*t**2

# a)
v = ing.quad(a,0,2)
print("Brzina čestice u trenutku t=2s je %.2f m/s" %v[0])

# b)
def dv(t):
    V = 3*t**2-t**3
    return V

T = opt.brentq(dv,2,4)
print("Čestica miruje u trenutku nakon %.2fs" %T)

# c)
def ds(t):
    S = t**3-0.25*t**4
    return S

s = ds(T)
print("Udaljenost koju je čestica prešla do trenutka mirovanja je %.2fm" %s)


TT = np.linspace(0,4,200)

plt.axvline(T,color='blue', linestyle='dashed') #Vrijeme kada je brzina 0
plt.axhline(dv(2),color='red', linestyle='dashed')  #Brzina nakon 2 sec

plt.plot(TT, dv(TT))    #Brzina u ovisnosti o vremenu
plt.axhline(color='black', zorder=-1)
plt.axvline(color='black', zorder=-1)
plt.xlabel('Vrijeme (s)') 
plt.ylabel('brzina (m/s)')
plt.grid()
plt.show()

plt.axhline(s,color='red', linestyle='dashed')  #Udaljenost kada je brzina 0 m/s
plt.axvline(T,color='green', linestyle='dashed')  #Trenutak kada je brzina 0

plt.plot(TT, ds(TT))    #Brzina u ovisnosti o vremenu
plt.axhline(color='black', zorder=-1)
plt.axvline(color='black', zorder=-1)
plt.xlabel('Vrijeme (s)') 
plt.ylabel('Udaljenost od početnog položaja (m)')
plt.grid()
plt.show()