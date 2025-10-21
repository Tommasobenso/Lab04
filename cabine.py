class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self.prezzo = float(prezzo)

class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, animali):
        super().__init__(codice, letti, ponte, prezzo)
        self.animali = animali






class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, tipo):
        super().__init__(codice, letti, ponte, prezzo)
        self.tipo = tipo


