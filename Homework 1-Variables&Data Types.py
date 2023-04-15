#EXERCITII OBLIGATORII
print('---Exercitiul 1---')
'''În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
O variabila este o cutie de memorie unde pot fi stocate valori'''
print('---Exercitiul 2---')
'''Declară și initializează câte o variabilă din fiecare din următoarele tipuri devariabilă :
- string
- int
- float
- bool'''
tara='Germania' #variabila string
populatie= 83 # variabila integer
nemti= 96.6 # variabila float
turci= True #variabila boolean
print('---Exercitiul 3---')
# Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
print(type(tara))
print(type(populatie))
print(type(nemti))
print(type(turci))
print('---Exercitiul 4---')
'''Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere),
apoi verifică din nou tipul de date al acesteia'''
nemti=round(nemti)
print(nemti)
print(type(nemti))
print('---Exercitiul 5---')
'''Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
 Rezolvă nepotrivirile de tip prin orice modalitate dorești (type casting, printare cu formatare).'''
print(f'{tara} este motorul economic al Europei')
print(f'{tara} are o populatie de aproximativ {populatie} miliioane de locuitori' )
print(f'{nemti} % din populatia tarii sunt nemti')
print(f'Is {turci} that turks have a lot of fast food shops in {tara}')
print('---Exercitiul 6---')
'''Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
 Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'''''
nume='Micle'
prenume='Florin'
print(f'Numele complet are {len(nume) + len(prenume)} caractere')
print('---Exercitiul 7---')
'''Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila
 Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.'''
lungime = int(input('Introdu lungimea '))
latime = int(input ('Introdu latimea '))
aria = lungime*latime
print(f'Aria dreptunghiului este de {aria}')
print('---Exercitiul 8---')
'''Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' 
în acest string'''
sentence = input('Introdu propozitia: ')
space_count = 1
for character in sentence:
    if character == "" :
        space_count = space_count + 1
number_of_words = space_count + 1
print('The user entered', sentence, sep =" ")
print ("The number of the in the sentence is", number_of_words, sep = " ")
prop ='Coral is either the stupidest animal or the smartest rock'
print(prop.count(' the '))
print('---Exercitiul 9---')
'''Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si 
afișează pe ecran rezultatul'''
prop ='Coral is either the stupidest animal or the smartest rock'
print(f'{prop.replace("the", "THE")}')
print('---Exercitiul 10---')
'''Același string.
 Folosiți un assert ca să verificați dacă acest string conține doar numere.'''
prop='Coral is either the stupidest animal or the smartest rock'
#assert prop.isdigit() is True,'Propozitia nu contine doar numere' - sterge # pentru a verifica assertul
#EXERCITII OPTIONALE
print('---Exercitiul 1---')
#Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
str = input('Introdu o variabila de tip string:')
print(f'Caracterul din mijloc este : {str[(len(str)//2)]}')
print('---Exercitiul 2---')
'''Folosind assert, verifică dacă un string este palindrom.
palindrom= cand inversezi un string, trebuie sa arate la fel ca si  stringul original'''
s = 'ana'
assert s == s[::-1],'Cuvantul nu este palindrom'
print('---Exercitiul 3---')
'''Citește un string format din 2 cuvinte de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.'''
text = input('Scrie un string:')
a,b = text.split(' ')
print(f'Primul cuvant este:{a}')
print(f'Ultimul cuvant este: {b}')
print('---Exercitiul 4---')
'''Citește un text format din 2 cuvinte de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.'''
text = input('Scrie un text:')
primul_caracter = text[0]
text_modificat = text [0] + text[1:-1].replace(primul_caracter,primul_caracter.capitalize()) + text[-1]
print(text)
print(text_modificat)
print('---Exercitiul 5---')
#citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere'
user = str (input('User-ul este:'))
parola = str (input('Introdu parola:'))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')