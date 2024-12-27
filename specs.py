# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Give specs of the selected aircrafts in the team
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv
import numpy as np

def getSpecs(team):
    
    # Initialize the team_specs matrix
    team_specs = np.array([])
        
    # Loop through the team array and get the specs of each aircraft
    for aircraft in team:
        # Get the specs of the aircraft
        with open('Spec_Sheet.csv', mode = 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                if row[1] == aircraft:
                    if team_specs.size == 0: # If the team_specs matrix is empty, append the first row
                        team_specs = np.array(row[4:8])
                    else:
                        # Append the only values in column 4 to 7 to the team_specs matrix as a new row
                        new_row = np.array(row[4:8])
                        team_specs = np.vstack([team_specs, new_row])
                    break
    
    return team_specs