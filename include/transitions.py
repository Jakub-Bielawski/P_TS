from statemachine import Transition

import include.states as st

# valid transitions for a master (indices of states from-to)
form_to = [
    [0, [1]],
    [1, [2]],
    [2, [3]],
    [3, [4]],
    [4, [4, 5]],
    [5, [6]],
    [6, [0]]
]

form_to_R1 = [
    [0, [1]],
    [1, [2, 3]],
    [2, [3, 0]],
    [3, [0]]
]
form_to_R2 = [
    [0, [1]],
    [1, [2, 3]],
    [2, [3, 0]],
    [3, [0]]
]

# create transitions for a master (as a dict)
master_transitions = {}
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(st.master_states[from_idx], st.master_states[to_idx], identifier=op_identifier)
        master_transitions[op_identifier] = transition

        # add transition to source state
        st.master_states[from_idx].transitions.append(transition)

# create transitions for a robot1 (as a dict)
robotL_transitions = {}
for indices in form_to_R1:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "r1_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(st.robotL_states[from_idx], st.robotL_states[to_idx], identifier=op_identifier)
        robotL_transitions[op_identifier] = transition

        # add transition to source state
        st.robotL_states[from_idx].transitions.append(transition)

# create transitions for a robot2 (as a dict)
robotR_transitions = {}
for indices in form_to_R2:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "r2_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(st.robotR_states[from_idx], st.robotR_states[to_idx], identifier=op_identifier)
        robotR_transitions[op_identifier] = transition

        # add transition to source state
        st.robotR_states[from_idx].transitions.append(transition)

