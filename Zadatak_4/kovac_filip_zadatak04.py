import numpy as np

RA,Dec,Mag,V,SigV = np.loadtxt('Shapley_galaxy.dat.txt', skiprows=1, unpack=True)

sve_V = 0

for i in range(4215):
    sve_V = sve_V + V[i]
avg_V = sve_V/4215

print(avg_V)

datoteka = open("ispis.dat","w")
for i in range(4215):
    if V[i]>avg_V:
        datoteka.write("%9.5f %11.5f %7.2f %7d %5d\n" %(RA[i], Dec[i], Mag[i], V[i], SigV[i]))
datoteka.close()

print(V)