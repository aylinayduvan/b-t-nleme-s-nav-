#SORU 1
from functools import reduce
a = []
y = int(input("Bir Sayı Giriniz"))
l = []
if (y%2 == 1):
    for i in range(1, (y+1)):
        a.append(i)
    print("Toplam Sonucu:",sum(a), "Çarpım Sonucu:", reduce(lambda n, d: n * d, a))
else:
    for i in range(0, y+1, 2):
        a.append(i)
    for i in range(1 , len(a)):
        l.append(a[i]*a[i])
    print("Kareleri Toplamı:",sum(l))




#SORU 2
a = int(input("0-15 Arası Bir Sayı Giriniz"))
aylinliste1 = []
aylinliste2 = []
deger = 1
if(0 <= a < 10):
    for l in range(0,a,1):
        aylinliste1.append(l)
    for l in range(0, (len(aylinliste1))):
        aylinliste2.append(aylinliste1[l]*aylinliste1[l])
    print("2. Soru Fonksiyon 1'in Çıktısı:",(sum(aylinliste2)+a*a))
elif (10 < a <=15):
    deger = 1
    for l in range(0, a, 1):
        aylinliste1.append((l))
    for l in range(0, (len(aylinliste1))):
        for i in range(l):
            deger = deger*(i+i)
    print(deger)
else:
    print("Girdiğiniz Sayı Negatif veya 15'ten Büyük Bir Sayısır")



#SORU 3
dosyam = open(file="ogrenciler.txt", mode='r', encoding='utf8')
a = (dosyam.readline())
y = (dosyam.readline())
l = (dosyam.readline())
i = (dosyam.readline())
print(a,y,l,i)


#SORU 4
from math import sqrt
print("ax^2 + bx + c = 0")
a = int(input("a Değerini Giriniz"))
b = int(input("b Değerini Giriniz"))
c = int(input("c Değerini Giriniz"))
delta = (b*b) - (4 * a * c)
if(delta > 0):
    kök1 = ((-1 * b) + sqrt(delta)) / 2 * a
    kök2 = ((-1 * b) - sqrt(delta)) / 2 * a
    print("Girilen Denklemin Kökleri:",round(kök1//1), "ve",round(kök2//1))
elif(delta < 0):
    print("Girilen Denklemin Kökleri Yoktur")
else:
    print("Girilen Denklemin Çakışık İki Kökü Vardır ve Bu Kök:",round(sqrt(c)))


