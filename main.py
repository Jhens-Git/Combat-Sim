# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Main python file for the CombatSim project
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from aircraft import selectTeam
from simulation import runSimulation
from data_loader import getSpecs, displayAircraft
import utils

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
    # TeamA_IDs, TeamA_names = selectTeam('Jamie')
    # TeamB_IDs, TeamB_names = selectTeam('Gabriel')
    TeamA_IDs = ['F22', 'F35', 'FA18', 'FA18', 'FA18', 'FA18']
    TeamB_IDs = ['Su57', 'J20', "Su35", 'Su35', 'Su27', 'Su27']
    TeamA_names = ['Raptor', 'Lightning II', 'Hornet 1', 'Hornet 2', 'Hornet 3', 'Hornet 4']
    TeamB_names = ['Felon', 'Mighty Dragon', "Flanker-E 1", 'Flanker-E 2', 'Flanker 1', 'Flanker 2']
    
    # Display the teams selected without their commas and brackets
    print("\nTeam A:", ", ".join(TeamA_names))
    print("\nTeam B:", ", ".join(TeamB_names))
    
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
