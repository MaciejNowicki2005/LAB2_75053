
print("Zadanie 1.0")
punkty = int(input("Podaj liczbę punktów (0-100): "))

while punkty>100 or punkty<0:
    punkty = int(input("Podaj faktyczną ilość punktów: "))

if punkty > 80:
    print("Zaliczenie w terminie 0")
elif punkty >= 50:
    print("Możesz poprawić wynik")
else:
    print("Musisz poprawić wynik")



print("Zadanie 2.0\nSortowanie liczb od najmniejszej do największej:")

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
z = int(input("Podaj z: "))

if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

print(f"Liczby w podanej kolejności to:{x}, {y}, {z}")


print("Zadanie 3.0\nSprawdzamy czy istnieje plik o podanym rozszerzeniu:")
nazwa_pliku = 'raport_maj.xlsx'

if nazwa_pliku.endswith('.xlsx'):
    print("Plik o podanym rozszerzeniu istnieje")
else:
    print("Plik o podanym rozszerzeniu nie istnieje")


print("Zadanie 4.A")
gol = int(input("Podaj liczbę strzelonych goli: "))
bonus = 0

if gol > 5:
    bonus = 5

if gol > 10:
    bonus = 10

wynik = gol * 10 + bonus
print(f"Wynik drużyny:{wynik}")


print("Zadanie 4.B")
gol = int(input("Podaj liczbę goli: "))
bonus = 0

if gol > 5:
    bonus = bonus + 5

if gol > 10:
    bonus = bonus + 10

wynik = gol * 10 + bonus
print(f"Wynik drużyny:{wynik}")


print("Zadanie 5.A\nZawartość pliku 'notowania giełdowe':")
with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
plik.close()

print("\nZadanie 5.B")
with open("notwania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")

with open("notwania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
plik.close()



print("\nZadanie 6.0")
litera = input("Podaj literę: ")

if litera.isupper():
    print("Duża litera")
elif litera.islower():
    print("Mała litera")
else:
    print("To nie jest litera")


print("Zadanie 7.0")
haslo = 'pk47!jy0893'

if len(haslo) == 11 and '!' in haslo:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")


print("Zadanie 8.0")
text = 'Studiuje-Informatykę'

print(text[:3])
print(text[-2:])


print("Zadanie 9.0")
text = input("Podaj tekst: ")
print(f"Tekst po podmianie wielkości znaków:{text.swapcase()}")
