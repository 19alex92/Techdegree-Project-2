import csv

team_name_1 = "sharks"
team_name_2 = "raptors"
team_name_3 = "dragons"

sharks = []
raptors = []
dragons = []

players = []
experienced = []
unexperienced = []

#test git
# Include comments!!!!

# opens file and reads it into players + makes a dict
def open_file(humans):
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        rows = list(reader)
        for row in rows:
            humans.append(dict(row))

# sorts players in experienced and unexperienced            
def sort_players(humans, exp, unexp):
    for data in humans:
        if data['Soccer Experience'] == 'YES':
            exp.append(data)
        else:
            unexp.append(data)

# sorts experienced players evenly in 3 teams
def sort_experienced(exp, sharks, raptors, dragons):
    for divide in exp:
        if len(sharks) < len(raptors):
            sharks.append(divide)
        elif len(dragons) < len(sharks):
            dragons.append(divide)
        else:
            raptors.append(divide)

# sorts unexperienced players evenly in 3 teams
def sort_unexperienced(unexp, sharks, raptors, dragons):
    for divide in unexp:
        if len(sharks) < len(raptors):
            sharks.append(divide)
        elif len(dragons) < len(sharks):
            dragons.append(divide)
        else:
            raptors.append(divide)

def create_team_file(team, team_name):
    with open("teams.txt", "a") as file:
        file.write("\n" + team_name.upper() + "\n" + "="*20 + "\n")
        for iteration in range(len(team)):
            file.write(
                        team[iteration]['Name'] + ", " 
                        + team[iteration]['Soccer Experience'] + ", " 
                        + team[iteration]['Guardian Name(s)'] + "\n"
                        )


def create_player_files(humans, sharks, raptors, dragons):
    for iteration in range(len(humans)):
        name = humans[iteration]['Name']
        for teams in range(len(sharks)) and range(len(raptors)) and range(len(dragons)):
            if name == sharks[teams]['Name']:
                team_name = "Sharks"
                first_training = "02-11-2019"
            elif name == raptors[teams]['Name']:
                team_name = "Raptors"
                first_training = "02-12-2019"
            elif name == dragons[teams]['Name']:
                team_name = "Dragons"
                first_training = "02-13-2019"
        name = name.lower().replace(" ", "_") + ".txt"
        parents = humans[iteration]['Guardian Name(s)']
        child = humans[iteration]['Name']
        with open(name, "a") as file:
            file.write("Dear {},\n" 
                        "our new advanced algorithm drafted this years teams.\n"
                        "Your Child {} is going to play on team {}.\n"
                        "The first training will be on {}.".format(parents, child, team_name, first_training))

    
def league_builder_script():
    open_file(players)
    sort_players(players, experienced, unexperienced)
    sort_experienced(experienced, sharks, raptors, dragons)
    sort_unexperienced(unexperienced, sharks, raptors, dragons)
    create_team_file(sharks, team_name_1)
    create_team_file(raptors, team_name_2)
    create_team_file(dragons, team_name_3)
    create_player_files(players, sharks, raptors, dragons)


if __name__ == "__main__":
    league_builder_script()