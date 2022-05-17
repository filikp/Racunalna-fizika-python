"""
napišite program u Pythonu koji numerički rješava diferencijalnu jednadžbu i crta njezino rješenje 
za zadatak Ex 17.1.17  iz zbirke
https://www.whitman.edu/mathematics/calculus_online/section17.01.html

Ex 17.1.17 The half life of carbon-14 is 5730 years. 
If one starts with 100 milligrams of carbon-14, how much is left after 6000 years? 
How long do we have to wait before there is less than 2 milligrams?

U drugoj boji i drugim stilom (npr. dashed), na istoj slici, nacrtajte graf rješenja izravno
iz funkcije koju ćete naći pod linkom "answer". Krivulje bi se treble poklapati.
"""

import numpy as np
import matplotlib.pyplot as plt

hl = 5730       # vrijeme poluraspad
m_pocetno = 100 # početna masa u gramima
t = 6000        # zadano konačno vrijeme
m_konacno = 2   # zadana konačna masa

def konacno(T):     # Računanje konačne mase nakon vremena T
    K=np.log(2)/hl
    mk = m_pocetno*np.exp(-K*T)
    return mk;

print('Konačna masa je %.2fg' %konacno(t));

def vrijeme(m_konacno):     # Računanje vremena potrebnog da nam preostane masa m_konacno
    K=np.log(2)/hl
    tt = np.log(m_konacno/m_pocetno)/(-K)
    return tt;

print('Konačno vrijeme je %.2fs' %vrijeme(m_konacno));

T = np.linspace(0,35000,100000)
Y = konacno(T)
plt.axhline(konacno(t),color='blue', linestyle='dashed')
plt.axvline(vrijeme(m_konacno),color='green', linestyle='dashed')

M = np.linspace(0,100,1000)
X = vrijeme(M)

plt.plot(T,Y, color = 'yellow')
plt.plot(X,M, color = 'red',linestyle='dashed')
plt.axhline(color='black', zorder=-1)
plt.axvline(color='black', zorder=-1)
plt.xlabel('Vrijeme (godine)') 
plt.ylabel('masa (g)')
plt.grid()
plt.show()