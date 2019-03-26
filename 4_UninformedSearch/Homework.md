# Homework 1 - Goat, Cabbage and Wolf

Result:

    Solution path:
    
    State: ('E', 'E', 'E', 'E') - Depth: 7
    State: ('W', 'E', 'W', 'E') - Depth: 6
    State: ('E', 'E', 'W', 'E') - Depth: 5
    State: ('W', 'E', 'W', 'W') - Depth: 4
    State: ('E', 'E', 'E', 'W') - Depth: 3
    State: ('W', 'W', 'E', 'W') - Depth: 2
    State: ('E', 'W', 'E', 'W') - Depth: 1
    State: ('W', 'W', 'W', 'W') - Depth: 0
    
Personal note:

    Tried to draw the tree in order to gain an understanding in how the exercise works, 
    but it was wrong according to the results though. I must find some program in order to draw
    a tree!
    But the length of the overall depth of the tree is 8 though, where it started from the initial state:
    WWWW and ended in EEEE, the rule was to not break the law with following illegal states:
    
    ('W', 'E', 'E', 'W'),
    ('W', 'W', 'E', 'E')
    
    That's simply because the homework said that (W, E, W, W) 
    represents the (farmer, wolf, goat, cabbage) respectively.
    
    And the rules say that
    - The goat cannot be alone with the cabbage, since it will eat it.
      e.g. ('W', 'W', 'E', 'E')
      
    - The boat can only hold two passengers (so all four passengers cannot move from one side to another at once.
      e.g. (w,w,w,w) or (E,E,E,E)
      
      But idk why the (W,E,E,W) is an illegal rule to be honest.
      
    It ended up with being the following illegal rules, 
    that would be removed if they ever was spotted, according to this function:
    
    
    
        def successor_fn(state):  # Lookup list of successor states
            states = STATE_SPACE[state]
            for stat in states:
                if stat == ('W', 'E', 'E', 'W'):
                    states.remove(('W', 'E', 'E', 'W'))
                if stat == ('W', 'W', 'E', 'E'):
                    states.remove(('W', 'W', 'E', 'E'))
                if stat == ('E', 'E', 'W', 'W'):
                    states.remove(('E', 'E', 'W', 'W'))
                if stat == ('E', 'W', 'W', 'E'):
                    states.remove(('E', 'W', 'W', 'E'))
            return states
            
            
    
    There is more notes about the exercise in the code itself.