# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Run simulations logic of the flight combat senario
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import random

def runSimulation(TeamA, TeamB):
    # Initialize combat distance in nautical miles
    distance = 50
    
    # Initialize list of aircraft detected
    detected_TeamA = []
    detected_TeamB = []
    
    # Initialize list of aircraft undetected (All start off as undetected)
    undetected_TeamA = []
    undetected_TeamB = []
    for aircraft in TeamA:
        undetected_TeamA.append(aircraft)
    for aircraft in TeamB:
        undetected_TeamB.append(aircraft)
    
    # Initialize list of remaining aircrafts
    remaining_TeamA = []
    remaining_TeamB = []
    
    # Run BVR (Beyond Visual Range) until combat distance is within 10 nautical miles
    print("The BVR (Beyond Visual Range) phase begins!")
    
    while distance > 10:
        # Print the events that occur at the given combat range of BVR
        print(f"\nAt a range of {distance} nautical miles:")
        
        # Detect aircrafts in each team given combat distance
        detected_TeamA  = detection(TeamA, detected_TeamA, distance, 'A')
        print("--------------------------------")
        detected_TeamB = detection(TeamB, detected_TeamB, distance, 'B')
        
        # Check if either team has a target
        if len(detected_TeamA) == 0 and len(detected_TeamB) == 0:
            print("\nNo targets detected!")
            
        elif len(detected_TeamA) == 0: # Team B has no targets
            print("\nTeam B has no targets")
            print("Team A engages!")
            TeamB, detected_TeamB, detected_TeamA = engagement(TeamA, TeamB, detected_TeamA, detected_TeamB, 'A', 'B')
            
        elif len(detected_TeamB) == 0: # Team A has no targets
            print("\nTeam A has no targets")
            print("Team B engages!")
            TeamA, detected_TeamA, detected_TeamB = engagement(TeamB, TeamA, detected_TeamB, detected_TeamA, 'B', 'A')
            
        
        elif random.randint(0, 1) == 1: # Random between 0 and 1 to determine which team engages first
            
            # Team A engages Team B and Team B attempts to evade
            print("\nTeam A engages!")
            TeamB, detected_TeamB, detected_TeamA = engagement(TeamA, TeamB, detected_TeamA, detected_TeamB, 'A', 'B')
            
            # Team B returns fire and Team A attempts to evade
            print("\nTeam B returns fire!")
            TeamA, detected_TeamA, detected_TeamB = engagement(TeamB, TeamA, detected_TeamB, detected_TeamA, 'B', 'A')
            
        else:
            print("\nTeam B engages!")
            # Team B engages Team A and Team A attempts to evade
            TeamA, detected_TeamA, detected_TeamB = engagement(TeamB, TeamA, detected_TeamB, detected_TeamA, 'B', 'A')
            
            # Team A returns fire and Team B attempts to evade
            print("\nTeam A returns fire!")
            TeamB, detected_TeamB, detected_TeamA = engagement(TeamA, TeamB, detected_TeamA, detected_TeamB, 'A', 'B')
            
        # Check if any teams are eliminated by checking health values
        remaining_TeamA = [aircraft.name for aircraft in TeamA]
        remaining_TeamB = [aircraft.name for aircraft in TeamB]
        
        # Check if any teams are eliminated, if not, end BVR phase
        if len(remaining_TeamA) == 0 and len(remaining_TeamB) == 0:
            print("Tie!")
            break
        elif len(remaining_TeamA) == 0:
            print("Team B wins!")
            break
        elif len(remaining_TeamB) == 0:
            print("Team A wins!")
            break
        else:
            distance -= 10 # Update distance value
            continue
        
    # Print the events that occur at WVR now
    print(f"\nRemaining aircraft in Team A: {', '.join(remaining_TeamA)}")
    print(f"\nRemaining aircraft in Team B: {', '.join(remaining_TeamB)}")
    print("\nAt 10km aircraft can now see each other and Within Visual Range (WVR) phase begins!")
    
    # Run WVR (Within Visual Range) phase until one team is eliminated
    # while len(remaining_TeamA) > 0 and len(remaining_TeamB) > 0:
    
    
    return 1
        

def detection(Team, detected, distance, teamName):
    
    # Iterate through each aircraft in the team
    for aircraft in Team:
        
        if aircraft in detected: # Aircraft already detected, skip detection logic
            print(f"The {aircraft.name} ({teamName}) still detected!")
            continue
        
        else: 
            # Generate a random detection threshold with margin of randomness
            detection_threshold = random.uniform(0.25, 0.5) + (10 / distance)
            
            # Compare stealth spec to threshold
            if detection_threshold > aircraft.stealth:
                detected.append(aircraft) # Add aircraft to detected list
                print(f"The {aircraft.name} ({teamName}) now detected!")
            else:
                print(f"The {aircraft.name} ({teamName}) remains undetected.")
    
    return detected

def engagement(Team_shooter, Team_target, detected_shooter, detected_target, teamNameShooter, teamNameTarget):
    # Initialize previous target
    previous_target = None
    
    # Iterate through each aircraft target that was detected under the radar
    for target in detected_target:
        
        # Remove previous target from the team if necessary (It needs to be like this because we are iterating through the list itself)
        if previous_target != None:
            detected_target.remove(previous_target)

        # Choose a random shooter from the shooting team to take down the target
        shooter = random.choice(Team_shooter)
        
        # Determine if shooter is revealed by firing and engaging in target
        reveal_threshold = random.uniform(0, 1)
        if reveal_threshold > shooter.stealth:
            detected_shooter.append(shooter)
            print(f"The {shooter.name} ({teamNameShooter}) targets the {target.name} ({teamNameTarget}), but it reveals its position by firing!")
        else:
            print(f"The {shooter.name} ({teamNameShooter}) targets the {target.name} ({teamNameTarget}) and remains undetected!")
    
        # Determine if the target aircraft evades the missile
        evasion_threshold = random.uniform(0, 1)
        
        # Calculate the evasion chance based on maneuverability and electronic warfare values
        if evasion_threshold > 0.5 * (target.maneuverability + target.EW): 
            for aircraft in Team_target:
                if aircraft.name == target.name:
                    aircraft.health = 0 # Target eliminated
                    Team_target.remove(aircraft) # Remove target from the team
                    previous_target = target
                    print(f"The {target.name} ({teamNameTarget}) was destroyed by {shooter.name} ({teamNameShooter}) via missile!")
                    break
        else:
            print(f"The {target.name} ({teamNameTarget}) evades the {shooter.name}'s ({teamNameShooter}) missile.")
            
    return Team_target, detected_target, detected_shooter

def decide():
    
    
    
    return 1

def dogFight():
    
    # Instead of shooting by number of targets, shoot by number of shooters
    
    return 1

