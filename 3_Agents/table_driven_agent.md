# Table Driven Agent

![alt text](img/tda.png "Table Driven / Simple Reflex Agent")

## 1. 
Run the module (using run()). 

Answer:

    Done, it shows this result:
    Action	Percepts
    Right 	 [('A', 'Clean')]
    Suck 	 [('A', 'Clean'), ('A', 'Dirty')]
    Left 	 [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean')]

## 2. 
The percepts should now be: [('A', 'Clean'), ('A', 'Dirty'), ('B','Clean')].
– The table contains all possible percept sequences to match with the
percept history.
– Enter:
print (TABLE_DRIVEN_AGENT((B, 'Clean')))
percepts
– Explain the results. 

Answer:

    Done, the result after adding print (TABLE_DRIVEN_AGENT((B, 'Clean'))), is as following:
    Action	Percepts
    Right 	 [('A', 'Clean')]
    Suck 	 [('A', 'Clean'), ('A', 'Dirty')]
    Left 	 [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean')]
    None 	 [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean'), ('B', 'Clean')]

## 3. 
How many table entries would be required if only the current percept was used to select an action rather than the percept history? 

Answer:
    
    0 table entries, since its actions are based on what it perceives in the actual moment, 
    instead of looking up in a history. 

4. ??