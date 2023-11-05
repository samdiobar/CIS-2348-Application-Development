# Name: Samuel Barroso
# PSID: 1844307

class Team:

  def __init__(self):
    self.team_name = "none"
    self.team_wins = 0
    self.team_losses = 0

  def get_win_percentage(self):
    return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":
  student_team = Team()
  student_team.team_name = str(input())
  student_team.team_wins = int(input())
  student_team.team_losses = int(input())

  if student_team.get_win_percentage() > .5:
    print("Congratulations, Team", student_team.team_name, "has a winning average!")
  else:
    print("Team", student_team.team_name, "has a losing average.")