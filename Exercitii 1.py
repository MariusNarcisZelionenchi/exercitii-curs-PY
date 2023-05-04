'''
1. ### În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# #R: o variabila este o 'cutie' cu valori // este o zona din memoria unui calculator unde se salveaza date

# # Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă: str, int, float, bool
'''

nume = 'Marius'
varsta=44
inaltime=1.78
conditie=False

# # Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type('nume'))
print(type(varsta))
print(type(inaltime))
print(type(conditie))

''' 
2. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere)
Verifică tipul acesteia.
'''

a = 5.323654
print(a)
a = round(a,4)
print(a)
print(type(a))

'''
3. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''

nume = 'Marius'
varsta = 44
inaltime = 1.78
conditie = False

print(f'Numele meu este {nume}.')
print(f'Am varsta de {varsta} ani.')
print(f'Am inaltimea {inaltime}.')
print(f'Afara este cald. {conditie}')
print('Numele meu este ' + nume + ', am varsta de ' + str(varsta) + ' ani, inaltimea de ' + str(inaltime) + '.')

'''
3. Citește de la tastatură: numele; prenumele. Afișează: 'Numele complet are x caractere'.
'''

nume = input('Introdu numele: ')
prenume = input('Introdu prenumele: ')
l = nume + prenume


print(f'Numele complet {prenume} {nume} are {len(l)} caractere')

'''
4. Citește de la tastatură: lungimea; lățimea. Afișează: 'Aria dreptunghiului este x'.
'''

lungime = float(input('Introdu lungimea L: '))
latime = float(input('Introdu latimea l: '))
aria = lungime * latime
print(f'Aria dreptungiului este: L*l = {aria}')

'''
5. Având stringul: 'Coral is either the stupidest animal or the smartest rock': afișează de câte ori apare
cuvântul 'the';
'''

str1 = 'Coral is either the stupidest animal or the smartest rock'
print(str1.count('the'))

'''
6. Același string: Folosește un assert ca să verifici dacă acest string conține doar numere.
'''

str1 = 'Coral is either the stupidest animal or the smartest rock'
assert str1.isnumeric()

'''
7. Citește de la tastatură un string de dimensiune impară; afișează caracterul din mijloc.
'''

str2 = input('Introdu un text cu numar impar de caractere: ')
caracter = int(len(str2) / 2)
print(str2[caracter])

'''
8. Folosind o singură linie de cod : citește un string de la tastatură (ex: 'alabala portocala'); salvează fiecare
cuvânt într-o variabilă; printează ambele variabile pentru verificare.
'''

print(input('Introdu 2 cuvinte: ').split())
a, b = 'alabala', 'portocala'
print(a, b)

'''
9. Citește un string de la tastatură (ex: alabala portocala); salvează primul caracter într-o variabilă -
indiferent care este el, încearcă cu 2 stringuri diferite; capitalizează acest caracter peste tot, mai puțin pentru
primul și ultimul caracter => alAbAlA portocAla.
'''

str3 = input('Introdu un text: ')
char1 = str3[0]
capital_char1 = char1.upper()
str4 = str3[1:-1].replace(char1, capital_char1)
print(char1 + str4 + str3[-1])

'''
10. Citește un user de la tastatură; citește o parolă; afișează: 'Parola pt user x este ***** și are y caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
'''

user = input('Introdu numele de utilizator: User = ')
parola = input(f'Introdu parola pentru utilizatorul {user}: Parola = ')
parola_mask = len(parola) * '*'
lungime_parola = len(parola)

print(f'Parola pentru utilizatorul {user} este {parola_mask} si are {lungime_parola} caractere')

'''
11. ### Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

if-else este un conditional care ne ajuta sa executam cod in functie de anumite conditii.
intr-un if avem prima data definita ramura if; aceasta se executa doar daca conditia de la if se egaleaza ca fiind
adevarata
daca nu e adevarata se va executa else
elif ne ajuta sa punem mai multe conditii
ex:

x = int(input('Introdu un numar '))
if x == 10:
    print('Numarul ales este 10')
elif x <= 0:
    print('Ai introdus un numar negativ')
elif x < 10:
    print('Numarul ales este mai mic decat 10')
else:
    print('Numarul ales este mai mare decat 10')
'''

'''
12. Verifică și afișează dacă x este număr natural sau nu.
'''

x = float(input('Introdu un numar x: '))

if x >= 0 and x % 1 == 0:
    print(f'{x} este un numar natural')
else:
    print(f'{x} nu este un numar natural')


'''
13. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''

x = float(input('Introdu un numar x: '))

if x < 0:
    print(f'{x} este un numar negativ')
elif x == 0:
    print(f'{x} este un numar neutru')
else:
    print(f'{x} este un numar pozitiv')

'''
14. Verifică și afișează dacă x este între -2 și 13.
'''

x = float(input('Introdu un numar x: '))

if -2 <= x <= 13:
    print(f'{x} este cuprins intre -2 si 13')
else:
    print(f'{x} nu este cuprins intre -2 si 13')

''' 
15. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''

x = float(input('Introdu un nr x: '))
y = float(input('Introdu un nr y: '))
dif_xy = x-y

if dif_xy < 5:
    print(dif_xy)
else:
    pass


'''
16. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
'''

x = float(input('Introdu un nr x: '))

if x not in range(5,28):
    print(f'numarul ales {x} nu este cuprins intre 5 si 27')
else:
    print(f'numarul ales {x} este cuprins intre 5 si 27')

''' 
17. x și y (int) - Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
'''

x = int(input('introdu un nr x: '))
y = int(input('introdu un nr y: '))

if x == y:
    print('Numerele alese sunt egale')
else:       #sau direct cu elif
    if x > y:
        print(x)
    else:
        print(y)

''' 
18. x, y, z - laturile unui triunghi. - Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''

