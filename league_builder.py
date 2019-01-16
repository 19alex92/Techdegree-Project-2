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


def open_file(humans):
    """Opens a file and reads it as a dict into players"""
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        rows = list(reader)
        for row in rows:
            humans.append(dict(row))


def sort_players(humans, exp, unexp):
    """Sorts players in experienced and unexperienced"""
    for data in humans:
        if data['Soccer Experience'] == 'YES':
            exp.append(data)
        else:
            unexp.append(data)


def sort_experienced(exp, team_1, team_2, team_3):
    """Sorts experienced players evenly in 3 teams"""
    for divide in exp:
        if len(team_1) < len(team_2):
            team_1.append(divide)
        elif len(team_3) < len(team_1):
            team_3.append(divide)
        else:
            team_2.append(divide)


def sort_unexperienced(unexp, team_1, team_2, team_3):
    """Sorts unexperienced players evenly in 3 teams"""
    for divide in unexp:
        if len(team_1) < len(team_2):
            team_1.append(divide)
        elif len(team_3) < len(team_1):
            team_3.append(divide)
        else:
            team_2.append(divide)


def create_team_file(team, team_name):
    """Creats a new file named teams.txt and writes
    the different Teams as well as the fitting players into it
    """
    with open("teams.txt", "a") as file:
        file.write("\n" + team_name.upper() + "\n" + "="*20 + "\n")
        for iteration in range(len(team)):
            file.write(team[iteration]['Name'] + ", "
                       + team[iteration]['Soccer Experience'] + ", "
                       + team[iteration]['Guardian Name(s)'] + "\n"
                       )


def create_player_files(humans, sharks, raptors, dragons):
    """Creats a txt file for each player with a personalised message in it"""
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
            file.write(
                        "Dear {},\n"
                        "our new advanced algorithm drafted this years teams.\n"
                        "Your Child {} is going to play in team {}.\n"
                        "The first training will be on {}.\n"
                        "Have a great day!"
                        .format(parents, child, team_name, first_training)
                        )


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
