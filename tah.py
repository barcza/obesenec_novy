import opratka


zvolene_slovo = opratka.zvol_slovo()
#odpoved = input("Jaké zkusíš písmeno? ")

def over_delku(pismena):
    #chci, aby hráč zadal jen jedno písmeno
    if len(pismena) == 1:
        return True
    else:
        return False

def over_pismeno(cislo):
    #chci, aby zadal písmeno, ne číslo. jdu na to oklikou.
    #zkusím, jestli zadal číslo, potom je to ale špatně. když nezadal číslo, je to v pořádku.
    try:
        number = int(cislo)
    except ValueError:
        return True
    else:
        return False

def hledani(sluvko, pismenko):
    #prohledáme, jestli zadané písmenko je v tom vybraném řetězci
    if pismenko in sluvko:
        #když tam je, nahradíme podtržítko písmenkem

        seznam_pozic_pismene = []
        for i, char in enumerate(sluvko):
            #najdu, kde všude jsou ty stejné písmenka, musím vynásobit 2, protože v řetězci mám mezery, aby to bylo hezčí
            if char == pismenko:
                seznam_pozic_pismene.append(i * 2)

        for j in seznam_pozic_pismene:
            #podle seznamu nahradím na všech místech
            opratka.retezec = opratka.retezec[:j] + pismenko + opratka.retezec[j + 1:]

    else:
        #když to tam není, přidám na počítadlo chybu a vykreslím šibenici
        print("Ne, to tam není.")
        opratka.pocet_chyb += 1
        opratka.sibenice()

    print(opratka.retezec)

def opakovat():
    #zeptá se hráče, jestli chce hrát znovu. v takovém případě znovu zavolá funkci hra(), vynuluje slovo, řetězec i počet chyb
    znovu = input("Chceš si zahrát znovu? (ano/ne) ")
    if znovu == "ano":
        zvolene_slovo = opratka.zvol_slovo()
        opratka.retezec = "_ _ _ _ _"
        opratka.pocet_chyb = 0
        hra()
    elif znovu == "ne":
        print("Díky za hru!")
    else:
        print("Tak asi nechceš, že? Zdarec...")

def hra():
    #samotná hra, pokud tedy je volné místečko v řetězci
    while "_" in opratka.retezec:

        while True:
            #hráč zadá písmeno a pokud je to písmeno a jen jedno, jde dál, jinak zadává znovu
            pismenko = input("Jaké zkusíš písmeno? ")
            if over_delku(pismenko) and over_pismeno(pismenko) == True:
                break
            else:
                print("Chci po tobě jedno písmeno")

        #teď prohledáme to slovo, jestli tam písmeno je
        hledani(zvolene_slovo, pismenko)

        if opratka.pocet_chyb == 10:
            #když chybuje 10x, končí hra
            print("Sorry, už visíš. Zkus to znovu.")
            break

    if "_" not in opratka.retezec:
        #pokud není volné místečko v řetězci, znamená to, že vyhrál
        print("Gratulace, vyhrálas!")
        opakovat()
