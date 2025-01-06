# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson and Gabriel Scott
# Prompt user to select the aircrafts for the senario
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv

def selectTeam(teamName):
    
    # Initialize the team size, team array, and team cash
    teamSize = 0
    team = []
    teamCash = 0

    # Ask how much cash the team will have (maximum of $1 billion)
    teamCash = select_cash(teamName)
    
    # Loop to build the team until the team size reaches 10
    while True:
    
        # Prompt user to select aircraft for the senario
        aircraft_id, aircraft_cost, min_price = select_aircraft(teamName, teamCash)
        
        # Prompt user to select quantity of aircrafts
        aircraft_qty = select_qty(teamName, teamSize, aircraft_id, teamCash, aircraft_cost)
        teamCash -= aircraft_qty * aircraft_cost
        teamSize += aircraft_qty
        
        # Confirm the aircrafts added to the team and remaining cash balance
        print(f"{aircraft_qty} x {aircraft_id} added to team {teamName}.")
        print(f"Team {teamName} has ${teamCash} million left.")
        
        # Add the aircraft to the team array
        for i in range(aircraft_qty):
            team.append(aircraft_id)
            
        while True:
            # Check if the team size reaches 10
            if teamSize == 10:
                print(f"Team {teamName} has reached their aircraft limit.")
                break

            if teamCash < min_price:
                print(f"It is not possible for team {teamName} purchase any more aircraft.")
                break
            
            # Ask user if they want more aircrafts
            add = input("Do you want to add more aircrafts to the team? (yes/no): ").lower()
            if add == "no" or add == "yes": 
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
        
        # If the team size reaches 10 or they finished building the team, break the loop
        if teamSize == 10 or add == "no" or teamCash < min_price:
            break
        else:
            continue
        
    # Return the team array
    return team

def select_cash(teamName):

    while True:
        # Prompt user to enter a cash amount
        cash = input(f"Enter amount of cash for team {teamName} (million USD): ")
        cash_number = cash.isnumeric() # Checks if user inputted only numeric input
             
        if cash_number == 0:
            print("\nInvalid input. Please enter only numbers!\n")
        elif int(cash) > 1000:
            print("\nInvalid input. Please enter a value less than or equal to 1 billion (1000).\n")
        else:
            break

    cash = int(cash)
            
    return cash
    
def select_aircraft(teamName, teamCash):

    with open(r'C:\Users\admir\OneDrive\VS Code\General\air_combat_sim\SpecSheet.csv') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            valid_ids = [row[1] for row in csv_reader]

    with open(r'C:\Users\admir\OneDrive\VS Code\General\air_combat_sim\SpecSheet.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        prices = [row[4] for row in csv_reader]

    for i in range(len(prices)):
        prices[i] = int(prices[i])

    min_price = min(prices)

    while True:
        # Prompt user to pick an aircraft
        aircraft_id = input(f"\nEnter an aircraft ID for team {teamName} (Example 'F22'): ")
        
        # Validate the aircraft ID
        # If the aircraft ID is not in the list of valid IDs, prompt the user to enter the ID again
        if aircraft_id not in valid_ids:
                print("Invalid aircraft ID. Please try again.")
        else:
            # Extract the cost of the aircraft
            for i in range(len(valid_ids)):
                if aircraft_id == valid_ids[i]:
                    aircraft_cost = prices[i]
            if teamCash - aircraft_cost < 0:
                print(f"Aircraft cost exceeds team {teamName}'s remaining cash. Please select a cheaper aircraft.")
            else:
                break

    return aircraft_id, aircraft_cost, min_price

def select_qty(teamName, teamSize, aircraft_id, teamCash, aircraft_cost):
    
    # If the input is invalid, prompt the user to enter the quantity again
    while True:
        # Prompt user to enter the number of aircrafts
        aircraft_qty = int(input(f"Enter the number of {aircraft_id} for team {teamName} (Note, up to 10 allowed per team): "))
        
        # Validate the aircraft quantity
        if not str(aircraft_qty).isdigit():
            print("Invalid quantity. Please enter a number.")
        elif aircraft_qty < 1:
            print("Invalid quantity. Please enter a number greater than 0.")
        elif aircraft_qty + teamSize > 10:
            print("Please enter a smaller number. The team has reached the limit of 10 aircrafts.")
        else:
            if teamCash - (aircraft_qty * aircraft_cost) < 0:
                print(f"Purchasing this quantity of the {aircraft_id} exceeds team {teamName}'s cash. Please lower the quantity purchased.")
            else:
                break
    
    return aircraft_qty
