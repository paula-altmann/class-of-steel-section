import math
import sys


# pobieranie danych
def get_float_value(index, t_value):
    while True:
        try:
            x = float(input("Podaj wartość " + index + " [mm] = "))
            if index == "c" and x <= t_value:
                print("Podane c jest mniejsze od t - wprowadź poprawną wartość.")
                continue
            return x
        except ValueError:
            print("Podałeś niewłaściwą wartość, wpisz ją ponownie.")


def get_int_value(index):
    while True:
        try:
            x = int(input("Podaj wartość " + index + " [MPa] = "))
            return x
        except ValueError:
            print("Podałeś niewłaściwą wartość, wpisz ją ponownie.")


def section_force():
    while True:
        x = input("Przekrój ściskany czy zginany? [wpisz s/z]: ")
        if x == "z" or x == "s":
            return x
        print("Podałeś niewłaściwą literę. Wpisz z jeśli przekrój jest zginany, wpisz s jeśli przekrój jest ściskany.")


def class_of_section(b, E, y1, y2, y3):
    if b <= y1 * E:
        return 1
    elif b <= y2 * E:
        return 2
    elif b <= y3 * E:
        return 3
    else:
        return 4


print("Wprowadź poniższe dane aby wyliczyć klasę elementu. W zapisie dziesiętnym użyj kropki.")
t = get_float_value("t", None)
c = get_float_value("c", t)
fy = get_int_value("fy")
a = section_force()

# policzenie c/t oraz epsilon
b = c/t
E = math.sqrt((235/fy))

# sprawdzenie warunków
if a == "z":
    k = class_of_section(b, E, 72, 83, 124)
elif a == "s":
    k = class_of_section(b, E, 33, 38, 42)
else:
    print("Wprowadziłeś niepoprawną zmienną - uruchom ponownie program i wybierz s lub z")
    sys.exit(0)

# klasa przekroju
print("Klasa wprowadzonego przekroju: ", k)