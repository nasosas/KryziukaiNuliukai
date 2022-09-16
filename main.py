from lenta import lentele, kieno_eile_zaist, tikrina

vietos = {1:"1", 2:"2", 3:"3",
          4:"4", 5:"5", 6:"6",
          7:"7", 8:"8", 9:"9",}


vyksta_zaidimas = True
eile_zaist = 0
paskutinis_ejimas = -1
zaidimas_baigtas = False

while vyksta_zaidimas:
    lentele(vietos)
    # jei pasirenka netinkama simboli
    if paskutinis_ejimas == eile_zaist:
        print("Netinkamas pasirinkimas")

    paskutinis_ejimas = eile_zaist

    print("Zaidejo " + str((eile_zaist % 2) + 1) +
          " eile: Pasirinkite vieta, arba paspauskite q kad isjungti zaidima")
    # gauna inputi is zaidejo
    pasirinkimas = input()
    if pasirinkimas == 'q':
        vyksta_zaidimas = False

    # checkina ar zaidejas pasirinko skaiciu nuo 1-9
    elif str.isdigit(pasirinkimas) and int(pasirinkimas) in vietos:
        # patikrina ar vieta jau buvo uzimta
        if not vietos[int(pasirinkimas)] in {"X", "O"}:
            # updatina boarda
            eile_zaist += 1
            vietos[int(pasirinkimas)] = kieno_eile_zaist(eile_zaist)

    if tikrina(vietos): vyksta_zaidimas, zaidimas_baigtas = False, True
    if eile_zaist > 8: vyksta_zaidimas = False

#pasako kas nugaletojas
if zaidimas_baigtas:
    if kieno_eile_zaist(eile_zaist) == 'O':
        print("Zaidejas 2 laimejo!")
    else:
        print("Zaidejas 1 laimejo!")
else:
    print("Lygiosios")
