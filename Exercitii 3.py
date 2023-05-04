"""
PARTEA 1 - FUNCTII

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile: Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

"""
1. Funcție care să calculeze și să returneze suma a două numere.
"""

def suma_2_nr(x, y):
    suma = x + y
    return suma

s1 = suma_2_nr(5, 2)

print(s1)


"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar.
"""

def par_impar(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(par_impar(5))
print(par_impar(4))

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""

x = input(' Cum te numesti?: ')
def caractere_nume(x):
    l = len(x)
    print(l)

#pentru a calcula doar caracterele numelui, fara spatii:

def caractere_nume(nume, prenume, nume_mijlociu):
    total_caractere = len(nume) + len(prenume) + len(nume_mijlociu)
    return total_caractere

print(caractere_nume('Marius', 'Narcis', 'Zelionenchi'))


"""
4. Funcție care returnează aria dreptunghiului.
"""

def arie_dreptunghi(lungime, latime):
    arie_d = lungime * latime
    return arie_d

print(arie_dreptunghi(4, 4))

"""
5. Funcție care returnează aria cercului.
"""

import math

def arie_cerc(r):
    arie_c = math.pi * r * r
    return arie_c

print(arie_cerc(2))

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""

text = input('Introdu un text: ')
x = input('Introdu un caracter x: ')

def x_in_text(x, text):
    if x in text:
        return True
    else:
        return False

print(x_in_text(x, text))

"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x.
Numărul de caractere upper case exte y.
"""

text = input('Introdu un text: ')
x = 0
y = 0
def nr_caractere(text, x, y):
    for a in text:
        if a.islower():
            x += 1
        else:
            y += 1
    print(f'Numărul de caractere lower case este {x}')
    print(f'Numărul de caractere upper case este {y}')

nr_caractere(text, x, y)


"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""

text = input('Introdu o lista de numere: ')
lst = text.split()
lst_poz = []

def nr_poz_lista(lst):
    for nr in lst:
        if int(nr) > 0:
            lst_poz.append(int(nr))
    return lst_poz

print(nr_poz_lista(lst))

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ:
Primul număr x este mai mare decat al doilea număr y.
Al doilea număr y este mai mare decat primul număr x.
Numerele sunt egale.
"""

x = input('x = ')
y = input('y = ')

def comparatie(x, y):
    if x > y:
        print('Primul număr x este mai mare decat al doilea număr y')
    elif x < y:
        print('Al doilea număr y este mai mare decat primul număr x.')
    else:
        print('Numerele sunt egale.')

comparatie(x, y)

"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""

# DE INTREBAT CUM PUTEM FACE SA CITIM DE LA TASTATURA DATELE DE INTRODUS

x = input('Introdu un numar x: ')
print('Introdu un set de numere:')
set_numere = {input(), input(), input()}

def set_nou(x, set_numere):
    if x in set_numere:
        print('Nu am adaugat numărul în set. Acesta există deja:')
        print(set_numere)
        return False
    else:
        print('am adaugat numărul nou în set:')
        set_numere.add(x)
        print(set_numere)
        return True

print(set_nou(5, {1,2,3}))
print(set_nou(2, {1,2,3}))

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""

def nr_zile(luna):
    if luna == 'februarie':
        return 28
    if luna in ['ianuarie', 'martie', 'mai', 'iulie', 'august', 'octombrie', 'decembrie']:
        return 31
    else:
        return 30

print(nr_zile('aprilie'))

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

x = int(input('Introdu un nr x: '))
y = int(input('Introdu un nr y: '))

def suma(x, y):
    suma = x + y
    return suma
def diferenta(x, y):
    diferenta = x - y
    return diferenta
def inmultirea(x, y):
    inmultirea = x * y
    return inmultirea
def impartirea(x, y):
    impartirea = x / y
    return impartirea

def calculator(*args):
    return suma(x, y), diferenta(x, y), inmultirea(x, y), impartirea(x, y)

print(calculator(x, y))


"""
13. Funcție care primește o listă de cifre (adică doar 0-9).
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

def count_cifre(lista):
    dictionar = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0 , 8:0, 9:0}
    for cheie in dictionar.keys():
        dictionar[cheie] = lista.count(cheie)
    return dictionar

print(count_cifre([0,0,0,1,1,2,2,2,3]))

"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""

def cmM_nr(x, y, z):
    lista_nr = [x, y, z]
    return max(lista_nr)

print(cmM_nr(1,5,2))

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""

def suma_n(n):
    for i in range(n):
        n += i
    return n

print(suma_n(3))

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""

# v1:
def nr_comune(lst1, lst2):
    set_comun = []
    for i in lst1:
        for j in lst2:
            if i == j:
                set_comun.append(i)
    set_comun = set(set_comun)
    return set_comun

print(nr_comune([1, 1, 2, 3], [2, 2, 3, 4]))


# v2 (utilizand intersection de la seturi):

lst1 = [1,1,2,3]
lst1 = set(lst1)
lst2 = [2,3,3,4]
lst2 = set(lst2)
def nr_comune(lst1, lst2):
    return lst1.intersection(lst2)

print(nr_comune(lst1,lst2))

"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""

def promotie(pret, reducere):
    pret_nou = pret - reducere * pret / 100
    if pret_nou < 0:
        print('Reducerea este prea mare')
    else:
        return pret_nou

print(promotie(100,10))

"""
18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișează și data și ora curentă din China)
"""

import pytz
import datetime

def get_current_datetime(timezone):
    tz = pytz.timezone(timezone)
    current_datetime = datetime.datetime.now(tz)
    print(current_datetime)


print(pytz.all_timezones)
get_current_datetime('Europe/Bucharest')
get_current_datetime('Asia/Shanghai')
get_current_datetime('Australia/Sydney')

"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

def countdown(day, month, year):
    import datetime

    data_curenta = datetime.date.today()
    data_dorita = datetime.date(year, month, day)
    if year < data_curenta.year:
        data_dorita = datetime.date(data_curenta.year, month, day)
    zile_ramase = (data_dorita - data_curenta).days
    print(f'Mai sunt {zile_ramase} zile pana la eveniment!')

countdown(17, 3, 2024)

"""
PARTEA 2 - OOP: Clase & Obiecte
"""

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
"""

