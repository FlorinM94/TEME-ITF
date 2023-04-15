#EXERCITII OBLIGATORII
print('---Exercitiul 1---')

'''Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială'''

musical_notes=['do','re','mi','fa','sol','la','si','do']
print(musical_notes)
musical_notes = musical_notes[::-1]
print(musical_notes)
musical_notes = ['do','re','mi','fa','sol','la','si','do']
musical_notes.reverse() #inversare
print(musical_notes)

print('---Exercitiul 2---')

#Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

print(musical_notes.count('do'))

print('---Exercitiul 3---')

#Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

list1=[3,1,0,2]
list2=[6,5,4]
list1.extend(list2)
print(list1)

print('---Exercitiul 4---')

'''Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
folosind o functie si apoi afiseaza din nou lista'''

list1.sort()
print(list1)
list1.pop(0)
print(list1)

print('---Exercitiul 5---')

'''Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)'''

if  len(list1)==0:
    print('lista este goala')
else:
    print('lista nu este goala')

print('---Exercitiul 6---')

#Foloseste o functie care sa goleasca lista de la exercitiul 3

list1.clear()

print('---Exercitiul 7---')

'''Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
afiseze ca lista e goala'''

if  len(list1)==0:
    print('lista este goala')
else:
    print('lista nu este goala')

print('---Exercitiul 8---')

'''Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
afisezi Elevii (cheile)'''

clasa5={
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
for key in clasa5.keys():
    print(key)

print('---Exercitiul 9---')

'''Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie'''

nota_ana=str(clasa5['Ana'])
nota_gigel=str(clasa5['Gigel'])
nota_dorel=str(clasa5['Dorel'])
print('Ana a luat nota '+ nota_ana)
print('Gigel a luat nota '+ nota_gigel)
print('Dorel a luat nota '+ nota_dorel)

print('---Exercitiul 10---')

'''Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
- Modifica nota lui Dorel in 6
- Printeaza nota lui dupa modificare'''

clasa5['Dorel']= 6
print(clasa5)

print('---Exercitiul 11---')

'''Imagineaza-ti ca Gigel se transfera din clasa.
- Cauta o functie care sa il stearga
Vine un coleg nou.
- Adaugati-l in lista pe Ionica, cu nota 9
- Printati dictionarul cu noii elevi'''

clasa5.pop('Gigel')
clasa5['Ionica']=9
print(clasa5)

print('---Exercitiul 12---')

'''Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.'''

zile_saptamana={'luni','marti','miercuri','joi','vineri','sambata','duminica'}
weekend={'sambata','duminica'}
#adaugam ziua de luni in setul cu zilele saptamanii si printam din nou setul
zile_saptamana.add('luni')
print(zile_saptamana)
# concluzie in seturi nu se pot folosi valori dublate

print('---Exercitiul 13---')

'''Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt'''

if weekend.issubset(zile_saptamana):
    print(True)
else:
    print(False)

print('---Exercitiul 14---')

'''Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
sunt in weekend si invers)'''

diferenta_seturi1=zile_saptamana.difference(weekend)
print(diferenta_seturi1)
diferenta_seturi2=weekend.difference(zile_saptamana)
print(diferenta_seturi2)

print('---Exercitiul 15---')

'''Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
ambele seturi)'''

print(weekend.intersection(zile_saptamana))

print('---Exercitiu Optional---')

'''Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’'''

lista_jucatori_teren=['j1', 'j2','j3','j4','j5']
lista_jucatori_rezerva=['r1', 'r2','r3','r4','r5']
lista_jucatori_scosi=[]
Schimbari_efectuate=int(input('Nr. schimbari efectuate: '))
SCHIMBARI_MAX=3
if input('Introduceti jucatorul pe care vreti sa il scoateti de pe teren: ') in lista_jucatori_teren and Schimbari_efectuate <3:
    print(input('Scrieti jucatorul pe care vreti sa il introduceti pe teren'))
if (input('Scrieti jucatorul pe care vreti sa il introduceti pe teren: ')) in lista_jucatori_rezerva:
    Schimbari_efectuate +=1
    print(f' Numarul de schimbari este: {Schimbari_efectuate}')
