
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
