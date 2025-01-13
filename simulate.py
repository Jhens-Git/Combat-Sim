# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson and Gabriel Scott
# Run simulations logic of the flight combat senario
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import random
import time

# TrueColor ANSI escape codes
BLUE = '\033[38;2;0;0;255m'
RED = '\033[38;2;255;0;0m'
BOLD = '\033[1m'
RESET = '\033[0m'

def runSimulation(TeamA, TeamB):
    # Run Beyond Visual Range (BVR)
    TeamA, TeamB = BVR(TeamA, TeamB)
    
    # Run Within Visual Range (WVR)
    remaining = WVR(TeamA, TeamB)
    
    # Return the results of the simulation
    if remaining == True:
        return True
    elif remaining == False:
        return False
    else:
        print(f"\nRemaining aircraft in the winning team: {', '.join(remaining)}")
        return True
    
def BVR(TeamA, TeamB):
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
    
    # Run BVR (Beyond Visual Range) until combat distance is within 10 nautical miles
    print("\nThe BVR (Beyond Visual Range) phase begins!")
    time.sleep(1) # Pause for 1 second
    
    while distance >= 10:
        # Print the events that occur at the given combat range of BVR
        print(f"\n{BOLD}At a range of {distance} nautical miles:{RESET}")
        time.sleep(1) # Pause for 1 second
        
        # Detect aircrafts in each team given combat distance
        detected_TeamA  = detection(TeamA, detected_TeamA, distance, 'A')
        print("<------==================------>")
        detected_TeamB = detection(TeamB, detected_TeamB, distance, 'B')
        
        # Check if either team has a target
        if len(detected_TeamA) == 0 and len(detected_TeamB) == 0:
            print("\nNo targets detected on either team!")
            
        elif len(detected_TeamA) == 0: # Team B has no targets
            print(f"\n{BLUE}Team B{RESET} has no targets")
            print(f"{RED}Team A{RESET} engages!")
            TeamB, detected_TeamB, detected_TeamA = engagement(TeamA, TeamB, detected_TeamA, detected_TeamB, 'A', 'B')
            
        elif len(detected_TeamB) == 0: # Team A has no targets
            print(f"\n{RED}Team A{RESET} has no targets")
            print(f"{BLUE}Team B{RESET} engages!")
            TeamA, detected_TeamA, detected_TeamB = engagement(TeamB, TeamA, detected_TeamB, detected_TeamA, 'B', 'A')
        
        elif random.randint(0, 1) == 1: # Random between 0 and 1 to determine which team engages first
            
            # Team A engages Team B and Team B attempts to evade
            print(f"\n{RED}Team A{RESET} engages!")
            TeamB, detected_TeamB, detected_TeamA = engagement(TeamA, TeamB, detected_TeamA, detected_TeamB, 'A', 'B')
            if len(TeamB) == 0: # Team B cannot return fire
                break
            # Team B returns fire and Team A attempts to evade
            print(f"\n{BLUE}Team B{RESET} returns fire!")
            TeamA, detected_TeamA, detected_TeamB = engagement(TeamB, TeamA, detected_TeamB, detected_TeamA, 'B', 'A')
        
        else:
            print(f"\n{BLUE}Team B engages!{RESET}")
            # Team B engages Team A and Team A attempts to evade
            TeamA, detected_TeamA, detected_TeamB = engagement(TeamB, TeamA, detected_TeamB, detected_TeamA, 'B', 'A')
            if len(TeamA) == 0: # Team A cannot return fire
                break
            # Team A returns fire and Team B attempts to evade
            print(f"\n{RED}Team A returns fire!{RESET}")
            TeamB, detected_TeamB, detected_TeamA = engagement(TeamA, TeamB, detected_TeamA, detected_TeamB, 'A', 'B')
            
        # Check if any teams are eliminated by checking health values
        remaining_TeamA = [aircraft.ID for aircraft in TeamA]
        remaining_TeamB = [aircraft.ID for aircraft in TeamB]
        
        # Check if any teams are eliminated, if not, end BVR phase and most to WVR
        if len(remaining_TeamA) == 0 and len(remaining_TeamB) == 0:
            print("Tie!")
            break
        elif len(remaining_TeamA) == 0:
            print(f"{BLUE}Team B wins!{RESET}")
            break
        elif len(remaining_TeamB) == 0:
            print(f"{RED}Team A wins!{RESET}")
            break
        else:
            distance -= 20 # Update distance value
            continue
        
    # Print the events at transition from BVR to WVR
    print(f"\nRemaining aircraft in {RED}Team A{RESET}: {', '.join(remaining_TeamA)}")
    print(f"\nRemaining aircraft in {BLUE}Team B{RESET}: {', '.join(remaining_TeamB)}")
    
    # Return the remaining aircrafts in each team
    return TeamA, TeamB
        
