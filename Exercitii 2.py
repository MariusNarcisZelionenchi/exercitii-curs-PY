'''PARTEA 1 - STRUCTURI DE DATE

Exerciții - studiu în workshopul de weekend

1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o
suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o
 listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își
 găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

portativ = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(portativ)
portativ = portativ[::-1]
print(portativ)
portativ.reverse()
print(portativ)

"""
2. De câte ori apare ‘do’?
"""

portativ = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(portativ.count('do'))

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. 
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
# v1:
l3 = l1 + l2
print(l3)
# v2:
l1.extend(l2)
print(l1)

"""
4.
Sortează și afișează lista generată la exercițiul anterior.
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1 + l2
l3.sort()
print(l3)

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1 + l2

if len(l3) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1 + l2

l3.clear()
print(l3)

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1 + l2

l3.clear()
print(l3)

if len(l3) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""

dict1 = {
    'Ana':8,
    'Gigel':10,
    'Dorel':5
}
print(dict1.keys())

"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""

dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
nota_Ana = dict1['Ana']
nota_Gigel = dict1['Gigel']
nota_Dorel = dict1['Dorel']
print(f'Ana a luat nota {nota_Ana}')
print(f'Gigel a luat nota {nota_Gigel}')
print(f'Dorel a luat nota {nota_Dorel}')
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Raluca a luat nota {dict1.get('Raluca', 7)}")

"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
"""

dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}

dict1['Dorel'] = 6
print(dict1)

"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
"""

dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
del dict1['Gigel']
dict1['Ionica'] = 9
print(dict1)

"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
"""
# v1:

echipa = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(echipa)
sch_max = 3
sch = 0

for j in echipa:
    player_out = input('Scoate un jucator de pe teren: ')

    if player_out in echipa:
        player_in = input('Introdu un jucator pe teren: ')
    else:
        print('Jucatorul ales nu este pe teren')

    if sch < sch_max:
        if player_out in echipa:
            echipa.remove(player_out)
            sch = sch + 1
            echipa.append(player_in)
            print(f'A intrat {player_in}, a ieșit {player_out}, mai ai {sch_max - sch} schimbări')
            print(f'Noua echipa este {echipa}')
        else:
            print(f'Nu se poate efectua schimbarea deoarece jucătorul {player_out} nu e în teren')
            print(f'mai ai {sch_max - sch} schimbari')
            break
    else:
        print('Nu sunt posibile alte schimbari')
        break

# v2:

echipa = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
nrsch = 3
while 0 < nrsch <= 3:
    x = input('Scoate un jucator de pe teren: ')
    if x in echipa:
        echipa.remove(x)
        nrsch = nrsch - 1
        y = input('Introdu un jucator pe teren: ')
        echipa.append(y)
        print(f'A intrat {y}, a ieșit {x}, mai ai {nrsch} schimbări')
    else:
        print(f'nu se poate efectua schimbarea deoarece jucătorul {x} nu e în teren')
        print(f'Mai ai  {nrsch} schimbari')
print(echipa)

"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
"""

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
"""

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

if weekend.issubset(zile_sapt):
    print('weekend este un subset al zile_sapt.')
else:
    print('weekend nu este un subset al zile_sapt')

"""
15. Afișează diferențele dintre aceste 2 seturi.
"""

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

print(zile_sapt.difference(weekend))

"""
16. Afișează intersecția elementelor din aceste 2 seturi.
"""

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

print(zile_sapt.intersection(weekend))


"""
PARTEA 2: CICLURI REPETITIVE

Exerciții - studiu în workshopul de weekend

17.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# v1: (for)

for i in range(0, len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

# v2: (for each)
for m in masini:
    print(f'Masina mea preferata e {m}')

# v3: (while)

k = 0
while k < len(masini):
    print(f'Masina mea preferata este {masini[k]}')
    k = k + 1

"""
18. Aceeași listă:
Folosește un for else
În for:
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for m in range(1, len(masini)):
    if m == masini[0] or m == len(masini) - 1:
        continue
    else:
        masini[m] = masini[m].upper()
else:
    print(masini)

"""
19. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""

masini = {'Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'}

for m in masini:
    if m == 'Mercedes':
        print('Am gasit masina aleasa de dvs')
        break
    else:
        print(f'Am gasit masina {m}. Mai cautam')

"""
20. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""

masini = {'Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'}

for m in masini:
    if m == 'Lastun' or m == 'Trabant':
         continue
    else:
        print(f'S-ar putea sa va placa masina {m}')

"""
21. Modernizează parcul de mașini: Crează o listă goală, masini_vechi. Iterează prin mașini. Când găsesti Lăstun sau
Trabant: Salvează aceste mașini în masini_vechi. Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x. Modele noi: x.
"""
# v1:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for m in masini:
    if m == 'Lastun' or m == 'Trabant':
         masini_vechi.append(m)
         masini.remove(m)
         masini.append('Tesla')
    else:
        continue
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# v2:

masini_vechi = []
for i in range(0, len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

"""
22. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină x
Iterează prin listă.
"""

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 11000,
    'Audi': 19000,
    'BMW': 23000
}

for masina, pret in pret_masini.items():
    print(masina, pret)
    if pret < 15_000:
        print(f'Pentru un buget de sub 15000 euro puteți alege mașina {masina}')
    else:
        print(f'Bugetul nu este suficient pentru a cumpara masina {masina}, care costa {pret}')

"""
23. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor_3 = []

for i in numere:
    if i == 3:
        contor_3.append(i)
print(len(contor_3))

"""
24. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum_nr = 0

for nr in numere:
    sum_nr += nr

print(sum_nr)

"""
25. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere.sort()
print(numere[-1])

i = numere[0]

for nr in numere:
    if i < nr:
        i = nr
print(i)

"""
26. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_inversate = []

for nr in numere:
    if nr > 0:
        nr = 0 - nr
        numere_inversate.append(nr)

print(numere_inversate)

"""
27.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for nr in alte_numere:
    if nr >= 0:
        numere_pozitive.append(nr)
    else:
        numere_negative.append(nr)
    if nr % 2 == 0:
        numere_pare.append(nr)
    else:
        numere_impare.append(nr)
print(f'{numere_impare}\n{numere_pare}\n{numere_negative}\n{numere_pozitive}')

"""
28. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
print(alte_numere)

for i1 in range(len(alte_numere)):
    for i2 in range(i1 + 1, len(alte_numere)):
        if alte_numere[i1] > alte_numere[i2]:
            alte_numere[i1], alte_numere[i2] = alte_numere[i2], alte_numere[i1]

print(alte_numere)

"""
29. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""

import random

x = random.randint(1, 30)

while x:
    y = int(input('Introdu un numar y: '))
    print(f'Numar secret = {x}')
    if y == x:
        print('Felicitări! Ai ghicit!')
    elif y > x:
        print('Nr secret e mai mic')
    else:
        print('Nr secret e mai mare')
    break

"""
30. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""

x = int(input('Da o valoare lui x: '))
i = 0
while i in range(x):
    i += 1
    print(str(i) * i)

"""
31.
tastatura_telefon =
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for rand in tastatura_telefon:
  for coloana in rand:
    print(f"Cifra curentă este {coloana}")


"""
Exerciții Recomandate - studiu individual                                        .

32. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.

33. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
Structuri de date 
Flow Control
"""