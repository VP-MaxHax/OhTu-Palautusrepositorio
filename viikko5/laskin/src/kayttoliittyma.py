from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self.sovellus = sovellus
        self.root = root
        self.komennot = {
            Komento.SUMMA: Summa(self.sovellus),
            Komento.EROTUS: Erotus(self.sovellus),
            Komento.NOLLAUS: Nollaus(self.sovellus),
            Komento.KUMOA: Kumoa(self.sovellus)
        }

    def kaynnista(self):
        self.arvo_var = StringVar()
        self.arvo_var.set(self.sovellus.arvo())
        self.syote_kentta = ttk.Entry(master=self.root)

        tulos_teksti = ttk.Label(textvariable=self.arvo_var)

        summa_painike = ttk.Button(
            master=self.root,
            text="Summa",
            command=lambda: self.suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self.root,
            text="Erotus",
            command=lambda: self.suorita_komento(Komento.EROTUS)
        )

        self.nollaus_painike = ttk.Button(
            master=self.root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self.suorita_komento(Komento.NOLLAUS)
        )

        self.kumoa_painike = ttk.Button(
            master=self.root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self.suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self.syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self.nollaus_painike.grid(row=2, column=2)
        self.kumoa_painike.grid(row=2, column=3)



    def suorita_komento(self, komento):
        arvo = 0
        try:
            arvo = int(self.syote_kentta.get())
        except Exception:
            pass
        komento_olio = self.komennot[komento]
        komento_olio.suorita(arvo)
        self.kumoa_painike["state"] = constants.NORMAL

        if self.sovellus.arvo() == 0:
            self.nollaus_painike["state"] = constants.DISABLED
        else:
            self.nollaus_painike["state"] = constants.NORMAL

        self.syote_kentta.delete(0, constants.END)
        self.arvo_var.set(self.sovellus.arvo())

class Summa:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.plus(arvo)

class Erotus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.miinus(arvo)

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.kumoa()