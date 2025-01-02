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
    
    # Initialize list of remaining aircrafts
    remaining_TeamA = []
    remaining_TeamB = []
    
    # Run BVR (Beyond Visual Range) until combat distance is within 10 nautical miles
    while distance > 10:
        # Print the events that occur at the given combat range of BVR
        print("The BVR (Beyond Visual Range) phase begins!")
        print(f"\nAt a range of {distance} nautical miles:")
        
        # Detect aircrafts in each team given combat distance
        detected_TeamA = detection(TeamA, detected_TeamA, distance)
        detected_TeamB = detection(TeamB, detected_TeamB, distance)
        
        # Random between 0 and 1 to determine which team engages first
        if random.randint(0, 1) == 1:
            print("Team A engages first!")
            
            # Team A engages Team B and Team B attempts to evade
            targeted_TeamB, detected_TeamA = engagement(TeamA, detected_TeamB, detected_TeamA)
            TeamB, targeted_TeamB, detected_TeamB = evade(TeamB, targeted_TeamB, detected_TeamB)
            
            # Team B returns fire and Team A attempts to evade
            targeted_TeamA, detected_TeamB = engagement(TeamB, detected_TeamA, detected_TeamB)
            TeamA, targeted_TeamA, detected_TeamA = evade(TeamA, targeted_TeamA, detected_TeamA)
            
        else:
            print("Team B engages first!")
            
            # Team B engages Team A and Team A attempts to evade
            targeted_TeamA, detected_TeamB = engagement(TeamB, detected_TeamA, detected_TeamB)
            TeamA, targeted_TeamA, detected_TeamA = evade(TeamA, targeted_TeamA, detected_TeamA)
            
            # Team A returns fire and Team B attempts to evade
            targeted_TeamB, detected_TeamA = engagement(TeamA, detected_TeamB, detected_TeamA)
            TeamB, targeted_TeamB, detected_TeamB = evade(TeamB, targeted_TeamB, detected_TeamB)
            
        # Check if any teams are eliminated by checking health values
        remaining_TeamA = [aircraft['name'] for aircraft in TeamA if aircraft['health'] > 0]
        remaining_TeamB = [aircraft['name'] for aircraft in TeamB if aircraft['health'] > 0]
        
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
            continue
            distance -= 10 # Update distance value
        
    # Print the events that occur at WVR now
    print(f"\nRemaining aircraft in Team A: {', '.join(remaining_TeamA)}")
    print(f"\nRemaining aircraft in Team B: {', '.join(remaining_TeamB)}")
    print("\nAt 10km aircraft can now see each other and Within Visual Range (WVR) phase begins!")
    
    # Run WVR (Within Visual Range) phase until one team is eliminated
    while len(remaining_TeamA) > 0 and len(remaining_TeamB) > 0:
        

# Detection Phase (Get detect aircrafts in each team given combat distance) 
def detection(Team, detected, distance):
    
    # Iterate through each aircraft in the team
    for aircraft in Team:
        
        # Check if the aircraft is already detected
        if aircraft["name"] in detected:
            continue
        else:
            # Generate a random detection threshold
            detection_threshold = random.uniform(0, 1) - (distance / 200)
            
            # Compare stealth spec to threshold
            if detection_threshold > aircraft["stealth"]:
                detected.append(aircraft["name"])
                print(f"{aircraft['name']} detected! (Stealth: {aircraft['stealth']:.2f}, Threshold: {detection_threshold:.2f})")
            else:
                print(f"{aircraft['name']} remains undetected. (Stealth: {aircraft['stealth']:.2f}, Threshold: {detection_threshold:.2f})")
    
    return detected

# Engagement Phase (Detected aircraft are targeted)
def engagement(Team_shooter, detected_target, detected_shooter):
    # Initialize the targeted aircrafts
    targeted = []

    for target in detected_target:

        # Choose a random shooter from the shooting team
        shooter = random.choice(Team_shooter)
        
        # Determine if shooter is revealed by firing and engaging in target
        reveal_threshold = random.uniform(0, 1)
        if reveal_threshold > shooter["stealth"]:
            detected_shooter.append(shooter)
            print(f"The {shooter['name']} targets the {target['name']}, but it reveals its position by firing!")
        else:
            print(f"The {shooter['name']} targets the {target['name']} and fires undetected!")
    
    return targeted, detected_shooter
    
# Evasion Phase (When an aircraft is targeted, it attempts to evade the missile)
def evade(team, targeted, detected):
    
    # Iterate through each targeted aircraft
    for target in targeted:
        # Determine if the target aircraft evades the missile
        evasion_threshold = random.uniform(0, 1)
        
        # Calculate the evasion chance based on maneuverability and electronic warfare values
        if evasion_threshold > 0.5 * (target['maneuverability'] + target["EW"]): 
            for aircraft in team:
                if aircraft['name'] == target['name']:
                    aircraft['health'] = 0 # Target eliminated
            detected.remove(target['name'])
            targeted.remove(target)
            print(f"The {target['name']} is hit by the missile")
        else:
            print(f"{target['name']} evades the missile.")
            
    return team, targeted, detected


def decide():
    
    
    
    return 1

def engage_WVR():
    
    


def evade_gun():
    
    
    
    return 1

