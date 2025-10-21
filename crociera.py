from cabine import Cabina, CabinaAnimali, CabinaDeluxe
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.cabine = {}
        self.passeggeri = {}
        self.prenotazioni = []






    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        file = open(file_path, "r")
        for line in file:
            line = line.strip()
            dato = line.split(",")
            if "CAB" in dato[0]:
                if len(dato) == 4:
                    self.cabine[dato[0]] = Cabina(dato[0], dato[1], dato[2], dato[3])
                elif len(dato) == 5 and dato[4].isdigit():
                    self.cabine[dato[0]] = CabinaAnimali(dato[0], dato[1], dato[2], dato[3], dato[4])
                elif len(dato) == 5:
                    self.cabine[dato[0]] = CabinaDeluxe(dato[0], dato[1], dato[2], dato[3], dato[4])
                else:
                    raise ValueError
            elif "P" in dato[0]:
                self.passeggeri[dato[0]] = Passeggero(dato[0], dato[1], dato[2])






    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        cabina =





    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self.passeggeri.values():
            print(passeggero)

