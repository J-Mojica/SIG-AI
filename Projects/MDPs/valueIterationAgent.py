from racingMDP import *

def initializeValues(states):
    values = {}
    for state in states:
        values[state] = 0.0
    return values

def runValueIteration(states, actions, legalActions, transition, reward, terminal_states, gamma, iterations):
    # Initialize the value function
    values = initializeValues(states)
    for _ in range(iterations):
        internalValues = values.copy()
        for state in states:
            legalActions = getLegalActions(state, actions, terminal_states)
            if(len(legalActions) > 0):
                Qvalues = [computeQvalue(state, action, transition, reward, internalValues, gamma) for action in legalActions]
                values[state] = max(Qvalues)
    return values

# Compute Q values
def computeQvalue(state, action, transition, reward, values, gamma):
    Qvalue = sum([prob * (reward(state, action, next_state) + gamma * values[next_state]) for next_state, prob in getTransitionStatesAndProbs(state, action, transition)])
    return Qvalue

def extractPolicy(states, actions, getLegalActions, transition, reward, terminal_states, gamma, values):
    policy = {}
    for state in states:
        legalActions = getLegalActions(state, actions, terminal_states)
        if(len(legalActions) > 0):
            for a in legalActions:
                Qvalue = computeQvalue(state, a, transition, reward, values, gamma)
                if(state not in policy):
                    policy[state] = (a, Qvalue)
                else:
                    if(Qvalue > policy[state][1]):
                        policy[state] = (a, Qvalue)
    return policy

# Run value iteration
values = runValueIteration(states, actions, getLegalActions, transition, reward, terminal_states, 1.0, 2)
policy = extractPolicy(states, actions, getLegalActions, transition, reward, terminal_states, 1.0, values)
print(values)
print(policy)