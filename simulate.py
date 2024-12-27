# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Jamie Henson
# Run simulations of the senario
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import csv
import random
import numpy as np

def runSimulation(TeamA, TeamB, TeamA_specs, TeamB_specs):
    
    # Initialize the team scores and desired number of simulations runs
    TeamA_win = 0
    TeamB_win = 0
    runs = 20
    
    # Run the simulation the desired number of times 
    for run in range(runs):
        
        # Run BVR simulation
        TeamA, TeamB = BVR(TeamA, TeamA_specs, TeamB, TeamB_specs)
        
        # Continue dog fight until no aircrafts are left in one of the teams
        while True:
            
            
            
            
            
            # Run WVR simulation
            
            
            # Combat simulation
            if all(x == 0 for x in TeamA):
                TeamB_win += 1
                break
            elif all(x == 0 for x in TeamB):
                TeamA_win += 1
                break
            else:
                continue
    
    # Calculate the win percentage of each team
    result = [TeamA_win/runs, TeamB_win/runs]

    return result, runs

def BVR(TeamA, TeamB):
    
    distance = 50 # Initial distance between the two teams [nautical miles]
    
    # (Detection phase) Find the aircrafts with lowest stealth value as they will expose the team
    min_RCS = min(TeamA[:,5])
    
    # Keep lowering the distance until one team detects another
    
    
    # Engagement phase
    
    
    # Evasion phase
    
    
    # Merge phase into WVR
    
    
    
    return TeamA, TeamB


def WVR(TeamA, TeamB):
    
    
    return 1
    
    
    
    
