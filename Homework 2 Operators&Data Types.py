#EXERCITII OBLIGATORII
print('---Exercitiul 1---')

'''Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
R:Instructiunea if executa un cod in caz ca conditia este adevarata si alt cod(cu ajutorul else) in caz care conditia nu
 este adevarata'''

print('---Exercitiul 2---')

'''Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
daca este numar intreg mai mare ca 0)'''

x=0
if x==int(x) and x>0:
    print('numar natural')
else:
    x!=int(x) and x<0
    print('nu este numar natural')

print('---Exercitiul 3---')

#Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if x>0:
    print('numar pozitiv')
elif x<0:
    print('numar negativ')
# numar netru pentru adunare si scadere este 0 iar pentru imultime/impartire este 1
else:
    print('numar neutru')

print('---Exercitiul 4---')

#Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

if x>=-2 and x<=13:
    print('True')
else:
    print('False')

print('---Exercitiul 5---')

'''Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs'''

x =10
y =2
if abs(x-y)<5:
    print('diferenta este mai mica de 5')
else:
    print('diferenta este mai mare de 5')

print('---Exercitiul 6---')

#Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

if not 5<=x<=27:
    print ('x nu este intre 5 si 27')
else:
    print('x este intre 5 si 27')

print('---Exercitul 7---')

'''Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
daca nu, afiseaza care din ele este mai mare'''

x=1
y=1
if x==y:
    print ('cele doua valori sunt egale')
elif x>y:
    print(x)
else:
    x<y
    print(y)

print('---Exercitiul 8---')

'''Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).'''

a= 4
b=6
c=6
if a==b==c:
    print('triunghi echilateral')
elif a!=b!=c:
    print('triunghi oarecare')
else:
    print('triunghi isoscel')

print('---Exercitiul 9---')

'''Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.'''

x= input (('Scrie o litera:'))
if x in ['a','e','i','o','u','A','E','O','U']:
    print('este vocala')
else:
    print('nu este vocala')

print('---Exercitiul 10---')

'''Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F'''

nota=int(input('scrie nota:'))
if nota>=9 and 0<=nota<=10:
    print('Ai primit nota A')
elif nota>=8 and 1<=nota<=10:
    print('Ai primit nota B')
elif nota>=7 and 1<=nota<=10:
    print('Ai primit nota C')
elif nota>=6  and 1<=nota<=10:
    print('Ai primit nota D')
elif nota>=4  and 1<=nota<=10:
    print('Ai primit nota E')
elif nota<4  and 1<=nota<=10:
    print('Ai primit nota F')
else:
    print('Notele trebuie sa fie intre 1 si 10')

#EXERCITII OPTIONALE

print('---Exercitiul 1---')

#Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x= 456
if len(str(x))>=4:
    print('numarul are minim 4 cifre')
else:
    print('numarul are mai putin de 4 cifre ')

print('---Exercitiul 2---')

#Verifica daca x are exact 6 cifre

if len(str(x))==6:
    print('numarul are 6 cifre')
else:
    print('numarul nu are 6 cifre')

print('---Exercitiul 3---')

#Verifica daca x este numar par sau impar

x=10
if x%2==0:
    print('este numar par')
else:
    print('este numar impar')

print('---Exercitiul 4---')

'''Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
ele'''

x=4
y=5
z=6
print(max(x,y,z))

print('----Exercitiul 5---')

'''Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)'''
#verificam daca suma unghiurilor este de 180 grade
x=90
y=50
z=40
if x+y+z==180 and x>0 and y>0 and z>0:
    print('este triunghi')
else:
    print('nu este triunghi')

print('---Exercitiul 6---')

'''Avand stringul: 'Coral is either the stupidest animal or the smartest rock'·
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'''
prop = 'Coral is either the stupidest animal or the smartest rock'
x = int (input('Introdu un numar:'))
print (prop[0:-x])

print('-Exercitiul 7---')

'''Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
din primele 5 caractere + ultimele 5'''

prop = 'Coral is either the stupidest animal or the smartest rock'
prop2 = prop[:5] + prop [-6:]
print('String nou:', prop2)

print('---Exercitiul 8---')

'''Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '''

prop = 'Coral is either the stupidest animal or the smartest rock'
prop_2 = prop.split()
print(prop_2)
prop_3 = prop_2[9]
print(prop_3)
print(prop_3[:1])
print(" ".join(prop_2[0:9]))

print('---Exercitiul 9---')

'''Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
functie pentru a face string-ul case insensitive)'''

s = input("Pune un string: ")
s = s.lower()
assert s[0] == s[-1], 'Primul si ultimul caracter sunt diferite'

print('---Exercitiul 10---')

'''Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
(hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)'''

string= '0123456789'
numere_pare= slice(0, None, 2)
print(string[numere_pare])
numere_impare= slice(1,None,2)
print(string[numere_impare])

#EXERCITII BONUS

print('---Exercitiul 1---')

'''Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca'''

yes = "y"
no = "n"
varsta = int(input("Introduceti varsta pasageriului: "))
pasaport = input("Pasaport valid? y/n = ")
insotit_de_mama = input("Insotit de mama? y/n = ")
insotit_de_tata = input("Insotit de tata? y/n = ")
act_permisiune_mama = input("Act permisiune mama? y/n = ")
act_permisiune_tata = input("Act permisiune tata? y/n = ")
if varsta >= 18 and pasaport == yes:
    print(f'Varsta {varsta} ani, am pasaport => Ma pot imbarca')
elif varsta >= 18 and pasaport == no:
    print(f'Varsta {varsta} ani, nu am pasaport => Nu ma pot imbarca ')
elif varsta < 18 and pasaport == no:
    print(f'Varsta {varsta} ani, nu am pasaport => Nu ma pot imbarca  ')
elif varsta < 18 and pasaport==yes and insotit_de_mama==yes or insotit_de_tata==yes and act_permisiune_mama==yes and act_permisiune_tata==yes :
    print(f'Varsta {varsta} ani, am pasaport , insotit de un parinte cu aprobarea ambilor parinti => Ma pot imbarca')
elif varsta < 18 and pasaport == yes and insotit_de_mama == no or insotit_de_tata == no and act_permisiune_mama == no or act_permisiune_tata == no:
    print(f'Varsta {varsta} ani, am pasaport , Neinsotit de parinti FARA aprobarea ambilor parinti => Nu ma pot imbarca ')
elif varsta < 18 and pasaport==yes and insotit_de_mama==yes or insotit_de_tata==yes and act_permisiune_mama==no or act_permisiune_tata==no :
    print(f'Varsta {varsta} ani, am pasaport , insotit de un parinte FARA aprobarea ambilor parinti => Nu ma pot imbarca ')
elif varsta < 18 and pasaport==yes and insotit_de_mama==no or insotit_de_tata==no and act_permisiune_mama==yes and act_permisiune_tata==yes :
    print(f'Varsta {varsta} ani, am pasaport , Neinsotit de parinti cu aprobarea ambilor parinti => Ma pot imbarca  ')
else:
    print("Date introduse incorecte SAU nu indeplinesc conditiile de calatorie => Nu ma pot imbarca")


