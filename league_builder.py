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


def sort_teams(player, team_1, team_2, team_3):
    """Sorts players evenly in 3 teams"""
    for sort in player:
        if len(team_1) < len(team_2):
            team_1.append(sort)
        elif len(team_3) < len(team_1):
            team_3.append(sort)
        else:
            team_2.append(sort)


def create_team_file(team, team_name):
    """Creats a new file named teams.txt and writes
    the different Teams as well as the fitting players into it
    """
    with open("teams.txt", "a") as file:
        file.write("\n" + team_name.upper() + "\n" + "="*20 + "\n")
        for iteration in range(len(team)):  # This range(len()) gives back a number for every dict while iterating through
            file.write(team[iteration]['Name'] + ", "
                       + team[iteration]['Soccer Experience'] + ", "
                       + team[iteration]['Guardian Name(s)'] + "\n"
                       )


def create_player_files(humans, sharks, raptors, dragons):
    """Creats a txt file for each player with a personalised message in it"""
    for iteration in range(len(humans)):  # With range(len()) this again gives back a number for each dict while iterating through
        name = humans[iteration]['Name']
        for teams in range(len(sharks)) and range(len(raptors)) and range(len(dragons)):  # Same here with range(len()), except here I
            if name == sharks[teams]['Name']:                                             # use it to iterate through each team
                team_name = "Sharks"                                                      # and match the player name from the previous loop
                first_training = "02-11-2019"                                             # with the player name in this loop, to find out in
            elif name == raptors[teams]['Name']:                                          # which team they are
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
    """Runs all the functions for the programm"""
    open_file(players)
    sort_players(players, experienced, unexperienced)
    sort_teams(experienced, sharks, raptors, dragons)
    sort_teams(unexperienced, sharks, raptors, dragons)
    create_team_file(sharks, team_name_1)
    create_team_file(raptors, team_name_2)
    create_team_file(dragons, team_name_3)
    create_player_files(players, sharks, raptors, dragons)


if __name__ == "__main__":
    league_builder_script()
