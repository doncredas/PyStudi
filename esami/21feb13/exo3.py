class AnalizzaLibro:

    def __init__(self, name):
        if name == "" or name is None:
            raise RuntimeError
        self.name = name

    # 1) leggere tutte le parole contenute nel file e caricarle su una struttura dati adeguata
    def getParole(self):
        listaParole = []
        with open(self.name, "rb") as myFile:
            lines = myFile.readlines()
            for line in lines:
                tmp = line.split(" ")
                for parola in tmp:
                    listaParole.append(parola)

        return [ x.lower() for x in listaParole]

    # 2)
    def getParoleRipetutte10Volte(self, listaParole):
        if not listaParole or listaParole is None:
            raise RuntimeError("Parametro vuoto o None")
        listaParole10V = []
        parolaGiaVerificata = []
        count=0
        for parola in listaParole:
            if parola in parolaGiaVerificata:
                continue
            parolaGiaVerificata.append(parola)
            for altreParole in listaParole:
                if parola == altreParole:
                    count += 1
            if count >= 10:
                listaParole10V.append(parola)
            count=0
        return listaParole10V


if __name__=="__main__":
    Libro = AnalizzaLibro("testo.txt")

    # Example of method 1) getParole
    parole = Libro.getParole()
    print(parole)

    # Example of method 2)
    lista10Volte = Libro.getParoleRipetutte10Volte(parole)
    print(lista10Volte)