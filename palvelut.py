import random

class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__asiakasnro = self.__luo_nro()
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
        if nimi2 == "":
            raise ValueError("Uusi nimi kannattaa antaa UwU")
        else:
            self.__nimi = nimi2

    def set_ika(self, ika2):
        if ika2 != "":
            raise ValueError("Uusi ika kannattaa antaa UwU")
        else:
            self.__ika = ika2

    def get_ika(self):
        return self.__ika
 
class Palvelu:
    def __init__(self, tuotenimi=[]):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(Asiakas):
        return "f'{asiakas.get_nimi()} on asiakkaamme."

    def lisaa_asiakas(self, Asiakas):
        if Asiakas.get_nimi() == "" or Asiakas.get_ika() == "":
            raise ValueError("Uusi asiakas")
        else:
            self.__asiakkaat.append(Asiakas)


    def poista_asiakas(self, nimi):
        if nimi in self.__asiakkaat:
            self.__asiakkaat.remove(nimi)
        else:
            pass

    def tulosta_asiakkaat(self):
        for x in self.__asiakkaat:
            print("f'{asiakas.get_nimi()} on asiakkaamme.")
    



class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi, edut = []):
        super().__init__(tuotenimi)
        self.__edut = edut
        

    def lisaa_etu(self, etu):
        if etu == "":
            raise ValueError("Uusi asiakas")
        else:
            self.__asiakkaat.append(__edut(etu))

    def poista_etu(self, etu):
        if etu in self.__asiakkaat:
            self.__edut.remove(etu)
        else:
            pass

    def tulosta_edut(self, etu):
        for x in len(self.__asiakkaat) // 3:    
            print(f'{__edut.get_nimi()} on asiakkaamme.')
