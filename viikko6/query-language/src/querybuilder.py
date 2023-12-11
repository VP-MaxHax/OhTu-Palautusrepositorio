from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class Pino:
    def __init__(self):
        self.alkiot = []

    def push(self, alkio):
        self.alkiot.append(alkio)

    def pop(self):
        return self.alkiot.pop()

    def empty(self):
        return len(self.alkiot) == 0


class QueryBulder:
    def __init__(self):
        self.query_olio = Pino()

    def all(self):
        return QueryBulder()
    
    def pino(self):
        return self.query_olio