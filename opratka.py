from random import choice


#úvodní nastavení: prázdný řetězec a žádné chyby
retezec = "_ _ _ _ _"

pocet_chyb = 0

def zvol_slovo():
    #seznam, ze kterého zvolíme slovo
    slovo = ["balon", "zubař", "opice", "parno", "želva", "dveře", "kočka", "ratan", "ježek", "lelek"]
    return choice(slovo)

def sibenice():
    #obrázky, které to vykreslí, když se bude navyšovat počet chyb

    if pocet_chyb == 1:
        with open("sib1.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 2:
        with open("sib2.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 3:
        with open("sib3.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 4:
        with open("sib4.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 5:
        with open("sib5.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 6:
        with open("sib6.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 7:
        with open("sib7.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 8:
        with open("sib8.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 9:
        with open("sib9.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    elif pocet_chyb == 10:
        with open("sib10.txt") as opratka:
            for radek in opratka:
                print(radek, end="")
    else:
        raise ValueError("už visíš")
