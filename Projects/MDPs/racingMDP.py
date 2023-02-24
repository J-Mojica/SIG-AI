states = ["cool", "hot", "overheated"]
actions = ["fast", "slow"]
terminal_states = ["overheated"]

def getLegalActions(state, actions, terminal_states):
    if(state in terminal_states):
        return []
    return actions

def getTransitionStatesAndProbs(state, action, transition):
    transitionStatesAndProbs = []
    for next_state in states:
        prob = transition(state, action, next_state)
        if(prob > 0.0):
            transitionStatesAndProbs.append((next_state, prob))
    return transitionStatesAndProbs

def transition(state, action, next_state):
    if(state == "overheated"):
        return 0.0
    if(state == "hot" and action == "fast" and next_state == "overheated"):
        return 1.0
    if(state != "overheated" and next_state != "overheated"):
        return 0.5
    if(next_state == "overheated" and state == "cool"):
        return 0.0
    return 0.0

def reward(state, action, next_state):
    if(state != "overheated" and next_state != "overheated" and action == "fast"):
        return 2.0
    if(state != "overheated" and next_state != "overheated" and action == "slow"):
        return 1.0
    if(next_state == "overheated"):
        return -10.0
    return 0.0