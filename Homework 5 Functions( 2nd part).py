#EXERCITII OBLIGATORII
print('---Exercitiul 1---')

#Funcție care să calculeze și să returneze suma a două numere

def suma_numere(num1,num2):
    return num1 +num2

rezultat1= suma_numere(3,4)
print(f'Suma numerelor este {rezultat1}')

print('---Exercitiul 2---')
#Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def numar_par_impar(numar):
    if numar%2==0:
        return True
    else:
        return False
rezultat1=numar_par_impar(2)
print(rezultat1)
rezultat2=numar_par_impar(9)
print(rezultat2)

print('---Exercitiul 3---')

'''Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)'''

def nume_complet(nume,prenume1,prenume2):
    nume_complet=nume+prenume1+prenume2
    return len(nume_complet)

nume1=nume_complet('Micle','Florin','Ghita')
print(nume1)

print('---Exercitiul 4---')

#Funcție care returnează aria dreptunghiului

def aria(lungime,latime):
    aria= lungime*latime
    return (f' Aria dreptunghiului este {aria}')

dreptunghi1=aria(4,5)
print(dreptunghi1)

print('---Exercitiul 5---')

def aria_cerc(raza):
    return 3.14 *(raza**2)

cerc1= aria_cerc(10)
print(cerc1)
cerc2=aria_cerc(5)
print(cerc2)

print('---Exercitiul 6---')

'''Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.'''

def isstring(string,caracter):
    if caracter in string:
        return True
    else:
        return False
rezultat1= isstring('mere','e')
print(rezultat1)
rezultat2= isstring('mere','z')
print(rezultat2)

print('---Exercitiul 7---')

'''Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y'''

def caractere_mari_mici(string):
    caractere_mici = 0
    caractere_mari = 0
    for char in string:
        if char.islower():
            caractere_mici += 1
        elif char.isupper():
            caractere_mari += 1
    return (f'Numarul caracterelor mici este {caractere_mici} si numarul caracterelor mari este {caractere_mari}')

rezultat1=caractere_mari_mici('flORin')
print(rezultat1)
rezultat2=caractere_mari_mici('Masina mea Este alBa')
print(rezultat2)

print('---Exercitiul 8---')

'''Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive'''

def lista_numere_pozitive(numere):
    lista_numere_pozitive=[]
    for x in numere:
        if x > 0:
            lista_numere_pozitive.append(x)
    return lista_numere_pozitive

numere = [-2, -1, 0, 1, 2,15,65,44,909]
lista_numere_pozitive =lista_numere_pozitive(numere)
print(lista_numere_pozitive)

print('---Exercitiul 9----')

'''Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.'''

def numere(x,y):
    if x==y:
        return(f'Cele doua numere sunt egale')
    elif x>y:
        return(f'Primul numar: {x} este mai mare decat al doilea: {y}')
    elif x<y:
        return(f'Primul numar: {x} este mai mic decat al doilea: {y}')

comparare_numere1=numere(2,3)
print(comparare_numere1)
comparare_numere2=numere(6,5)
print(comparare_numere2)
comparare_numere3=numere(3,3)
print(comparare_numere3)

print('---Exercitiul 10---')

'''Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False'''

set_numere={1,8,5,45,32,666,32}
def adaugare_numar(set_numere,x):
    if x not in  set_numere:
        print(f'Am adaugat numarul {x} in setul de numere ')
        return True
    elif x in set_numere:
        print(f'Numarul {x} este deja in setul de numere')
        return False
print(adaugare_numar(set_numere,8))
print(adaugare_numar(set_numere,199))

#EXERCITII OPTIONALE
print('---Exercitiul 1---')

#Funcție care primește o lună din an și returnează câte zile are acea luna

def zilele_lunii(luna):
    lunile_anului = {'Ianuarie': 31,
                  'Februarie': 28,
                  'Martie': 31,
                  'Aprile': 30,
                  'Mai': 31,
                  'Iunie': 30,
                  'Iulie': 31,
                  'August': 31,
                  'Septembrie': 30,
                  'Octobrie': 31,
                  'Noiembrie': 30,
                  'Decemberie': 31}

    if luna in lunile_anului:
        return lunile_anului[luna]
    else:
        return 'No valid month'

print(zilele_lunii('Februarie'))
print(zilele_lunii('Martie'))

print('---Exercitiul 2---')

'''Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)

● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)'''

def calculator(nr1, nr2):
    suma = nr1 + nr2
    diferenta = nr1 - nr2
    inmultirea = nr1 * nr2
    impartirea = nr1 / nr2
    return suma, diferenta, inmultirea, impartirea
a, b, c, d = calculator(50,40)
print("12.Suma: ", a)
print("   Diferenta: ", b)
print("   Inmultirea: ", c)
print("   Impartirea: ", d)

print('---Exercitiul 3---')

'''Funcție care primește o lista de cifre (adică doar 0-9)
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
}'''

def count_nr(lista):
    dict ={}
    for nr in range(10):
        dict[nr] =0
    for nri in lista:
        dict[nri] +=1
    return dict
lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(f'13.DICT de câte ori apare nr: {count_nr(lista)}')

print('---Exercitiul 4---')

#Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def val_max(a,b,c,):
    max_val = a
    if b > max_val:
        max_val=b
    if c > max_val:
        max_val = c
    return max_val
print(f'14. Val. max. a trei numere(1,2,3): {val_max(1, 2, 3)}')

print('---Exercitiul 5---')

'''Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)'''

def suma_pana_la(numar):
    suma = 0
    for i in range(numar+1):
        suma += i
    return suma
print(f'15.Suma de nr. 4: {suma_pana_la(4)}')