# v1 - cu laturi:

print('introdu laturile triunghiului:')
x = float(input('x= '))
y = float(input('y= '))
z = float(input('z= '))

if x == y == z:
    print('triunghi echilateral')
elif x == y or x == z or y == z:
    print('triunghi isoscel')
else:
    print('triunghi oarecare')

# v2 - cu unghiuri:

x = int(input('introdu unghiul x: '))
y = int(input('introdu unghiul y: '))
z = int(input('introdu unghiul z: '))

if x + y + z == 180:
    if x == y == z:
        print('triunghi echilateral')
    elif x == y or x == z or y == z:
        print('triunghi isoscel')
    else:
        print('triunghi oarecare')
else:
    print('triunghiul nu exista')

''' 
19. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu.
'''

vocale = ['a', 'e', 'i', 'o', 'u']
litera = input('Introdu o litera: ')

if litera.isalpha():
    if litera in vocale:
        print('Ai introdus o vocala')
    else:
        print('Ai introdus o consoana')
else:
    print('Nu ai introdus o litera')

'''
20. Transformă și printează notele din sistem românesc în  sistem american: Peste 9 => A // Peste 8 => B //
Peste 7 => C // Peste 6 => D // Peste 4 => E // 4 sau sub => F
'''

nota = float(input('Introdu nota obtinuta: '))

if nota > 10:
    print('Nu ai introdus o nota valida')
else:
    if nota > 9:
        print('Ai obtinut nota A')
    elif 8 < nota <= 9:
        print('Ai obtinut nota B')
    elif 7 < nota <= 8:
        print('Ai obtinut nota C')
    elif 6 < nota <= 7:
        print('Ai obtinut nota D')
    elif 4 < nota <= 6:
        print('Ai otinut nota E')
    else:
        print('Ai obtinut nota F')

''' 
21. Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

x = int(input('Intro du un nr x: '))

if len(str(x)) == 4:
    print(f'{x} are 4 cifre')
elif len(str(x)) < 4:
    print(f'{x} nu are minim 4 cifre')
else:
    print(f'{x} are mai mult de 4 cifre')

''' 
22. Verifică dacă x are exact 6 cifre.
'''

try:
    x = int(input('Introdu un nr x: '))
except ValueError:
    print('Nu ai introdus un numar !!')
else:
    if len(str(x)) == 6:
        print(f'{x} are exact cifre')
    else:
        print(f'{x} nu are exact cifre')

''' 
23. Verifică dacă x este număr par sau impar (x e int).
'''

try:
    x = int(input('Introdu un nr x: '))
except ValueError:
    print('Nu ai introdus un numar !!')
else:
    if x % 2 == 0:
        print('x este un nr par')
    else:
        print('x este un nr impar')

''' 
24. x, y, z (int). Afișează care este cel mai mare dintre ele?
'''

try:
    x = int(input('Introdu un nr x: '))
    y = int(input('Introdu un nr y: '))
    z = int(input('Introdu un nr z: '))
except ValueError:
    print('Nu ai introdus un numar !!')
else:
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > y and z > x:
        print(z)
    else:
        print('Numerele introduse sunt egale')

''' 
25. x, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.
'''

try:
    x = int(input('introdu unghiul x: '))
    y = int(input('introdu unghiul y: '))
    z = int(input('introdu unghiul z: '))
except ValueError:
    print('Nu ai introdus valori valide')
else:
    if x + y + z == 180:
        print('Triunghi valid')
    else:
        print('Triunghiul nu este valid')

''' 
26. Având stringul: 'Coral is either the stupidest animal or the smartest rock': Citește de la tastatură un int x.
Afișează stringul fără ultimele x caractere. Exemplu: dacă ai ales 12 => 'Coral is either the stupidest animal or the s'
'''

str1 = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introdu valoarea lui x: '))

print(str1[:-x])

''' 
27. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
'''

str1 = 'Coral is either the stupidest animal or the smartest rock'
str2 = str1[:5] + str1[-5:]

print(str2)

''' 
28. Același string: Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care
te ajuta sa faci asta). Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest'
'''

str1 = 'Coral is either the stupidest animal or the smartest rock'
i_rock = str1.index('rock')
print(i_rock)
print(str1[:i_rock])

''' 
29. Joc ghicit zarul. Caută pe net și vezi cum se generează un număr random. Ne imaginăm ca dai cu zarul și salvăm acest
număr în dice_roll. Ia numărul ghicit de la utilizator. Verifică și afișează dacă utilizatorul a ghicit. Vei avea
3 opțiuni: Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y. / Ai pierdut. Ai ales un numar mai mare.
Ai ales x dar a fost y. / Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

import random

zar = int(input('Da cu zarul: '))
dice_roll = random.randint(1, 6)

if zar < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {zar} dar a fost {dice_roll}.')
elif zar > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {zar} dar a fost {dice_roll}.')
else:
    print(f'Ai ghicit. Felicitări! Ai ales {zar} si zarul a fost {dice_roll}.')

''' 
30. Citește de la tastatură un string. Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''

str1 = input('Introdu un scurt text: ')
c1 = str1[0]
c2 = str1[-1]

assert c1 == c2 or c1 == c2.upper() or c1.upper() == c2, 'Caractere diferite!'
print('Caractere identice')

''' 
31. Având stringul '0123456789': Afișează doar numerele pare. Afișează doar numerele impare.
(hint: folosește slicing, controlează din pas)
'''

str_numere = '0123456789'
print(str_numere[::2])
print(str_numere[1::2])