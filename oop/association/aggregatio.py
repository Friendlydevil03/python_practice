class Players:
    def __init__(self, p_name, age, jersey_no, place, yoe, role):
        self.name = p_name
        self.age = age
        self.jersey_no = jersey_no
        self.place = place
        self.yoe = yoe
        self.role = role

    def player_details(self):
        print(f"\nname: {self.name},\nage: {self.age},\njercy_no: {self.jersey_no},\nplace: {self.place},\nype: {self.yoe},\nrole: {self.role}")

class Team:
    def __init__(self,player,team_name,coach,jercy_color,no_of_matches,ranking):
        self.player = player
        self.team_name = team_name
        self.coach = coach
        self.jercy_color = jercy_color
        self.no_of_matches = no_of_matches
        self.ranking = ranking
        player.player_details()
        # p1.player_details()
        self.player.player_details()

    def team_details(self):
        print(f"\nt_name: {self.team_name},\ncoach: {self.coach},jercy_color:{self.jercy_color},\nmatches: {self.no_of_matches},\nranking{self.ranking}")

p1 = Players("ada",45,7,"india",30,"captian")
p2 = Players("<NAME>",36,2,"india",20,"captian")
# p1.player_details()
team1 = Team(p1,"cak","asd","yellow","33","first")

