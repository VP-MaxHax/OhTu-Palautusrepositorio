import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_palauta_haettu_pelaaja(self):
        search = self.stats.search("Kur")

        self.assertEqual(search.name, "Kurri")

    def test_ei_etsittyä_pelaajaa(self):
        search = self.stats.search("Kul")

        self.assertEqual(search, None)

    def test_palauta_joukkueen_pelaajat(self):
        players_of_team = self.stats.team("EDM")

        self.assertEqual(len(players_of_team), 3)

    def test_järjestä_pisteiden_mukaan(self):
        tops = self.stats.top(4)

        lista = []
        for i in tops:
            lista.append(i.name)

        self.assertEqual(lista, ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri', 'Semenko'])

    def test_järjestä_sortby_maalien_mukaan(self):
        tops = self.stats.top(4, SortBy.GOALS)

        lista = []
        for i in tops:
            lista.append(i.name)

        self.assertEqual(lista, ['Lemieux', 'Yzerman', 'Kurri', 'Gretzky', 'Semenko'])

    def test_järjestä_sortby_syöttöjen_mukaan(self):
        tops = self.stats.top(4, SortBy.ASSISTS)

        lista = []
        for i in tops:
            lista.append(i.name)

        self.assertEqual(lista, ['Gretzky', 'Yzerman', 'Lemieux', 'Kurri', 'Semenko'])

    def test_järjestä_sortby_pisteiden_mukaan(self):
        tops = self.stats.top(4, SortBy.POINTS)

        lista = []
        for i in tops:
            lista.append(i.name)

        self.assertEqual(lista, ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri', 'Semenko'])
        