def WVR(TeamA, TeamB):
    
    print("\nAt 5km aircraft can now see each other and Within Visual Range (WVR) phase begins!")
    
    # Run WVR (Within Visual Range) phase until one team is eliminated
    while len(TeamA) > 0 and len(TeamB) > 0:
        
        # If both team have one aircraft remaining, switch to dog fight only
        if len(TeamA) == 1 and len(TeamB) == 1:
            print("\nOne aircraft remaining in each team, they engage each other in a final dogfight!")
            TeamA, TeamB = dogFight(TeamA, TeamB)
            
        else:
            if random.randint(0, 1) == 1: # Team A engages in strike/dogfight
                if len(TeamA) == 1: # Team A has one aircraft remaining, engage in dogfight only
                    TeamA, TeamB = dogFight(TeamA, TeamB)
                else: # Team A decides between strike or dogfight approach is appropriate
                    go_all_in = random.randint(0, 1)
                    if go_all_in == True:
                        TeamB = strike(TeamA, TeamB, 'A', 'B') 
                    else:
                        TeamA, TeamB = dogFight(TeamA, TeamB)
            
            else: # Team B engages in strike/dogfight
                if len(TeamB) == 1: # Team B has one aircraft remaining, engage in dogfight only
                    TeamB, TeamA = dogFight(TeamB, TeamA)
                else: # Team B decides between strike or dogfight approach is appropriate
                    go_all_in = random.randint(0, 1)
                    if go_all_in == True:
                        TeamA = strike(TeamB, TeamA, 'B', 'A') 
                    else:
                        TeamB, TeamA = dogFight(TeamB, TeamA)
            
    # Check which team is eliminated and their remaining aircrafts in the winning team
    time.sleep(1) # Pause for 1 second
    if len(TeamA) == 0 and len(TeamB) == 0:
        print("\nTie!")
        return True
    elif len(TeamA) == 0:
        print(f"\n{BLUE}Team B wins!{RESET}")
        return [aircraft.ID for aircraft in TeamB]
    elif len(TeamB) == 0:
        print(f"\n{RED}Team A wins!{RESET}")
        return [aircraft.ID for aircraft in TeamA]
    else:
        print("\nError: Simulation failed to determine winner!")
        return False

def detection(Team, detected, distance, teamName):
    # Iterate through each aircraft in the team
    for aircraft in Team:
        time.sleep(0.2) # Pause for 0.2 second
        
        if aircraft.name in detected: # Aircraft already detected, skip detection logic
            print(f"The {aircraft.name} ({teamName}) still detected!")
        
        else: 
            # Generate a random detection threshold with margin of randomness
            detection_threshold = random.uniform(0.25, 0.75) + (10 / distance)
            
            # Compare stealth spec to threshold
            if detection_threshold > aircraft.stealth:
                detected.append(aircraft.name) # Add aircraft to detected list
                print(f"The {aircraft.name} ({teamName}) now detected!")
            else:
                print(f"The {aircraft.name} ({teamName}) remains undetected.")
    
    return detected

def engagement(Team_shooter, Team_target, detected_shooter, detected_target, teamNameShooter, teamNameTarget):  
    # Initialized array of destroyed aircrafts
    destroyed = []
    
    # Iterate through each aircraft target that was detected under the radar
    for target in detected_target:
        time.sleep(1) # Pause for 1 second

        # Choose a random shooter from the shooting team to take down the target
        shooter = (random.choice(Team_shooter)).name

        # Check if the aircraft is currently detected, if so, then it is at revealed state
        revealed = False
        for detected in detected_shooter:
            if detected == shooter:
                revealed = True
                break
            elif detected != shooter:
                revealed = False
        
        # If aircraft is currently undetected, run odds of it being detected when firing
        if revealed == True:  
            print(f"The {shooter} ({teamNameShooter}) targets the {target} ({teamNameTarget})!")
        elif revealed == False:
            # Get the shooter stealth value
            for aircraft in Team_shooter:
                if aircraft.name == shooter:
                    stealth = aircraft.stealth
            # Determine if shooter is revealed by firing and engaging in target (Gen 4 nearly always reveals itself)
            reveal_threshold = random.uniform(0.5, 1)
            if reveal_threshold > stealth:
                detected_shooter.append(shooter)
                print(f"The {shooter} ({teamNameShooter}) targets the {target} ({teamNameTarget}), but it reveals its position by firing!")
            else:
                print(f"The {shooter} ({teamNameShooter}) targets the {target} ({teamNameTarget}) and remains undetected!")
        elif revealed == 'no targets':
            continue # No targets to hit
        else:
            print("Something went wrong in detection()")
            
        # Determine if the target aircraft evades the missile
        Team_target, evaded = evade(shooter, teamNameShooter, target, Team_target, teamNameTarget, 'LongRangeMissile')
        
        # Remove target from detected targets list
        if evaded == False:
            destroyed.append(target)
            
    # Remove destroyed aircrafts from detected targets list
    for target in destroyed:
        if target in detected_target:
            detected_target.remove(target)
            
    return Team_target, detected_target, detected_shooter

