import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.data = requests.get(url).json()

class PlayerStats:
    def __init__(self, reader):
        self.data = reader
        self.players = []
        for player_dict in reader: self.players.append(Player(player_dict["name"], player_dict["nationality"], player_dict["assists"], player_dict["goals"], player_dict["penalties"],\
                        player_dict["team"], player_dict["games"]))
            
    def top_scorers_by_nationality(self, nationality):
        player = []
        for i in self.players:
            if i.nationality == nationality:
                player.append(i)
        return sorted(player, key=lambda p: p.assists+p.goals, reverse=True)



def main():
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players")
    stats = PlayerStats(reader.data)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(f"{player.name:20} {player.team:5} {player.goals:2} + {player.assists:2} = {player.goals+player.assists:3}")

if __name__ == "__main__":
    main()