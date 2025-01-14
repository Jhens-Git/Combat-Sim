# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson and Gabriel Scott
# Prompt user to select the aircrafts for the senario
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv
import time

def selectTeam(teamName):
    # Initialize the team size, team IDs array, team names array, and team cash
    teamSize = 0
    teamIDs = []
    teamNames = []
    teamCash = 0

    # Ask how much cash the team will have (maximum of $1 billion)
    teamCash = select_cash(teamName)
    
    # Loop to build the team until the team size reaches 10
    while True:
    
        # Prompt user to select aircraft for the senario
        aircraft_id, aircraft_name, aircraft_cost, min_price = select_aircraft(teamName, teamCash)
        
        # Prompt user to select quantity of aircrafts
        aircraft_qty = select_qty(teamName, teamSize, aircraft_id, teamCash, aircraft_cost)
        teamCash -= aircraft_qty * aircraft_cost
        teamSize += aircraft_qty
        
        # Confirm the aircrafts added to the team and remaining cash balance
        print(f"{aircraft_qty} x {aircraft_id} {aircraft_name} added to team {teamName}.")
        print(f"Team {teamName} has ${teamCash} million left.")
        time.sleep(1) # Pause for 1 second
            
        # Check if the user chose an aircraft already in the team
        prev_qty = 0
        already_in = False
        for ID in teamIDs:
            if aircraft_id == ID:
                prev_qty += 1 # Count the number of that aircraft type already in the team
                already_in = True
        aircraft_qty += prev_qty
        
        if already_in == False: # Append the aircraft with their names and quantity number
            if aircraft_qty == 1:
                teamIDs.append(f"{aircraft_id}")
                teamNames.append(f"{aircraft_name}")
            else:
                for i in range(1, aircraft_qty + 1):
                    teamIDs.append(f"{aircraft_id}")
                    teamNames.append(f"{aircraft_name} {i}")
                    
        elif already_in == True: # Append more of that same type of aircraft
            for i in range(prev_qty, aircraft_qty):
                teamIDs.append(f"{aircraft_id}")
                teamNames.append(f"{aircraft_name} {i}")
                
        else:
            print("Something went wrong in qty append @ selectTeam()")
        
        # Continue to either add for aircrafts or not
        while True:
            # Check if the team size reaches 10
            if teamSize == 10:
                print(f"Team {teamName} has reached their aircraft limit.")
                time.sleep(1) # Pause for 1 second
                break

            # Check if team has reach their price limit
            if teamCash < min_price:
                print(f"It is not possible for team {teamName} purchase any more aircraft.")
                time.sleep(1) # Pause for 1 second
                break
            
            # Ask user if they want more aircrafts
            add = input("Do you want to add more aircrafts to the team? (yes/no): ").lower()
            if add == "no" or add == "yes":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                time.sleep(1) # Pause for 1 second
                continue
        
        # If the team size reaches 10 or they finished building the team, break the loop
        if teamSize == 10 or add == "no" or teamCash < min_price:
            break
        else:
            continue
        
    # Return the team array
    return teamIDs, teamNames

def select_cash(teamName):
    while True:
        # Prompt user to enter a cash amount
        cash = input(f"\nEnter amount of cash for team {teamName} (million USD): ")
        cash_number = cash.isnumeric() # Checks if user inputted only numeric input
            
        # Check if input is valid
        if cash_number == 0:
            print("\nInvalid input. Please enter only numbers!\n")
        elif int(cash) > 1000:
            print("\nToo much. Please enter a value between 100 million (100) and 1 billion (1000).\n")
        elif int(cash) < 100:
            print("\nToo little. Please enter a value between 100 million (100) and 1 billion (1000).\n")
        else:
            break
        time.sleep(1) # Pause for 1 second

    # Round cash value to the nearest million
    cash = int(cash)
            
    return cash
    
def select_aircraft(teamName, teamCash):
    # Open the csv file and get the id, name, and price of the aircraft
    with open('SpecSheet.csv', mode='r') as file:
        csv_reader = list(csv.reader(file))
        header = csv_reader[0]  # Save header if needed
        rows = csv_reader[1:]   # Skip header

        # Populate the arrays for ids, aircraft names, and their prices
        valid_ids = [row[1] for row in rows]
        names = [row[2] for row in rows]
        prices = [row[4] for row in rows]

    # Find the aircraft with the lowest price available
    for i in range(len(prices)):
        prices[i] = int(prices[i])
    min_price = min(prices)

    while True:
        # Prompt user to pick an aircraft
        aircraft_id = input(f"\nEnter an aircraft ID for team {teamName} (Example 'F22'): ")
        
        # If the aircraft ID is not in the list of valid IDs, prompt the user to enter the ID again
        if aircraft_id not in valid_ids or aircraft_id.strip() == "":
                print("Invalid aircraft ID. Please try again.")
                time.sleep(1) # Pause for 1 second
        else:
            # Extract the cost of the aircraft
            for i in range(len(valid_ids)):
                if aircraft_id == valid_ids[i]:
                    aircraft_name = names[i]
                    aircraft_cost = prices[i]
            if teamCash - aircraft_cost < 0:
                print(f"Aircraft cost exceeds team {teamName}'s remaining cash. Please select a cheaper aircraft.")
                time.sleep(1) # Pause for 1 second
            else:
                break

    return aircraft_id, aircraft_name, aircraft_cost, min_price

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
        time.sleep(1) # Pause for 1 second
    
    return aircraft_qty
