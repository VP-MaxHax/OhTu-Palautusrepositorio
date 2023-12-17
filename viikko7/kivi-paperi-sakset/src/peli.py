
class Peli:
    def __init__(self, pelimuoto, tuomari):
        self.tuomari = tuomari
        self.tekoaly = pelimuoto

    def pelaa(self):
        self.ekan_siirto = self.ensimmaisen_siirto()
        self.tokan_siirto = self.toinen_siirto()
        while self._onko_ok_siirto(self.ekan_siirto) and self._onko_ok_siirto(self.tokan_siirto):
            self.laske_voittaja()
            self.ekan_siirto = self.ensimmaisen_siirto()
            if self.tekoaly == None:
                self.tokan_siirto = self.toinen_siirto()
            else:
                self.tokan_siirto = self.toinen_siirto()
                print(f"Tietokone valitsi: {self.tokan_siirto}")
                self.tekoaly.aseta_siirto(self.ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

        
    def ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def toinen_siirto(self):
        if self.tekoaly == None:
            return input("Toisen pelaajan siirto: ")
        else:
            return self.tekoaly.anna_siirto()

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def laske_voittaja(self):
        self.tuomari.kirjaa_siirto(self.ekan_siirto, self.tokan_siirto)
        print(self.tuomari)