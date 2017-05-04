import json
import datetime
print "Remaining Premier League Fixtures\n"

with open('en.1.json') as json_data:
	data = json.load(json_data)
	rounds = data['rounds']
	for matchday in rounds:
		matches = matchday['matches']
		for match in matches:
			match_date = match['date']
			home_team = match['team1']['name']
			away_team = match['team2']['name']
			current = datetime.datetime.now().strftime ("%Y-%m-%d")
			if current < match_date:
				print match_date, home_team, "vs", away_team


