import random

# Definiramo konstante

ŠTEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZAČETEK = "S"
ZMAGA = "W"
PORAZ = "X" 

# Definiramo logični model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()              # String
        self.crke = [i.upper() for i in crke]   # List

    def napacne_crke(self):
        return [i for i in self.crke if i not in self.geslo]

    def pravilne_crke(self):
        return [i for i in self.crke if i in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for i in self.geslo:
            if i not in self.crke:
                return False
        return True
    
    def poraz(self):
        if len(self.napacne_crke()) >= ŠTEVILO_DOVOLJENIH_NAPAK:
            return True
        return False
    
    def pravilni_del_gesla(self):
        pravilni_del = self.geslo
        for i in self.geslo:
            if i not in self.crke:
                pravilni_del.replace(i, "_")
        return pravilni_del
    
    def nepravilni_ugibi(self):
        nepravilni = ""
        for i in self.napacne_crke():
            nepravilni += i + " "
        return nepravilni.strip()

    def ugibaj(self, crka):
        velika_crka = crka.upper()
        if not self.zmaga() and not self.poraz():
            if velika_crka not in self.geslo and velika_crka not in self.crke:
                self.crke.append(velika_crka)
                return NAPACNA_CRKA
            elif velika_crka in self.geslo and velika_crka not in self.crke:
                self.crke.append(velika_crka)
                return PRAVILNA_CRKA
            else:
                return PONOVLJENA_CRKA
        else:
            if self.zmaga() == True:
                return ZMAGA
            return PORAZ

bazen_besed = []

with open("besede.txt", "r", encoding="utf-8") as besede:
    for geslo in besede.readlines():
        bazen_besed.append(geslo.upper())
    
    
class Vislice():

    def __init__(self):
        # V slovarju igre ima vsaka igra svoj ID.
        # ID je celo število.
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            for i in range(len(self.igre) + 1):
                if i not in self.igre:
                    return i
    
    def nova_igra(self):    # Naredi novo igro z naključnim geslom
        self.igre[self.prost_id_igre()] = (ZAČETEK, Igra(random.choice(bazen_besed), []))

    def ugibaj(self, id_igre, crka):
        igrica = self.igre[id_igre][1]
        self.igre.update({id_igre : (igrica.ugibaj(crka), igrica)})
        