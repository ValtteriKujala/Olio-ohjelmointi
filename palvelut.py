import random

class Asiakas:
    def __int__(self, nimi, ika):
        self.__nimi = nimi
        self.__asiakasnro = luo_nro()
        self.__ika = ika

    def __luo_nro(self):
        kikel1 = random.randint(0, 9)
        kikel2 = random.randint(0, 9)
        kikel3 = random.randint(0, 9)
        kikel4 = random.randint(0, 9)
        kikel5 = random.randint(0, 9)
        kikel6 = random.randint(0, 9)
        kikel7 = random.randint(0, 9)
        kikel8 = random.randint(0, 9)
        return f'{kikel1}{kikel2}-{kikel3}{kikel4}{kikel5}-{kikel6}{kikel7}{kikel8}'   

    def get_asiakasnumero(self):
        return self.__asiakasnro
 
    def get_nimi(self):
        return self.__nimi
 
    def get_ika(self):
        return self.__ika
    
    def set_nimi(self, nimi2):
        nimi2 = nimi2
        if nimi2 == "":
            raise ValueError("Uusi nimi kannattaa antaa UwU")
        else:
            self.__nimi = nimi2

    def set_ika(self, ika2):
        ika2 = ika2
        if ika2 != "":
            raise ValueError("Uusi ika kannattaa antaa UwU")
        else:
            self.__ika = ika2

    def get_ika(self):
        return self.__ika

    def __luo_nro():
        pass
 
class Palvelu(Asiakas):
    def __int__(self, tuotenimi=[]):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(Asiakas):
        pass

    def lisaa_asiakas(self, nimi, ika):
        if nimi or ika == "":
            raise ValueError("Uusi asiakas uwu meow woof woof")
        else:
            self.__asiakkaat.append(Asiakas(nimi, ika))


    def poista_asiakas(Asiakas):
        pass

    def tulosta_asiakkaat():
        pass
    



class ParempiPalvelu(Palvelu):
    def __init__(self):
        self.__edut = []
        self.tuotenimi = super().__init__(tuotenimi)

    def lisaa_etu(__edut):
        pass

    def poista_etu(__edut):
        pass

    def tulosta_edut():
        pass
