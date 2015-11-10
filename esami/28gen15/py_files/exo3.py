
def getCandidati(file):
    with open(file, "rb") as myFile:
        listaCandidati = []
        eta = []
        lines = myFile.readlines()
        for line in lines:
            tmp = line.split()
            listaCandidati.append(tmp[0])
            eta.append(tmp[1])

    return (listaCandidati, eta)


def getVoti(file):
    with open(file, "rb") as myFile:
        listaVoti = []
        lines = myFile.readlines()
        for voti in lines:
            tmp = voti.split()
            listaVoti.append(tmp[0])
    return listaVoti


def getVotiPerCandidato(lista_voti, lista_candidati):
    voti_per_candidati = []
    for i in range(len(lista_candidati)):
        voti_per_candidati.append(0)

    for voto in lista_voti:
        for i in range(len(lista_candidati)):
            if voto == lista_candidati[i]:
                voti_per_candidati[i] += 1

    return voti_per_candidati