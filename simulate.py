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
    
    # Initialize list of aircraft undetected (All aircrafts will start off undetected)
    undetected_TeamA = []
    undetected_TeamB = []
    for aircraft in TeamA:
        undetected_TeamA.append(aircraft)
    for aircraft in TeamA:
        undetected_TeamB.append(aircraft)
    
    # Run BVR (Beyond Visual Range) until combat distance is within 10 nautical miles
    while distance > 10:
        # Print the events that occur at the given combat range
        print(f"\nAt a range of {distance} nautical miles:")
        
        # Detection Phase (Get detect aircrafts in each team given combat distance)

        
        
        
        # Engagement Phase (Detected aircraft are targeted)
        


        
        # Reveal Mechanics (An undetected aircraft may reveal itself if engaged)

        
        
        
        # Evasion Phase (When an aircraft is targeted, it attempts to evade the missile)
 
        
        

    
        
        
        # Update distance value
        distance -= 10
    
    
    # Run BVR (Beyond Visual Range) simulation

    # while each team has an aircraft remaining
    
        # Targetting team decides whether to use a 


            
def detection():

    # 

    return 1

def engagement():
    
    
    
    return 1
    
def reveal():



    return 1

def evade():
    
    
    
    
    return 1


def decide():
    
    
    
    return 1
