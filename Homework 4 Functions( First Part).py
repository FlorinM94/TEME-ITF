#EXERCITII OBLIGATORII
print('---Exercitiul 1---')

'''Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.'''

masini=['Audi','BMW','Mercedes','Ashton Martin','Lastun','Fiat','Trabant','Opel']
print('---Folosind functia FOR---')
for x in range(len(masini)):
    print(f'Masina mea preferata este'+masini[x])
else:
    print('Nu am gasit masina mea preferata')

print('---Folosind functia FOR EACH---')

for x in masini:
    print('Masina mea prederata este' + x)


print('---folosind WHILE---')

x=0
while x<len(masini):
    print('Masina mea preferata este '+ masini[x])
    x += 1
else:
    print('Nu am gasit masina masina mea preferata')

print('---Exercitiul 2---')

'''Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
În else:
Printează lista.'''

masini=['Audi','BMW','Mercedes','Ashton Martin','Lastun','Fiat','Trabant','Opel']
for i in range(1,len(masini)-1):
    masini[i]=masini[i].upper()
else:
    print(masini)

print('---Exercitiul 3---')

'''Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘'''

masini=['Audi','BMW','Mercedes','Ashton Martin','Lastun','Fiat','Trabant','Opel']
for x in masini:
    if x=='Mercedes':
        print('Am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {x}.Mai cautam')

print('---Exercitiul 4---')

'''Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.'''

for x in masini:
    if x=='Trabant' or x=='Lastun':
        continue
    else:
        print(f'S-ar putea sa va placa masina {x}')

print('---Exercitiul 5---')

'''Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.'''

masini_vechi = []
for x in range(len(masini)):
    if masini[i] == 'Lăstun' or masini[x]=='Trabant':
        masini_vechi.append(masini[x])
        masini[x] = "Tesla"
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

print('---Exercitiul 6---')

'''ine un client cu un buget de 15000 euro.
Prezintă doar mașinile care se încadrează în acest buget.
Itereaza prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
Iterează prin listă.'''

pret_masini={'Dacia':6800,'Lastun':500,'Opel':1100,'Audi':19000,'BMW':23000}
buget=15000
for x in pret_masini:
    if pret_masini[x]<=buget:
        print(f'Pentru un buget de sub {buget} puteti alege masina {x}')

print('---Exercitiul 7---')

'''Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

numere=[5,7,3,9,3,3,1,0,-4,3]
for x in numere:
    if x==3:
        x+=1
        print(f'Numarul 3 apare de {x} ori in lista')

print('---Exercitiul 8---')

'''Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''

s=0
for x in range(0,len(numere)):
    s=s+numere[x]
    print(f'Suma numerelor din lista este {s} ')

print('---Exercitiul 9---')

'''Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).'''

max=0
for x in numere:
    if x>max:
        max=x
        print(f'Cel mai mare numar din lista este {max}')

print('---Exercitiul 10---')

'''Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.'''

for i in range(len(numere)):
    if numere[i]>0:
        numere[i]=numere[i]*-1
print(f'numerele listei sunt: {numere}')

#EXERCITII OPTIONALE

print('---Exercitiu 1---')

'''alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pozitive = []
numere_negative = []
numere_pare = []
numere_impare = []
for i in alte_numere:
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
print(alte_numere)
print(numere_impare)
print(numere_pare)
print(numere_pozitive)
print(numere_negative)

print('---Exercitiul 2---')

'''Aceeași listă:
Ordonează crescător lista fară să folosești sort.'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for x in range(len(alte_numere)):
    for y in range(x+1,len(alte_numere)):
        if alte_numere[x]>alte_numere[y]:
            alte_numere[x], alte_numere [y] = alte_numere[y], alte_numere[x]
print(f'Lista ordonata:{alte_numere}')

print('---Exercitiul 3---')

'''Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!'''

import random
n_secret = random.randint(1,30)
n_alese = 0
n_ghicit = None

print(f'Ma gandesc la un nr intre 1 si 30.')

while n_alese < 30:
    print('Ghiceste: ')
    n_ghicit = int(input())
    n_alese +=1
    if n_ghicit < n_secret:
        print('Nr ales este prea mic')
    if n_ghicit > n_secret:
        print('Nr. ales este prea mare')
    if n_ghicit == n_secret:
        break
if n_ghicit == n_secret:
    print(f' Ai ghicit numarul secret,era {n_secret} . Felicitari!')
else:
    print(f'Ai pierdut, numarul ales de mine era {n_secret}')