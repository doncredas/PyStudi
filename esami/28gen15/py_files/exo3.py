
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


if __name__=="__main__":
    candidati = ()

    #1)leggere i 2 file e caricare i dati  su una struttura dati adeguata.

    candidati = getCandidati("candidati.txt")
    #Lista dei voti
    lista_voti = getVoti("voti.txt")
    #Lista dei candidati
    lista_candidati = candidati[0]
    #Lista del loro eta
    lista_eta = candidati[1]
    #voti per candidato
    voti_per_candidato = getVotiPerCandidato(lista_voti, lista_candidati)

    # 2) Stampare le eta e il nome dei candidati che hanno preso piu di 100 voti, in ordine alfabetico di nome.
    listaPiuDi100 = []
    for i in range(len(lista_candidati)):
        if voti_per_candidato[i] > 100:
            listaPiuDi100.append((lista_candidati[i], lista_eta[i], voti_per_candidato[i]))

    listaPiuDi100.sort()
    for lista in listaPiuDi100:
        print lista[0], "con eta", lista[1], "ha preso", lista[2], "voti!"

    # 3) Stampare le fasce di voti (considerando le fasce "<20", "21-50", "51-100" ">100"),
    # seguite dal nome dei  candidati appartenti a quella fascia ordinati per eta decrescente e,
    # a parita di eta, per voti decrescenti.

    listaFascia1 = []  # "<20"
    listaFascia2 = []  # "21-50"
    listaFascia3 = []  # "51-100"
    listaFascia4 = []  # ">100"

    for i in range(len(lista_candidati)):
        if voti_per_candidato[i] <= 20:
            listaFascia1.append((lista_candidati[i], lista_eta[i], voti_per_candidato[i]))
        elif 21 <= voti_per_candidato[i] <= 50:
            listaFascia2.append((lista_candidati[i], lista_eta[i], voti_per_candidato[i]))
        elif 51 <= voti_per_candidato[i] <= 100:
            listaFascia3.append((lista_candidati[i], lista_eta[i], voti_per_candidato[i]))
        else:
            listaFascia4.append((lista_candidati[i], lista_eta[i], voti_per_candidato[i]))

    listaFascia1.sort()

    print("Fascia uno <= 20")
    for fascia in listaFascia1:
        print "Candidato", fascia[0], "di eta", fascia[1], "con", fascia[2], "voti"

    print("21 <= Fascia <= 50")
    for fascia in listaFascia2:
        print "Candidato", fascia[0], "di eta", fascia[1], "con", fascia[2], "voti"

    print("51 <= Fascia <= 100")
    for fascia in listaFascia3:
        print "Candidato", fascia[0], "di eta", fascia[1], "con", fascia[2], "voti"

    print("Fascia > 100")
    for fascia in listaFascia4:
        print "Candidato", fascia[0], "di eta", fascia[1], "con", fascia[2], "voti"