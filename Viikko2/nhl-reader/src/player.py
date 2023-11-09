class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.games = games
        self.penalties = penalties

    
    def __str__(self):
        return self.name
