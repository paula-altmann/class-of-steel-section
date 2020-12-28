import math
import sys

print("Wprowadź poniższe dane aby wyliczyć klasę elementu. W zapisie dziesiętnym użyj kropki.")
# pobieranie danych
while True:
    try:
        t = float(input("Podaj wartość t [mm] = "))
        break
    except:
        print("Podałeś niewłaściwą wartość, wpisz ją ponownie.")
        continue

while True:
    try:
        c = float(input("Podaj wartość c [mm] = "))
        if c <= t:
            print("Podane c jest mniejsze od t - wprowadź poprawną wartość.")
            continue
        break
    except:
        print("Podałeś niewłaściwą wartość, wpisz ją ponownie.")
        continue

while True:
    try:
        fy = int(input("Podaj wartość fy [MPa] = "))
        break
    except:
        print("Podałeś niewłaściwą wartość, wpisz ją ponownie.")
        continue

while True:
    a = input("Przekrój ściskany czy zginany? [wpisz s/z]: ")
    if a == "z" or a == "s":
        break
    print("Podałeś niewłaściwą literę - wpisz z, jeśli przekrój jest zginany, wpisz s, jeśli przekrój jest ściskany.")

# policzenie c/t oraz epsilon
b = c/t
E = math.sqrt((235/fy))

# sprawdzenie warunków
if a == "z":
    if b <= 72*E:
        k = 1
    elif b <= 83*E:
        k = 2
    elif b <= 124*E:
        k = 3
    else:
        k = 4
elif a == "s":
    if b <= 33*E:
        k = 1
    elif b <= 38*E:
        k = 2
    elif b <= 42*E:
        k = 3
    else:
        k = 4
else:
    print("Wprowadziłeś niepoprawną zmienną - uruchom ponownie program i wybierz s lub z")
    sys.exit(0)

# klasa przekroju
print("Klasa wprowadzonego przekroju: ", k)

