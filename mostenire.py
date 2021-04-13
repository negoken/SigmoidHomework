


class Avion:
    def __init__(self, companie,ruta_de_zbor, ora_de_zbor):
        self.companie = companie
        self.ruta_de_zbor = ruta_de_zbor
        self.ora_de_zbor = ora_de_zbor

    def decoleazaAvionul(self):
        print("Avionul decoleaza")

    def aterizeazaAvionul(self):
        print("Si va ateriza la ora 12:30 PM!")
        print("---------------------------------")

class Boeing(Avion):
    def __init__(self,companie,ruta_de_zbor,numar_pasageri,ora_de_zbor):
        super().__init__(companie = companie, ruta_de_zbor = ruta_de_zbor, ora_de_zbor = ora_de_zbor)  # "super": cuvant cheie care permite accesarea variabilelor prima data din clasa Avion
        self.numar_pasageri = numar_pasageri

    def informatii_zbor(self):
        print("la ora " +self.ora_de_zbor + " apartinand companiei "+ self.companie, "Pe ruta "+ self.ruta_de_zbor, "cu un numar de "+ str(self.numar_pasageri) + " pasageri la bord")
        
class Airbus(Avion):
    def __init__(self,companie,ruta_de_zbor,numar_pasageri,ora_de_zbor ):
        super().__init__(companie = companie, ruta_de_zbor = ruta_de_zbor,ora_de_zbor = ora_de_zbor) 
        self.numar_pasageri = numar_pasageri

    def informatii_zbor1(self):
        print("la ora " + self.ora_de_zbor + " apartinand companiei "+ self.companie, "Pe ruta "+ self.ruta_de_zbor, "cu un numar de "+ str(self.numar_pasageri) + " pasageri la bord")






# instantierea clasei Boeing
tip_aeronava = Boeing("Lufthansa/KLM", "Londra-Paris" , 220,"11:00")
tip_aeronava1 = Airbus("Fly-Emirates", "Istanbul-Dubai" , 350,"15:30")
tip_aeronava.decoleazaAvionul()
tip_aeronava.informatii_zbor()
tip_aeronava.aterizeazaAvionul()

tip_aeronava1.decoleazaAvionul()
tip_aeronava1.informatii_zbor1()
tip_aeronava.aterizeazaAvionul()