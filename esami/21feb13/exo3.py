class AnalizzaLibro:

    def __init__(self, name):
        if name == "" or name is None:
            raise RuntimeError
        self.name = name
        self.parole = []

    def getParole(self):
        with open(self.name, "rb") as myFile:
            lines = myFile.readlines()
            for line in lines:
                tmp = line.split(" ")
                for parola in tmp:
                    self.parole.append(parola)

        return self.parole

    def getRipetuta10Volte(self):
        pass


if __name__=="__main__":
    Libro = AnalizzaLibro("testo.txt")

    parole = Libro.getParole()

    for parola in parole:
        print(parola)