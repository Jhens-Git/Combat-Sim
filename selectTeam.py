# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Prompt user to select the aircrafts for the senario
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv

def getTeam(teamName):
    
    # Initialize the team size and team array
    teamSize = 0
    team = []
    
    # Loop to build the team until the team size reaches 10
    while True:
    
        # Prompt user to select aircraft for the senario
        aircraft_id = select_aircraft(teamName)
        
        # Prompt user to select quantity of aircrafts
        aircraft_qty = select_qty(teamName, teamSize, aircraft_id)
        teamSize += aircraft_qty
        
        # Confirm the aircrafts added to the team
        print(f"{aircraft_qty}x {aircraft_id} added to team {teamName}.")
        
        # Add the aircraft to the team array
        for i in range(aircraft_qty):
            team.append(aircraft_id)
            
        while True:
            # Check if the team size reaches 10
            if teamSize == 10:
                break
            
            # Ask user if they want more aircrafts
            add = input("Do you want to add more aircrafts to the team? (yes/no): ").lower()
            if add == "no" or add == "yes": 
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
        
        # If the team size reaches 10 or they finished building the team, break the loop
        if teamSize == 10 or add == "no":
            break
        else:
            continue
        
    # Return the team array
    return team

def select_aircraft(teamName):

    while True:
        # Prompt user to pick an aircraft
        aircraft_id = input(f"Enter the aircraft ID for team {teamName} (Example 'F22'): ")
        
        # Validate the aircraft ID
        with open('Spec_Sheet.csv', mode = 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            valid_ids = [row[1] for row in csv_reader]
            
            # If the aircraft ID is not in the list of valid IDs, prompt the user to enter the ID again
            if aircraft_id not in valid_ids:
                print("Invalid aircraft ID. Please try again.")
            else:
                break
    
    return aircraft_id

def select_qty(teamName, teamSize, aircraft_id):
    
    # If the input is invalid, prompt the user to enter the quantity again
    while True:
        # Prompt user to enter the number of aircrafts
        aircraft_qty = input(f"Enter the number of {aircraft_id} for team {teamName} (Note, we only allow up to 10 in a team): ")
        
        # Validate the aircraft quantity
        if not aircraft_qty.isdigit():
            print("Invalid quantity. Please enter a number.")
        elif int(aircraft_qty) < 1:
            print("Invalid quantity. Please enter a number greater than 0.")
        elif int(aircraft_qty) + teamSize > 10:
            print("Please enter a smaller number. The team has reached the limit of 10 aircrafts.")
        else:
            break
    
    return int(aircraft_qty)