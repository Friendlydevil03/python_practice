class Player:
    def __init__(self, p_name, age, jerseyno, place, yoe, role):
        self.name = p_name
        self.age = age
        self.jerseyno = jerseyno
        self.place = place
        self.yoe = yoe  # Years of Experience
        self.role = role

    def player_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"\n--- Player Details ---")
        print(f"Jersey No: {self.jerseyno}")
        print(f"Place: {self.place}")
        print(f"Years of Experience: {self.yoe}")
        print(f"Role: {self.role}")


class Team:
    def __init__(self, team_name, coach, jersey_color, no_of_matches, ranking):
        self.team_name = team_name
        self.coach = coach
        self.jersey_color = jersey_color
        self.no_of_matches = no_of_matches
        self.ranking = ranking
        self.players = []  # List to hold multiple players

    def add_player(self, player):
        """Add a player to the team"""
        self.players.append(player)
        print(f"\n✓ {player.name} added to {self.team_name}")

    def remove_player(self, player_name):
        """Remove a player from the team"""
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f"\n✓ {player_name} removed from {self.team_name}")
                return
        print(f"\n✗ {player_name} not found in team")

    def show_all_players(self):
        """Display all players in the team"""
        print(f"\n{'='*50}")
        print(f"Team: {self.team_name} - Players Roster")
        print(f"{'='*50}")
        if not self.players:
            print("No players in the team yet")
        else:
            for i, player in enumerate(self.players, 1):
                print(f"\n{i}. {player.name} - Jersey #{player.jerseyno} - {player.role}")

    def team_details(self):
        """Display team information"""
        print(f"\n{'='*50}")
        print(f"Team Details: {self.team_name}")
        print(f"{'='*50}")
        print(f"Coach: {self.coach}")
        print(f"Jersey Color: {self.jersey_color}")
        print(f"Matches Played: {self.no_of_matches}")
        print(f"Ranking: {self.ranking}")
        print(f"Total Players: {len(self.players)}")


# Create players
p1 = Player("Adam", 45, 7, "India", 30, "Captain")
p2 = Player("John", 28, 10, "Australia", 8, "Batsman")
p3 = Player("Smith", 32, 5, "England", 12, "Bowler")
p4 = Player("Virat", 35, 18, "India", 15, "Batsman")

# Create team
team1 = Team("Chennai Kings", "Dhoni", "Yellow", 150, "1st")

# Add players to team
team1.add_player(p1)
team1.add_player(p2)
team1.add_player(p3)
team1.add_player(p4)

# Show team details
team1.team_details()

# Show all players
team1.show_all_players()

# Show individual player details
print("\n" + "="*50)
print("Captain Details:")
print("="*50)
p1.player_details()

# Remove a player
team1.remove_player("John")

# Show updated roster
team1.show_all_players()


# Example: Creating another team
print("\n\n" + "="*70)
print("CREATING ANOTHER TEAM")
print("="*70)

team2 = Team("Mumbai Indians", "Rohit", "Blue", 140, "2nd")
p5 = Player("Rohit", 36, 45, "India", 16, "Captain")
p6 = Player("Bumrah", 30, 93, "India", 10, "Bowler")

team2.add_player(p5)
team2.add_player(p6)
team2.team_details()
team2.show_all_players()