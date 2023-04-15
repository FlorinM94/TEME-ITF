print(f'---ABSTRACTIZARE---')

'''Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’'''

from abc import ABC,abstractmethod
class FormaGeometrica(ABC):
    PI=3.14
    def descriere(self):
        print(f'Cel mai probabil am colturi')
    @abstractmethod
    def aria(self):
        pass

print(f'---MOSTENIRE---')

'''Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură'''

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura=latura
    def aria(self):
        return self.latura**2

print(f'----INCAPSULARE---')

'''latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)'''

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self._latura=latura
    @property
    def latura(self):
        return self._latura
    @latura.setter
    def latura(self,valoare):
        self._latura=valoare
    @latura.deleter
    def latura(self):
        del self._latura
    def aria(self):
        return self._latura**2
class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self._raza=raza
    @property
    def raza(self):
        return self._raza
    @raza.setter
    def raza(self,valoare):
        self._raza=valoare
    @raza.deleter
    def raza(self):
        del self._raza
    def aria(self):
        return self.PI * self.raza**2

print(f'---POLIMORFISM---')

'''Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui'''

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        super().__init__()
        self._latura=latura
    def aria(self):
        return self._latura
    def descriere(self):
        print(f'Cel mai probabil am colturi')

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self._raza=raza
    def aria(self):
        return self.PI*self._raza**2
    def descriere(self):
        print(f'Eu nu am colturi')
patrat=Patrat(10)
print('Aria patratului este:',patrat.aria())
patrat.descriere()

cerc=Cerc(10)
print(f'Aria cercului este:',cerc.aria())
cerc.descriere()