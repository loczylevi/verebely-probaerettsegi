"""Ahol az adatok rendre a következők:
A küldetés kódja (pl.: STS-50),
az űrsikló kilövésének dátuma (pl.: 1992.06.25),
a küldetést végző űrsikló neve (pl.: Columbia),
hány napot (pl.: 13)
és hány órát (pl.: 19) töltött a sikló földön kívül a küldetés alatt,
a légitámaszpont neve, ahol a sikló a küldetés végeztével landolt (pl.: Kennedy),
mekkora legénységgel szállt fel a sikló (pl.: 7)
"""

class Space:
    def __init__(self,sor):
        kod,datum,nev,nap,ora,landolt,crew = sor.strip().split(";")
        self.kod = kod
        self.datum = datum
        self.nev = nev
        self.nap = int(nap)
        self.ora = int(ora)
        self.landolt = landolt
        self.crew = int(crew)
        self.ev = int(datum[0:4])

with open("kuldetesek.csv","r",encoding="UTF-8") as f:
    lista = [Space(sor) for sor in f]
    
    
print(f"""3.feladat:
       Összesen {len(lista)} alkalommal inditottak űrhajot.""")

osszes_utas = sum([sor.crew for sor in lista])

print(f"""4.feladat:
       {osszes_utas} utas indult az űrbe összesen.""")

ot_fovel_vilagurben = len([sor for sor in lista if sor.crew < 5])

print(f"""5.feladat:
        Összesen {ot_fovel_vilagurben} alkalommal küldtek kevesebb, mint 5 embert az űrbe.""")

utolso_ut_columbia = [sor.crew for sor in lista if sor.nev == "Columbia"][-1]

print(f"""6.feladat:
        {utolso_ut_columbia} asztronatua volt a Columbia fedélzetén annak utolsó útján""")

#orak_nagy = max([(sor.ora + sor.nap*24,) for sor in lista])[0]

nagy = 0
nev = ""
kod = ""
for sor in lista:
    orak = sor.ora + sor.nap * 24
    if orak > nagy:
        nagy = orak
        nev = sor.nev
        kod = sor.kod
        
print(f"""7.feladat: 
         A leghosszabb ideig a {nev} volt az űrben a {kod} küldetés során.
         Összesen {nagy} órát volt távol a Földtől""")

print("8.feladat:")
bekeres = int(input("         Évszám: "))

x_evben_x_kuldetes = len([sor for sor in lista if sor.ev == bekeres])

if x_evben_x_kuldetes:
    print(f"         Ebben az évben {x_evben_x_kuldetes} küldetés volt.")
else:
    print("         Ebben az évben nem indult küldetés")
    
kennedy = len([sor for sor in lista if sor.landolt == "Kennedy"])
ossz = len([sor.landolt for sor in lista])

szazalek = kennedy / ossz
szazalek = str(szazalek)

tarolo = ""
szamlalo = 0
mehet = False
for karakter in szazalek:
    if karakter == ".":
        mehet = True
    if mehet == True and karakter != ".":
        tarolo = tarolo + karakter
        szamlalo += 1
        if szamlalo == 4:
            break

tarolo2 = ""
szamlalo2 = 0
for karakter in tarolo:
    szamlalo2 += 1
    tarolo2 += karakter
    if szamlalo2 == 2:
        tarolo2 = tarolo2 + "."
        
tarolo6 = ""
szamlalo7 = 0
if int(tarolo2[-1]) >= 5:
    for sor in tarolo2:
        szamlalo7 += 1
        tarolo6 += sor
        if szamlalo7 == 4:
            tarolo6 += str(int(tarolo2[-1]) + 1)
            break
tarolo6 = str(tarolo6).replace('.',',')
print(f"""9.feladat:
         A küldetések {tarolo6}%-a fejeződött be az Kennedy űrközpontban.""")



columbia = sum([(sor.ora + sor.nap * 24) for sor in lista if sor.nev == "Columbia"])
n_comulbia = columbia / 24

challanger = sum([(sor.ora + sor.nap * 24) for sor in lista if sor.nev == "Challenger"])
n_challanger = challanger / 24

discovery = sum([(sor.ora + sor.nap * 24) for sor in lista if sor.nev == "Discovery"])
n_discovery = challanger / 24

Atlantis = sum([(sor.ora + sor.nap * 24) for sor in lista if sor.nev == "Atlantis"])
n_Atlantis = Atlantis / 24

Endeavour = sum([(sor.ora + sor.nap * 24) for sor in lista if sor.nev == "Endeavour"])
n_Endeavour = Endeavour / 24

with open("ursiklok.txt","w",encoding="latin2") as f2:
    f2.write(f"Columbia      {n_comulbia:.2f}\n")
    f2.write(f"Challanger      {n_challanger:.2f}\n")
    f2.write(f"Discovery      {n_discovery:.2f}\n")
    f2.write(f"Atlantis      {n_Atlantis:.2f}\n")
    f2.write(f"Endeavour      {n_Endeavour:.2f}\n")