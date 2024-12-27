# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Main python file for the CombatSim project
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from selectTeam import getTeam
from simulate import runSimulation
from specs import getSpecs
import csv

def main():
    
    # If the user just started the program, greet them
    print("\nWelcome to the CombatSim program!")
    familiar = greet_user()
    
    # Display the table of available aircrafts
    displayAircraft()
    
    # Explain to the use how the program works
    if familiar == "no":
        explain()
    
    # Prompt the user to select the teams for the senario
    print("\nTeam A\n")
    TeamA = getTeam('A')
    print("\nTeam B\n")
    TeamB = getTeam('B')
    
    # Display the teams selected without their commas and brackets
    print("\nTeam A:", ", ".join(TeamA))
    print("Team B:", ", ".join(TeamB))
    
    # Get the specs of the aircrafts in both teams
    TeamA_specs = getSpecs(TeamA)
    TeamB_specs = getSpecs(TeamB)
    
    print("\nTeam A Specs:", TeamA_specs)
    
    # Prompt the user to run the simulation
    result = run(TeamA, TeamA_specs, TeamB, TeamB_specs)
    
    # Prompt the user if they want to run another simulation
    #if result == False:
    #    restart()

def greet_user():
        
    # Ask the user if they are familiar with the program
    familiar = input("\nAre you familiar with the CombatSim program? (yes/no): ").lower()
    
    if familiar == "no": # This is the user's first time
        print("\nThis program will simulate a combat senario between combat aircrafts.")
        print("You have the power to put aircrafts in combat senarios and the program will run a simulatation of it!")
        print("Obviously, this simulation is made for entertainment purposes only and should not be taken seriously!")
        print("Let's get started!\n")
        
    elif familiar == "yes": # The user is familiar with the program
        print("\nWelcome back!\n")
        
    else: # The user entered an invalid input
        print("\nInvalid input. Please enter 'yes' or 'no'\n")
        greet_user()
        
    return familiar
    
def displayAircraft():
    # Open the spec table of available aircraft
    with open('Spec_Sheet.csv', mode = 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        # Print the 1st three columns of available aircraft
        print(f"{header[0]:<10} {header[1]:<10} {header[2]:<20}")
        print("-" * 40)
        for row in csv_reader:
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<20}")
    
    # Print a new line after table for spacing purposes
    print("\n")

def explain():
    # This is the user's first time, explain how making team selections work
    print("\nThese are the available aircrafts for the senario")
    print("There will be two strike groups, team A and team B, who will face off in an air-to-air combat senario.")
    print("This senario will assume pilots are identical in performance and training.")
    print("You can pick the aircrafts type, how much, and repeat for each team. Note that each team can have up to 10 aircrafts.")
    print("The program will then simulate the senario and display the results.")
    print("Once again, this simulation is made for entertainment purposes only and should not be taken seriously!")
    print("Let's get started!\n")
    
def run(TeamA, TeamB):
    # Validate user input to run the simulation
    while True:
        # Prompt the user if they want to run the simulation
        run = input("\nRun simulation? (yes/no): ").lower()
            
        # Validate the input and reprompt if they put in wrong input
        if run == 'yes':
            result = runSimulation(TeamA, TeamB)
            break
        elif run == 'no':
            print("\nSimulation canceled.")
            result = False
            break
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
            continue
    
    return result
    
def restart():
    # Prompt the user to restart the program
    if input("\nDo you want to restart the program? (yes/no): ").lower() == "yes":
        print("Restarting the program...")
        main()
    else:
        print("\nThank you for using the CombatSim program. Goodbye!")
        exit()

if __name__ == "__main__":
    main()