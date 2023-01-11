team_a = []
team_b = []
stopped_game = False
for i in range(1, 12):
    team_a.append('A-'+str(i))
    team_b.append('B-'+str(i))
player_with_card = input().split()
for player in player_with_card:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        stopped_game = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if stopped_game:
    print("Game was terminated")