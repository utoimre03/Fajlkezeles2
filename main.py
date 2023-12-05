import Csoport

adatokListaja = []
def beolvasas():
    beFile = open("csoport.txt", "r", encoding="UTF-8")
    # első sor
    beFile.readline()
    # többi sor
    sorok = beFile.readlines()
    # print(sorok)
    for sor in sorok:
        #adat tisztítás
        tisztitottsor = sor.strip()
        #eldarabolom
        daraboltsor = tisztitottsor.split("/")
        # print(daraboltsor)
        # példányosítok
        csoporttag = Csoport.Csoport(daraboltsor[0], daraboltsor[1], daraboltsor[2])
        # print(csoporttag)
        # belefűzöm az objektumot a listába
        adatokListaja.append(csoporttag)
    beFile.close()

def kiir():
    for index in range(0, len(adatokListaja), 1):
        print(adatokListaja[index])
        # print(adatokListaja[index].nev+" "+adatokListaja[index].evfolyam+" "+adatokListaja[index].atlag)

def sorokSzama():
    sorszam = len(adatokListaja)
    print(f"A sorok tanulók száma: {sorszam}")

def megszamlalas():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
        osszeg += adatokListaja[index].atlag
    if len(adatokListaja) == 0:
        atlag = 0
    else:
        atlag = osszeg/len(adatokListaja)
        print(f"A suli átlag: {atlag}")

def elsosokSzama():
    db = 0
    for index in range(0, len(adatokListaja), 1):
        if adatokListaja[index].evfolyam == 1:
            db += 1
    print(f"Az elsősök száma: {db}")

# főprogram
beolvasas()
kiir()
sorokSzama()
megszamlalas()
elsosokSzama()