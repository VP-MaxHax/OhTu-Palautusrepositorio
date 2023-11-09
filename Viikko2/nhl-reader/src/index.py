import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict["name"], player_dict["nationality"], player_dict["assists"], player_dict["goals"], player_dict["penalties"],\
                        player_dict["team"], player_dict["games"])
        if player.nationality == "FIN":
            players.append(player)

    print("Players from FIN")

    for player in players:
        print(f"{player.name:20} {player.team:5} {player.goals:2} + {player.assists:2} = {player.goals+player.assists:3}")

if __name__ == "__main__":
    main()