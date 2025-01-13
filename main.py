# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson and Gabriel Scott
# Main python file for the CombatSim project
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from aircraft import selectTeam
from simulation import runSimulation
from data_loader import getSpecs, displayAircraft
import utils
import time

# TrueColor ANSI escape codes
BLUE = '\033[38;2;0;0;255m'
RED = '\033[38;2;255;0;0m'
BOLD = '\033[1m'
RESET = '\033[0m'

def main():
    # If the user just started the program, greet them
    print("\nWelcome to the CombatSim program!")
    familiar = utils.greet_user()
    
    # Display the table of available aircrafts
    displayAircraft()
    
    # Explain to the use how the program works
    if familiar == "no":
        utils.explain()
    
    # Prompt the user to select the teams for the senario in an array
    TeamA_IDs, TeamA_names = selectTeam(f'{RED}A{RESET}')
    TeamB_IDs, TeamB_names = selectTeam(f'{BLUE}B{RESET}')
    
    # Display the teams selected without their commas and brackets
    print(f"\n{RED}Team A{RESET}:", ", ".join(TeamA_names))
    print(f"\n{BLUE}Team B{RESET}:", ", ".join(TeamB_names))
    
    # Get the specs of the aircrafts in both teams
    TeamA = getSpecs(TeamA_IDs, TeamA_names)
    TeamB = getSpecs(TeamB_IDs, TeamB_names)
    
    # Prompt the user to run the simulation
    result = run(TeamA, TeamB)
    
    # If the user wants to restart the program, restart it
    if result:
        restart()
    
def run(TeamA, TeamB):
    # Validate user input to run the simulation
    while True:
        # Prompt the user if they want to run the simulation
        run = input("\nReady to run simulation? (yes/no): ").lower()
            
        # Validate the input and reprompt if they put in wrong input
        if run == 'yes':
            result = runSimulation(TeamA, TeamB)
            time.sleep(1) # Pause for 1 second
            break
        elif run == 'no':
            print("\nSimulation canceled.")
            time.sleep(1) # Pause for 1 second
            result = False
            break
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
            time.sleep(1) # Pause for 1 second
            continue
    
    return result
    
def restart():
    # Prompt the user to restart the program
    if input("\nDo you want to restart the program? (yes/no): ").lower() == "yes":
        print("Restarting the program...")
        time.sleep(1) # Pause for 1 second
        main()
    else:
        print("\nThank you for using the CombatSim program. Goodbye!\n")
        time.sleep(1) # Pause for 1 second
        exit()

if __name__ == "__main__":
    main()
