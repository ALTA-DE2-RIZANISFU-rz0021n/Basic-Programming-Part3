
#bilangan = int(input())

print('Ini Adalah Program Pencari Faktor Bilangan')
print('==========================================')

bilangan = int(input("Faktor dari bilangan: "))
hasil = []
for i in range(1,bilangan+1):
    if bilangan % i == 0:
        hasil.append(i)

for faktor in hasil:
    print(faktor)