players = input()

team_a_players = players.split('0')
team_b_players = players.split('1')

if len(max(team_a_players, key = len)) >= 7 or len(max(team_b_players, key = len)) >= 7:
    print('YES')
else:
    print('NO')