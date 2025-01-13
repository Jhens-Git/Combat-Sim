# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# General purpose helper functions
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import time

# TrueColor ANSI escape codes
BLUE = '\033[38;2;0;0;255m'
RED = '\033[38;2;255;0;0m'
BOLD = '\033[1m'
RESET = '\033[0m'

def greet_user():
    # Initialize the speed of the text output
    seconds = 2

    while True:
        # Ask the user if they are familiar with the program
        familiar = input(f"\nAre you familiar with the CombatSim program? {BOLD}(yes/no){RESET}: ").lower()
        
        if familiar == "no":  # This is the user's first time
            time.sleep(seconds)
            print("\nThis program will simulate a combat scenario between combat aircraft.")
            time.sleep(seconds)
            print("You have the power to put aircraft in combat scenarios, and the program will run a simulation of it!")
            time.sleep(seconds)
            print(f"Obviously, this simulation is made for entertainment purposes only and {BOLD}should not be taken seriously{RESET}!")
            time.sleep(seconds)
            print("Let's get started!\n")
            time.sleep(seconds)
            break

        elif familiar == "yes":  # The user is familiar with the program
            time.sleep(seconds / 2)
            print("\nWelcome back!\n")
            time.sleep(seconds / 2)
            break
        
        elif familiar.strip() == "":
            time.sleep(seconds)
            print(f"\nInvalid input. Please enter '{BOLD}yes{RESET}' or '{BOLD}no{RESET}'\n")
            time.sleep(seconds)

        else:  # The user entered an invalid input
            time.sleep(seconds)
            print(f"\nInvalid input. Please enter '{BOLD}yes{RESET}' or '{BOLD}no{RESET}'\n")
            time.sleep(seconds)
            
    return familiar

def explain():
    # Initialize the speed of the text output
    seconds = 1 
    
    # This is the user's first time, explain how making team selections work
    time.sleep(seconds)
    print("This is a table of modern fighter jets. Use this for reference when making your teams!")
    time.sleep(seconds)
    print(f"There will be two strike groups, {RED}team A{RESET} and {BLUE}team B{RESET}, who will face off in an air-to-air combat senario.")
    time.sleep(seconds)
    print("This senario will assume pilots are identical in performance and training.")
    time.sleep(seconds)
    print(f"You can pick the aircrafts type, how much, and repeat for each team. Note that each team can have up to {BOLD}10 aircrafts{RESET}.")
    time.sleep(seconds)
    print("The program will then simulate the senario and display the results.")
    time.sleep(seconds)
    print("Once again, this simulation is made for entertainment purposes only and should not be taken seriously!")
    time.sleep(seconds)
    print("Let's get started!\n")
    time.sleep(seconds)
