class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._operaatiot = []
        self.kumottava = 0

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._operaatiot.append(-operandi)
        self.kumottava = -operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._operaatiot.append(operandi)
        self.kumottava = operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        self._arvo -= self._operaatiot.pop()
        #self._arvo -= self.kumottava
        #self.kumottava = 0
