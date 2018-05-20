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

    if pocet_chyb <= 10:
        with open ("sib{0}.txt".format(pocet_chyb)) as opratka:
            for radek in opratka:
                print(radek, end="")

    else:
        raise ValueError("už visíš")
