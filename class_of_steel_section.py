import math
import sys

print("Wprowadź poniższe dane aby wyliczyć klasę elementu. W zapisie dziesiętnym użyj kropki.")
# pobieranie danych
t = float(input("Podaj wartość t [mm] = "))
c = float(input("Podaj wartość c [mm] = "))
fy = int(input("Podaj wartość fy [MPa] = "))
a = input("Przekrój ściskany czy zginany? [wpisz s/z]: ")

# policzenie c/t oraz epsilon
b = c/t
E = math.sqrt((235/fy))

# sprawdzenie warunków
if a == "z":
    if c/t <= 72*E:
        k = 1
    elif c/t <= 83*E:
        k = 2
    elif c/t <= 124*E:
        k = 3
    else:
        k = 4
elif a == "s":
    if c/t <= 33*E:
        k = 1
    elif c/t <= 38*E:
        k = 2
    elif c/t <= 42*E:
        k = 3
    else:
        k = 4
else:
    print("Wprowadziłeś niepoprawną zmienną - uruchom ponownie program i wybierz s lub z")
    sys.exit(0)

# klasa przekroju
print("Klasa wprowadzonego przekroju: ", k)

