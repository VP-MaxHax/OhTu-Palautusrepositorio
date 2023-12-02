class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.joukko = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        return alkio in self.joukko

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            self.joukko[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            if self.alkioiden_lkm % len(self.joukko) == 0:
                taulukko_old = self.joukko[:]
                self.joukko = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.joukko)

    def poista(self, alkio):
        if alkio in self.joukko:
            self.joukko.remove(alkio)
            self.alkioiden_lkm -= 1

    def kopioi_lista(self, joukko_a, joukko_b):
        for i in range(len(joukko_a)):
            joukko_b[i] = joukko_a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.joukko[i]
        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        palautettava_joukko = IntJoukko()
        for i in joukko_a.to_int_list():
            palautettava_joukko.lisaa(i)
        for i in joukko_b.to_int_list():
            palautettava_joukko.lisaa(i)
        return palautettava_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        palautettava_joukko = IntJoukko()
        for i in joukko_a.to_int_list():
            for j in joukko_b.to_int_list():
                if i == j:
                    palautettava_joukko.lisaa(j)
        return palautettava_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        palautettava_joukko = IntJoukko()
        for i in joukko_a.to_int_list():
            palautettava_joukko.lisaa(i)
        for i in joukko_b.to_int_list():
            palautettava_joukko.poista(i)
        return palautettava_joukko

    def __str__(self):
        string = "{"
        for i in range(self.alkioiden_lkm):
            string += str(self.joukko[i])
            if i < self.alkioiden_lkm-1:
                string += ", "
        string += "}"
        return string