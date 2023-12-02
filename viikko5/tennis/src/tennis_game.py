class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0
        self.score_translation_list = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score_player1 += 1
        else:
            self.score_player2 += 1

    def score_even(self):
        if self.score_player1 >= 3:
            score = "Deuce"
        elif self.score_player1 < 3:
            score = f"{self.score_translation_list[self.score_player1]}-All"
        return score
    
    def score_advantage(self):
        advanced_states_list = [f"Win for {self.player2_name}", f"Advantage {self.player2_name}", "",\
                                 f"Advantage {self.player1_name}", f"Win for {self.player1_name}"]
        point_difference = max(min(self.score_player1 - self.score_player2, 2), -2)
        score = advanced_states_list[point_difference+2]
        return score

    def get_score(self):
        if self.score_player1 == self.score_player2:
            score = self.score_even()
        elif max(self.score_player1, self.score_player2) >= 4:
            score = self.score_advantage()
        else:
            score = f"{self.score_translation_list[self.score_player1]}-{self.score_translation_list[self.score_player2]}"
        return score
