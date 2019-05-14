from model import Igra, bazen_besed

import random

def izpis_igre(igra):
    if not igra.zmaga() and not igra.poraz():
        return "Nadaljujmo z igro."
    return None

def izpis_zmage(igra):
    if igra.zmaga():
        return "Zmagali ste!"
    return None

def izpis_poraza(igra):
    if igra.poraz():
        return "Izgubili ste. Poskusite novo igro."
    return None

def zahtevaj_vnos():
    return str(input("Napiši (na blef ugibano) črko: "))

def pozeni_vmesnik():
    print("Pozdravljen v igri VISLICE! Začnimo z igro.")
    igra = Igra(random.choice(bazen_besed), [])
    print("Geslo je določeno.")
    while True:
        print(igra.pravilni_del_gesla())
        crka = zahtevaj_vnos()
        izid_kroga = igra.ugibaj(crka)
        
        