import math

class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul e de culoare {self.culoare} si are raza de {self.raza}')

    def aria_cerc(self):
        aria_c = math.pi * self.raza * self.raza
        return aria_c

    def diametru_cerc(self):
        diametru = 2 * self.raza
        return diametru

    def circumferinta_cerc(self):
        circumferinta = math.pi * 2 * self.raza
        return circumferinta

cerc1 = Cerc(3, 'alb')

cerc1.descrie_cerc()
print(f'Aria cercului este {cerc1.aria_cerc()}')
print(f'Diametrul cercului este {cerc1.diametru_cerc()}')
print(f'Circumferinta cercului este {cerc1.circumferinta_cerc()}')

"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va 
suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Dreptunghiul va avea lungimea de {self.lungime}cm, latimea de {self.latime}cm si va avea culoarea <{self.culoare}>')

    def aria_dreptunghi(self):
        aria_d = self.lungime * self.latime
        return aria_d

    def perimetru_dreptunghi(self):
        perimetru_d = 2 * (self.lungime + self.latime)
        return perimetru_d

    def sch_culoare(self, culoare_noua):
        self.culoare = culoare_noua
        self.descrie_dreptunghi()

dreptunghi1 = Dreptunghi(10, 5, 'alb')
dreptunghi1.descrie_dreptunghi()
print(f'Aria dreptunghiului este {dreptunghi1.aria_dreptunghi()}cm patrati')
print(f'Perimetrul dreptunghiului este {dreptunghi1.perimetru_dreptunghi()}cm')
dreptunghi1.sch_culoare('rosu')

"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""

class Employee:

    def __init__(self, name, first_name, salary):
        self.name = name
        self.first_name = first_name
        self.salary = salary

    def descrie(self):
        print(f'The employee {self.first_name} {self.name} has a salary of {self.salary}$')

    def full_name(self):
        employee = self.first_name + ' ' + self.name
        return employee

    def monthly_salary(self):
        return self.salary

    def yearly_salary(self):
        y_salary = 12 * self.salary
        return y_salary

    def raise_salary(self, percent):
        self.percent = percent
        r_salary = self.salary + self.salary * self.percent / 100
        return r_salary

employee1 = Employee('Zelionenchi', 'Marius Narcis', 4000)
employee1.descrie()
print(f'The employee full name is {employee1.full_name()}')
print(f'{employee1.full_name()}`s monthly salary is {employee1.monthly_salary()}')
print(f'{employee1.full_name()}`s yearly salary is {employee1.yearly_salary()}')
print(f'{employee1.full_name()} got a raise and the new  monthly salary is {employee1.raise_salary(45)}$')

employee2 = Employee('Zelionenchi-Balbuzan', 'Raluca Ruxandra', 4000)
employee1.descrie()
print(f'The employee full name is {employee2.full_name()}')
print(f'{employee2.full_name()}`s monthly salary is {employee2.monthly_salary()}')
print(f'{employee2.full_name()}`s yearly salary is {employee2.yearly_salary()}')
print(f'{employee2.full_name()} got a raise and the new monthly salary is {employee2.raise_salary(90)}$ because she is \n The Love of My Life')

"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""

class Account:

    def __init__(self, IBAN, account_holder, total_amount):
        self.IBAN = IBAN
        self.account_holder = account_holder
        self.total_amount = total_amount

    def bank_statement(self):
        print(f'{self.account_holder} has in the {self.IBAN} acount, the amount of {self.total_amount}$')

    def debit_account(self, debit):
        self.debit = debit
        new_amount_d = self.total_amount - self.debit
        return new_amount_d

    def credit_account(self, credit):
        self.credit = credit
        new_amount_c = self.debit_account(self.debit) + self.credit
        return new_amount_c

account1 = Account('RO35BTUSD2546597843', 'Marius Narcis Zelionenchi', 45000)
account1.bank_statement()
print(f'His account was debited, and the new total amount is {account1.debit_account(2000)}')
print(f'His account was credited, and now, the new total amount is {account1.credit_account(6000)}')

"""
5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
"""

class Invoice:
    serial = 'MNZ'
    import datetime
    def __init__(self, number, product, quantity, item_price):
        self.number = number
        self.product = product
        self.quantity = quantity
        self.item_price = item_price

    def change_quantity(self, new_q):
        self.quantity = new_q
        return new_q

    def change_price(self, new_i):
        self.item_price = new_i
        return new_i

    def change_product(self, new_p):
        self.product = new_p
        return new_p

    def total(self):
        return self.quantity * self.item_price

    def generate_invoice(self):
        print(f'{invoice1.product} | {invoice1.quantity} | {invoice1.item_price} | {invoice1.total()}')

invoice1 = Invoice(6554, 'Laptop Asus', 3, 3999)
print(f'Invoice {Invoice.serial} number {invoice1.number}')
print(datetime.date.today())
invoice1.generate_invoice()
invoice1.change_quantity(5)
invoice1.change_product('Remarkable Tablet')
invoice1.change_price(2599)
invoice1.generate_invoice()
invoice1.change_price(1500)
invoice1.change_product('iPhone')
invoice1.change_quantity(10)
invoice1.generate_invoice()

