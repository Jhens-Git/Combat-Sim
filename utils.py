# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# General purpose helper functions
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv

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

def explain():
    # This is the user's first time, explain how making team selections work
    print("\nThese are the available aircrafts for the senario")
    print("There will be two strike groups, team A and team B, who will face off in an air-to-air combat senario.")
    print("This senario will assume pilots are identical in performance and training.")
    print("You can pick the aircrafts type, how much, and repeat for each team. Note that each team can have up to 10 aircrafts.")
    print("The program will then simulate the senario and display the results.")
    print("Once again, this simulation is made for entertainment purposes only and should not be taken seriously!")
    print("Let's get started!\n")
