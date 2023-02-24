from racingMDP import *

def initializeValues(states):
    values = {}
    for state in states:
        values[state] = 0.0
    return values

def policyEvaluation(states, actions, policy, transition, reward, terminal_states, gamma):
    # Initialize the value function
    values = initializeValues(states)
    while(True):
        internalValues = values.copy()
        for state in states:
                action = policy[state][0]
                if(action != None):
                    values[state] = computeQvalue(state, action, transition, reward, internalValues, gamma)
        if(max([abs(values[state] - internalValues[state]) for state in states]) < 0.01):
            break
    return values

# Compute Q values
def computeQvalue(state, action, transition, reward, values, gamma):
    Qvalue = sum([prob * (reward(state, action, next_state) + gamma * values[next_state]) for next_state, prob in getTransitionStatesAndProbs(state, action, transition)])
    return Qvalue

def policyExtraction(states, actions, policy, getLegalActions, transition, reward, terminal_states, gamma, values):
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

def policyIteration(states, actions, getLegalActions, transition, reward, terminal_states, gamma, iterations):
    # Initialize the policy
    policy = {}
    for state in states:
        policy[state] = (actions[1], 0.0)
    for _ in range(iterations):
        values = policyEvaluation(states, actions, policy, transition, reward, terminal_states, gamma)
        policy = policyExtraction(states, actions, policy, getLegalActions, transition, reward, terminal_states, gamma, values)
    return policy


# Run policy iteration
policy = policyIteration(states, actions, getLegalActions, transition, reward, terminal_states, 0.9, 2)
print(policy)