from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari
from peli import Peli

class Pelinrakentaja:
    def vastaan_tekoäly():
        return Peli(Tekoaly(), Tuomari())
    
    def vastaan_kehittynyt_tekoäly():
        return Peli(TekoalyParannettu(10), Tuomari())
    
    def vastaan_ihminen():
        return Peli(None, Tuomari())