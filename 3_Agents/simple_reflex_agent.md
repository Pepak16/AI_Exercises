# Simple Reflex Agent

![alt text](img/tda.png "Table Driven / Simple Reflex Agent")

## 1. 
Run the module. 

Answer:
    
    Result is as following when running the program first time:
        Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty   
    B           Dirty   left    B           Dirty 

## 2. 
Enter: run(10)

Answer:
    
    The last exercise was using 20 steps, which means it was set to run(20).
    When changing the value to 10 in run(10), 
    the agent will then move only 10 steps in the 2 rooms (environment with A and B):
        
            Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean  
    

## 3. 
Change the SIMPLE_REFLEX_AGENT condition-action rules to return bogus actions, such as Left when
should go Right, or Crash, etc. Rerun the agent. Do the
Actuators allow bogus actions? 

Answer:

    Before the change:
    
    RULE_ACTION = {
        1: 'Suck',
        2: 'Right',
        3: 'Left',
        4: 'NoOp'
    }
    
    After the change bogus change:
    
    RULE_ACTION = {
        1: 'Suck',
        2: 'Left',
        3: 'Right',
        4: 'NoOp'
    }
    
    Status before bogus actions implemented:
    
            Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Left    A           Clean 
    
    Personal note: 
    
    i cannot understand why it wont clean room B at all. 
    It just return to room A when visiting room B.
    
    
    The status when doing the bogus actions:
    
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
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean   
    A           Clean   Left    A           Clean 
    
    Conclusion:
    
    Yes the actuators allows bogus actions, 
    but it will continuously move to Left and since there is 
    not other place left to A, it will stay in that room.