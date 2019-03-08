# Reflex Vacuum Agent

![alt text](img/tda.png "Table Driven / Simple Reflex Agent")

## 1. 
Run the module. 

Answer:
    
    Result is as following when running the program first time:
    
            Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Suck    B           Clean   
    B           Clean   Down    C           Dirty   
    C           Dirty   Suck    C           Clean   
    C           Clean   Left    D           Dirty   
    D           Dirty   Suck    D           Clean   
    D           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   
    B           Clean   Down    C           Clean   
    C           Clean   Left    D           Clean   
    D           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   
    B           Clean   Down    C           Clean   
    C           Clean   Left    D           Clean   
    D           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   
    B           Clean   Down    C           Clean   
    C           Clean   Left    D           Clean  

## 2. 
Enter: run(10)

Answer:
    
    The last exercise was using 20 steps, which means it was set to run(20).
    When changing the value to 10 in run(10), 
    the agent will then move only 10 steps in the 4 different rooms:
    
        Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Suck    B           Clean   
    B           Clean   Down    C           Dirty   
    C           Dirty   Suck    C           Clean   
    C           Clean   Left    D           Dirty   
    D           Dirty   Suck    D           Clean   
    D           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   

## 3. 
Should bogus actions be able to corrupt the
environment? Change the REFLEX_VACUUM_AGENT
to return bogus actions, such as Left when should go
Right, etc. Run the agent. Do the Actuators allow bogus
actions?

Answer:

    Bogus actions = fake/unfair.
    No they shouldn't, since then the agent will not do what it is intended to do.
    To test this, values such as Left and Right is manipulated to do the reversed 
    action instead, e.g. Left instead of Right and Right instead of Left.
    
    Before the change:
    
    def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    if loc_st[1] == 'Dirty':
        return 'Suck'
    elif loc_st[0] == A:
        return 'Right'
    elif loc_st[0] == B:
        return 'Down'
    elif loc_st[0] == C:
        return 'Left'
    elif loc_st[0] == D:
        return 'Up'
        
    What code looks like after bogus actions:
    
    def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    if loc_st[1] == 'Dirty':
        return 'Suck'
    elif loc_st[0] == A:
        return 'Left'
    elif loc_st[0] == B:
        return 'Down'
    elif loc_st[0] == C:
        return 'Right'
    elif loc_st[0] == D:
        return 'Up'

    Result:
        
            Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean  
    
    
    
    Conclusion:
    
    The actuators allow bogus actions, 
    but it will (in this case) just look for a room which 
    is already cleaned in 10 times. So if room A is cleaned already, 
    it will just go back to the same room, when turning to left.
    It is possible, but not flexible, hence the agent is not fullfilling its purpose.