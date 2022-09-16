
def lentele(vietos):
    lenta = (f"|{vietos[1]}|{vietos[2]}|{vietos[3]}|\n"
             f"|{vietos[4]}|{vietos[5]}|{vietos[6]}|\n"
             f"|{vietos[7]}|{vietos[8]}|{vietos[9]}|")
    print(lenta)


def kieno_eile_zaist(eile_zaist):
    if eile_zaist % 2 == 0:
        return 'O'
    else:
        return 'X'


def tikrina(vietos):
    if (vietos[1] == vietos[2] == vietos[3]) \
      or (vietos[4] == vietos[5] == vietos[6]) \
      or (vietos[7] == vietos[8] == vietos[9]):
        return True

    elif (vietos[1] == vietos[4] == vietos[7]) \
        or (vietos[2] == vietos[5] == vietos[8]) \
        or (vietos[3] == vietos[6] == vietos[9]):
        return True

    elif (vietos[1] == vietos[5] == vietos[9]) \
            or (vietos[3] == vietos[5] == vietos[7]):
        return True
    else:
        return False
