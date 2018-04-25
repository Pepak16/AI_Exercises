A = 'A'
B = 'B'
C = 'C'
D = 'D'
state = {}
action = None
model = {A: None, B: None, C: None, D: None}  # Initially ignorant

RULE_ACTION = {
}

rules = {
}
# Ex. rule (if location == A && Dirty then rule 1)

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}


def INTERPRET_INPUT(input):  # No interpretation
    return input


def RULE_MATCH(state, rules):  # Match rule for a given state
    rule = rules.get(tuple(state))
    return rule


def UPDATE_STATE(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == 'Clean':
        state = (A, B, 'Clean')
        # Model consulted only for A and B Clean
    model[location] = status  # Update the model state
    return state


def REFLEX_AGENT_WITH_STATE(percept):
    global state, action
    state = UPDATE_STATE(state, action, percept)
    rule = RULE_MATCH(state, rules)
    action = RULE_ACTION[rule]
    return action


def Sensors():  # Sense Environment
    location = Environment['Current']
    return (location, Environment[location])


def Actuators(action):  # Modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    # From position A to B and B back to A
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A
    # From position B to C and C back to B
    elif action == 'Down' and location == B:
        Environment['Current'] = C
    elif action == 'Up' and location == C:
        Environment['Current'] = B
    # From position C to D and D back to C
    elif action == 'Left' and location == C:
        Environment['Current'] = D
    elif action == 'Right' and location == D:
        Environment['Current'] = C
    # From position D to A and A back to D
    elif action == 'Up' and location == D:
        Environment['Current'] = A
    elif action == 'Down' and location == A:
        Environment['Current'] = D


def run(n):  # run the agent through n steps
    print('    Current                        New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_AGENT_WITH_STATE(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == '__main__':
    run(20)
