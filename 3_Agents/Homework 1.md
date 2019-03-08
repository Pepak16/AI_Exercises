# Homework 1 - Reflex Vacuum Agent

![alt text](img/tda.png "Table Driven / Simple Reflex Agent")

Extend the REFLEX-VACUUM-AGENT program to have 4
locations (4 squares): 

- The agent should only sense and act on the square where it is
located.
    
- Allow any starting square. 

- Use run (20) to test and display results. 

Answer:

        Current                        New
    location    status  action  location    status
    A           Dirty   Suck    A           Clean   
    A           Clean   Right   B           Dirty   
    B           Dirty   Suck    B           Clean   
    B           Clean   Down    D           Dirty   
    D           Dirty   Suck    D           Clean   
    D           Clean   Left    C           Dirty   
    C           Dirty   Suck    C           Clean   
    C           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   
    B           Clean   Down    D           Clean   
    D           Clean   Left    C           Clean   
    C           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   
    B           Clean   Down    D           Clean   
    D           Clean   Left    C           Clean   
    C           Clean   Up      A           Clean   
    A           Clean   Right   B           Clean   
    B           Clean   Down    D           Clean   
    D           Clean   Left    C           Clean
    
    The source code for this reflex vacuum agent is also untouched, 
    so it can be inspected later.