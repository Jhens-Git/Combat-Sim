# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Import and load csv related data
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv

class Aircraft:
    # Store aircraft attributes
    def __init__(self, ID, name, price, maneuverability, stealth, EW, health):
        self.ID = ID
        self.name = name
        self.price = price
        self.maneuverability = maneuverability
        self.stealth = stealth
        self.EW = EW
        self.health = health
    
    def __repr__(self):
        return (f"Aircraft(ID = {self.ID}, name = {self.name}, price = {self.price}, maneuverability = {self.maneuverability}, stealth = {self.stealth}, EW = {self.EW}, health = {self.health})")

def loadData():
    # Initialize the team_specs dictionary
    Aircraft_dict = {}
    
    # Read the csv file and store aircrafts data in a dictionary for easy lookup
    with open('Spec_Sheet.csv', mode = 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {key.strip(): value.strip() for key, value in row.items()} # Strip spaces from column names and values
            ID = row['ID']
            Aircraft_dict[ID] = Aircraft(
                ID = ID,
                name = str(row['Name']),
                price = int(row['Price']),
                maneuverability = float(row['Maneuverability']),
                stealth = float(row['Stealth']),
                EW = float(row['Electronic Warfare']),
                health = int(row['Health'])
            )
    
    return Aircraft_dict

def getSpecs(IDs):
    # Initialize team array and aircraft dictionary
    team = []
    Aircraft_dict = loadData()
    
    for ID in IDs:
        if ID in Aircraft_dict:
            team.append(Aircraft_dict[ID])
        else:
            print(f"Warning: {ID} not found in specifications sheet!")
    return team

def displayAircraft():
    # Open the spec table of available aircraft
    with open('Spec_Sheet.csv', mode = 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        # Print the 1st five columns of available aircraft
        print(f"{header[0]:<10} {header[1]:<10} {header[2]:<20} {header[3]:<10} {header[4]:<1} (million USD)")
        print("-" * 60)
        for row in csv_reader:
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<20} {row[3]:<10} {row[4]:<20}")
