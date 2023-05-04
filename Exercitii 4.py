# """
# OOP - advance
# Exerciții - studiu în workshopul de weekend
# 1. ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
# Inca o clasa care sa utilizeze metoda abstracta din clasa FormaGeormetrica
# """

from abc import ABC, abstractmethod

class GeometricForm(ABC):

    PI = 3.14

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print('Most likely I have corners !')

class Triangle(GeometricForm):

    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        area = self.height  * self.base / 2
        return area

# triangle1 = Triangle(12, 20)
# triangle1.describe()
# print(triangle1.area())

# '''
# POLIMORFISM
# '''

class Birds:

    def means_of_travel(self):
        print('Flying')

class Fish:

    def means_of_travel(self):
        print('Swimming')

def travel(animal):
    animal.means_of_travel()

# eagle = Birds()
# shark = Fish()
#
# travel(eagle)
# travel(shark)

# """
# 2. INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
# """

from abc import ABC, abstractmethod

class GeometricForm(ABC):

    PI = 3.14

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print('Most likely I have corners !')

class MySquare(GeometricForm):

    def __init__(self, side):
        self.__side = side

    def area(self):
        my_square_area = self.__side * self.__side
        return my_square_area

    @property
    def side(self):
        return self.__side

    @side.getter
    def side(self):
        return f'The square`s side is {self.__side}'

    @side.setter
    def side(self, new_side_value):
        print(f'The new side value is {new_side_value}')
        self.__side = new_side_value

    @side.deleter
    def side(self):
        print('The square`s side was deleted')
        self.__side = None

# square1 = MySquare(4)
# print(square1.area())
# new_side_value = 10
# square1.side = new_side_value
# square1.area()



# """
# 3. Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# """

class Circle(GeometricForm):

    def __init__(self, raza):
        self.__raza = raza

    def area(self):
        area_C = self.PI * self.__raza
        return area_C

    def describe(self):
        print('I definitely don`t have cormers')

# cerc1 = Circle(5)
# cerc1.describe()

"""

a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).

b. Implementeaza proprietatea password care va incapsula atributul privat
password.
Va avea:
- getter:
In getter verificam daca parola a fost setata (daca are valoare).
Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
cu lungimea parolei.
Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.
- setter:
In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
urmatoarele conditii:
    -- are minim 10 caractere
    -- are cel putin o litera mare
Daca aceste conditii se indeplinesc atunci setam parola.
Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.

c. Metode:
- Metoda login: verificam ca user-ul are atat username, email si parola.
Daca are, atunci afisam mesajul "Conectat".
Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"

d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
Afiseaza toate atributele/metodele/proprietatile.
"""


class User():

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.getter
    def password(self):
        print('Get')

        if self.__password is not None:
            pass_hidden = len(self.__password) * '*'
            return pass_hidden

        else:
            print('No password')

    @password.setter
    def password(self, new_pass):
        print('Set')
        if new_pass is not None and len(new_pass) >= 10:
            for letter in new_pass:
                if letter.isupper():
                    self.__password = new_pass
                    break
            else:
                print('The password must contain at least one uppercase letter')
        else:
            print('The password must have at least 10 characters')

    def login(self):
        if self.username and self.email and self.__password:
            print('Conectat')
        else:
            print('Lipsesc credentiale de conectare. Nu va putem conecta')


# user1 = User('mnz', 'bla@bla.bla')
# print(user1.username)
# print(user1.email)
# print(user1.password)
# user1.password = 'A1234567'
# print(user1.password)
# user1.login()
