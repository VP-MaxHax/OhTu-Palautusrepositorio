class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False
    
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True

        return False
    
class All:
    def test(self, player):
        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Pino:
    def __init__(self):
        self.alkiot = []

    def push(self, alkio):
        self.alkiot.append(alkio)

    def pop(self):
        return self.alkiot.pop()

    def empty(self):
        return len(self.alkiot) == 0

class QueryBuilder:
    def __init__(self, pino = All()):
        self.query_olio = pino

    def build(self):
        return self.query_olio
        
    def playsIn(self, team):
        return QueryBuilder(And(self.query_olio,PlaysIn(team)))
        
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_olio, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_olio, HasFewerThan(value, attr)))
    
    def oneOf(self, pino1, pino2):
        return QueryBuilder(Or(pino1, pino2))