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

    def getParolePiuLungheDi(self, listaParole, min = 1):
        piuLungheDi = []
        giaVerificate = []
        if not listaParole or listaParole is None:
            raise RuntimeError("Parametro vuoto o None")
        for parola in listaParole:
            if parola in giaVerificate:
                continue
            if len(parola) >= min:
                piuLungheDi.append(parola)
        return piuLungheDi

    def sortBy(self, listaParole, myKey = None):
        return sorted(listaParole, key=myKey)

    def getStessaLunghezza(self, listaParole):
        listaStessaLunghezza = []
        giaVerificate = []
        vero = False
        for parola in listaParole:
            if parola in giaVerificate:
                continue
            giaVerificate.append(parola)
            for altraParola in listaParole:
                if len(parola) == len(altraParola):
                    vero = True
            if vero:
                listaStessaLunghezza.append(parola)
        return listaStessaLunghezza

if __name__=="__main__":
    Libro = AnalizzaLibro("testo.txt")

    # Example of 2)
    parole = Libro.getParole()
    print(parole)

    lista10Volte = Libro.getParoleRipetutte10Volte(parole)
    print(lista10Volte)

    parolePiuLungheDi5 = Libro.getParolePiuLungheDi(lista10Volte, 5)
    sortedList = Libro.sortBy(parolePiuLungheDi5, len)
    print(sortedList)

    # Example of 3)
    parolePiuLungheDi8 = Libro.getParolePiuLungheDi(parole, 8)
    stessLunghezza = Libro.getStessaLunghezza(parolePiuLungheDi8)
    print(stessLunghezza)