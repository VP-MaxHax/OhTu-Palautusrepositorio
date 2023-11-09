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
        print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists}")

if __name__ == "__main__":
    main()