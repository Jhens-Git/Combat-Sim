# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Import and load csv related data
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv

class Aircraft:
    # Store aircraft attributes
    def __init__(self, name, maneuverability, stealth, EW, health):
        self.name = name
        self.maneuverability = maneuverability
        self.stealth = stealth
        self.EW = EW
        self.health = health
    
    def __repr__(self):
        return (f"Aircraft(name = {self.name}, maneuverability = {self.maneuverability}, stealth = {self.stealth}, EW = {self.EW}, health = {self.health})")

def loadData():
    # Initialize the team_specs dictionary
    Aircraft_dict = {}
    
    # Read the csv file and store aircrafts data in a dictionary for easy lookup
    with open('SpecSheet.csv', mode = 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {key.strip(): value.strip() for key, value in row.items()} # Strip spaces from column names and values
            name = row['Name']
            Aircraft_dict[name] = Aircraft(
                name = name,
                maneuverability = float(row['Maneuverability']),
                stealth = float(row['Stealth']),
                EW = float(row['Electronic Warfare']),
                health = int(row['Health'])
            )
    
    return Aircraft_dict

def getSpecs(names):
    # Initialize team array and aircraft dictionary
    team = []
    Aircraft_dict = loadData()
    
    for name in names:
        if name in Aircraft_dict:
            team.append(Aircraft_dict[name])
        else:
            print(f"Warning: {name} not found in specifications sheet!")
    return team

def displayAircraft():
    # Open the spec table of available aircraft
    with open('SpecSheet.csv', mode = 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        # Print the 1st three columns of available aircraft
        print(f"{header[0]:<10} {header[1]:<10} {header[2]:<20}")
        print("-" * 40)
        for row in csv_reader:
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<20}")
