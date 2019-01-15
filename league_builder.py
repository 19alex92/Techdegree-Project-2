import csv

Sharks = []
Dragons = []
Raptors = []

players = []
experienced = []
unexperienced = []

with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    rows = list(reader)
    for row in rows:
        players.append(dict(row))
            
for data in players:
    if data['Soccer Experience'] == 'YES':
        experienced.append(data)
    else:
        unexperienced.append(data)
        
for ex in experienced:
    Sharks.append(ex)
    Dragons.append(ex)
    Raptors.append(ex)

print(Dragons)



#if __name__ == "__main__":
 #   league_builder_script()