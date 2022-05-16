print("Unesite jedan broj od 10 do 100: ")
n = int(input())
while n < 10 or n > 100:
    print("Unijeli ste pogresan broj. Unesite ponovno: ")
    n = int(input())

print("Unesite drugi broj od 1 do 10: ")
m = int(input())
while m < 1 or m > 10:
    print("Unijeli ste pogresan broj. Unesite ponovno drugi broj: ")
    m = int(input())

print("Unesite broj ispred matematičke operacije koju želite izvršiti:\n1: Zbrajanje\n2: Oduzimanje\n3: Mnozenje\n4: Dijeljenje ")
k = int(input())
while k < 1 or k > 4:
    print("Unijeli ste krivi broj. Unesite ponovno: ")
    k = int(input())

if k == 1:
    print("Zbroj vasa dva broja je: ", n+m)
if k == 2:
    print("Razlika vasa dva broja je: ", n-m)
if k == 3:
    print("Umnozak vasa dva broja je: ", n*m)
if k == 4:
    print("Kolicnik vasa dva broja je: ", round(n/m, 2))