def strike(strikers, targets, strikersName, targetName):
    time.sleep(1) # Pause for 1 second
    
    # Pick a random target in the opposing team
    target = (random.choice(targets)).name
    print(f"{BOLD}Team {strikersName} performs a strike on {target}{RESET}")
    
    # Each aircraft shoots the target
    for striker in strikers: 
        targets, evaded = evade(striker.name, strikersName, target, targets, targetName, 'ShortRangeMissile') # Note that striker.name was necessary for evade() to work
        
        # Stop shooting if target is already destroyed
        if evaded == False:
            break
    
    return targets

def dogFight(Team1, Team2):
    time.sleep(1) # Pause for 1 second
    
    # Pick a random aircrafts from both teams in a dogfight until annihilation
    aircraft1 = (random.choice(Team1)).name
    aircraft2 = (random.choice(Team2)).name
    
    print(f"\n{BOLD}{aircraft1} and {aircraft2} engage in a head-to-head dogfight!{RESET}")
    
    # Keep fighting until one aircraft is eliminated
    dogfight = True
    while dogfight == True:

        # Decide between using missiles or gun based on distance randomly [meters]
        distance = random.randint(1, 5000)
        if distance > 2500:
            attackType = 'ShortRangeMissile'
        else:   
            attackType = 'Gun'
        
        # Aircraft 1 attacks first and Aircraft 2 evades
        Team2, evaded = evade(aircraft1, 'A', aircraft2, Team2, 'B', attackType)
        
        # End dogfight if aircraft is destroyed
        if evaded == False:
            time.sleep(1) # Pause for 1 second
            print(f"The {aircraft1} stands victorious over the {aircraft2} in a dogfight!")
            break
        
        # Aircraft 2 returns fire and Aircraft 1 evades 
        Team1, evaded = evade(aircraft2, 'B', aircraft1, Team1, 'A', attackType)
        
        # End dogfight if aircraft is destroyed
        if evaded == False:
            time.sleep(1) # Pause for 1 second
            print(f"The {aircraft2} stands victorious over the {aircraft1} in a dogfight!")
            break
    
    return Team1, Team2

def evade(shooter, teamNameShooter, target, Team_target, teamNameTarget, attackType):
    time.sleep(1) # Pause for 1 second
    
    # Get the target's manuverability and electronic warfare value from the team dictionary
    for aircraft in Team_target:
        if aircraft.name == target:
            maneuverability = aircraft.maneuverability 
            Ew = aircraft.EW # For some reasonn, EW stands for Encoded Warning, so EW isnt an appropriate variable name
    
    if attackType == 'LongRangeMissile':
        # Determine if the target aircraft evades the missile
        evasion_threshold = random.uniform(0, 1)
        
        # Calculate the evasion chance based on maneuverability and electronic warfare values
        if evasion_threshold > 0.5 * (maneuverability + Ew): 
            for aircraft in Team_target:
                if aircraft.name == target:
                    aircraft.health = 0 # Target eliminated
                    print(f"The {target} ({teamNameTarget}) was destroyed by {shooter} ({teamNameShooter}) via missile!")
                    evaded = False
                    break
        else:
            print(f"The {target} ({teamNameTarget}) evades the {shooter}'s ({teamNameShooter}) missile.")
            evaded = True
    
    elif attackType == 'ShortRangeMissile':
        # Determine if the target aircraft evades the barrage missiles
        evasion_threshold = random.uniform(0.5, 1)
        
        # Calculate the evasion chance based on maneuverability and electronic warfare values
        if evasion_threshold > (0.75 * maneuverability + 0.25 * Ew): 
            for aircraft in Team_target:
                if aircraft.name == target:
                    aircraft.health = 0 # Target eliminated
                    print(f"The {target} ({teamNameTarget}) was destroyed by {shooter} ({teamNameShooter}) via missile!")
                    evaded = False
                    break
        else: # The aircraft evades this missile
            print(f"The {target} ({teamNameTarget}) evades the {shooter}'s ({teamNameShooter}) missile.")
            evaded = True
            
    elif attackType == 'Gun':
        # Determine if the target aircraft evades the gun fire
        evasion_threshold = random.uniform(0.75, 1)
        
        # Calculate the evasion chance based on maneuverability and electronic warfare values
        if evasion_threshold > maneuverability: 
            for aircraft in Team_target:
                if aircraft.name == target:
                    aircraft.health -= random.randint(20, 100) # Aircraft takes damage
                    
                    # Check if the aircraft is destroyed
                    if aircraft.health <= 0:
                        aircraft.health = 0
                        print(f"The {target} ({teamNameTarget}) was destroyed by {shooter} ({teamNameShooter}) via gun!")
                        evaded = False
                    else:
                        print(f"The {target} ({teamNameTarget}) was damanged but not destroyed by {shooter}'s ({teamNameShooter}) gun!")
                        evaded = True
                    break
        else:
            print(f"The {target} ({teamNameTarget}) evades the {shooter}'s ({teamNameShooter}) gun fire.")
            evaded = True
            
    else:
        print("Error: Invalid attack type!")
        return 'error'
    
    # Remove target from the team
    if evaded == False:
        Team_target.remove(aircraft)
        
    # Return the updated team
    return Team_target, evaded
