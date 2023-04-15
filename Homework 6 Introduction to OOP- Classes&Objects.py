print('---Exercitiul 1---')

'''Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()'''

class Cerc:
    def __init__(self,raza,culoare):
        self.raza=raza
        self.culoare=culoare
    def descriere_cerc(self):
        print(f'Cercul are raza de',self.raza, 'si culoareaa' ,self.culoare)
    def aria(self):
        return 3.14*(self.raza*self.raza)
    def diametru(self):
            return self.raza*2
    def circumferinta(self):
        return 2*3.14*self.raza

c1=Cerc(8,'rosu')
print(c1.descriere_cerc())
print(c1.aria())
print(c1.circumferinta())
print(c1.diametru())

print('---Exercitiul 2---')

'''Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().'''

class Dreptunghi:
    def __init__(self,lungime,latime,culoare):
        self.lungime=lungime
        self.latime=latime
        self.culoare=culoare
    def descriere(self):
        print(f'Dreptunghiul are lungimea de',self.lungime,'latimea de',self.latime,'si culoarea',self.culoare)
    def aria(self):
        return self.lungime*self.latime
    def perimetru(self):
        return 2*(self.lungime+self.latime)
    def schimba_culoare(self,culoare_noua):
        self.culoare=culoare_noua
d1=Dreptunghi(5,6,'albastru')
d1.descriere()
print(d1.aria())
print(d1.perimetru())
d1.schimba_culoare('verde')

print('---Exercitiul 3---')

'''Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)'''

class Angajat:
    def __init__(self,nume,prenume,salariu):
        self.nume=nume
        self.prenume=prenume
        self.salariu=salariu
    def descriere(self):
        print('Angajatul',self.nume,self.prenume,'are un salariu de',self.salariu,'lei')
    def nume_complet(self):
        return self.nume+self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return  self.salariu*12
    def marire_salariu(self,procent):
         self.salariu+=self.salariu*procent/100
         print(f'Salariul angajatului {self.nume} {self.prenume} a fost marit cu {procent}%. Noul salariu este {self.salariu} lei')
angajat1=Angajat('Micle','Florin',8000)
angajat1.descriere()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
angajat1.marire_salariu(20)

print('---Exercitiul 4---')

'''Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''

class Cont:
    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold
    def afisare_sold(self):
        print(f' Titularul',self.titular_cont,'are in contul',self.iban,'suma de',self.sold,'lei')
    def debitare_cont(self,suma_debitata,):
        sold_nou=self.sold-suma_debitata
        if suma_debitata<=self.sold:
            print(f'Contul dumneavoastra a fost debitat cu suma de',suma_debitata,'lei.Noul sold este de',sold_nou,'lei')
        else:
            print('Fonduri insuficiente')
    def creditare_cont(self,suma_creditata):
        sold_nou=self.sold+suma_creditata
        return print('Contul dumneavoastra a fost creditat cu suma de',suma_creditata,'.Noul sold este de',sold_nou,'lei')
cont1=Cont('RO76RNCB0301XXXXXXXX0001','Florin Micle',10000)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.creditare_cont(800)

print('---Exercitiul Optional 1---')

'''Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000'''

class Factura:
    seria='MFG'
    def __init__(self,numar,nume_produs,cantitate,pret_buc):
        self.numar=numar
        self.nume_produs=nume_produs
        self.cantitate=cantitate
        self.pret_buc=pret_buc
    def schimba_cantitatea(self,cantitate):
        self.cantitate=cantitate
    def schimba_pretul(self,pret):
        self.pret_buc=pret
    def schimba_nume_produs(self,nume):
        self.nume_produs=nume
    def total(self):
        return self.cantitate*self.pret_buc
    def generare_factura(self):
        from datetime import date
        today=date.today()
        total=self.cantitate*self.pret_buc
        print(f'Factura are seria',self.seria,'si numarul',self.numar)
        print(f'Data:',today)
        table = [['Produs', 'Cantitate', 'pret bucata', 'total'],
                 [self.nume_produs, self.cantitate, self.pret_buc, Factura.total(self)]]
        for row in table:
            print('| {:1} | {:^4} | {:>4} | {:<3} |'.format(*row))
factura1= Factura(6,'Televizor',4,2500)
factura1.generare_factura()
factura1.schimba_cantitatea(6)
factura1.schimba_pretul(2000)
factura1.schimba_nume_produs('Telefon')
factura1.generare_factura()

print('---Exercitiul Optional 2---')

'''Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0'''

class Masina:
    culoare_initiala='gri'
    viteza_actuala=0
    culori_disponibile=['rosu','albastru','verde','portocaliu','negru','alb']
    marca='Skoda'
    inmatriculata=False
    def __init__(self,model,viteza_maxima):
        self.model=model
        self.viteza_maxima=viteza_maxima
    def descrie(self,):
        print(f'Masina are marca',self.marca)
        print(f'Vitzeza actuala a masinii este de',self.viteza_actuala,'km/h')
        print(f'In momentul acesta masina are culoarea',self.culoare_initiala)
        print(f'Marca masinii este',self.marca)
        print(f'Masina este inmatriculata?',self.inmatriculata)
    def inmatriculare_masina(self):
        self.inmatriculata=True
        return (f'Masina a fost inmatriculata')
    def vopeste_masina(self,culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare_initiala=culoare_noua
            print('Masina a fost vopsita in culoarea',culoare_noua)
        else:
            print('Culoare aleasa nu este disponibila')
    def acelereaza(self,viteza):
        if viteza >0 and viteza > self.viteza_maxima:
            self.viteza_actuala=self.viteza_maxima
        elif viteza >0 and viteza < self.viteza_maxima:
            self.viteza_actuala = viteza
        elif viteza < 0:
            print('Viteza trebuie sa aiba valori pozitive ')

    def franeaza(self):
        self.viteza_actuala=0
masina1=Masina('Octavia',280)
masina1.descrie()
print(masina1.inmatriculare_masina())
masina1.vopeste_masina('negru')
masina1.acelereaza(-100)
masina1.franeaza()

print('---Exercitiul Optional 3---')

'''Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict'''

class TodoList:
    todo={}
    def adauga_task(self,nume,descriere):
        self.todo[nume]=descriere
    def finalizeaza_task(self,nume):
        self.todo.pop(nume)
    def afiseaza_todo_list(self):
        print(self.todo.keys())
    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task in self.todo.keys():
            print(self.todo.values())
        else:
            print('Do you want to add this task to your list ? ')
            raspuns = bool(input(
                ''))
            if raspuns is False:
                print('Nu ai un task adaugat!')
            else:
                detalii = input('Descrierea task-ului ')
                self.todo[nume_task] = detalii
                print(self.todo)

todolist1 = TodoList()
todolist1.adauga_task('depoziteaza marfa', 'aranjeaza marfa pe rafturi')
todolist1.adauga_task('stai la caserie', 'ia-ti pauza de masa ')
todolist1.finalizeaza_task('depoziteaza marfa')
todolist1.afiseaza_todo_list()
todolist1.afiseaza_detalii_suplimentare('depoziteaza marfa venita cu o zi anterioara in depozitul C conform instructiunilor deja trimise ')