from statemachine import Transition

import setup.states as st

# valid transitions for a master (indices of states from-to)
from_to = [
    [0, [1]],
    [1, [2]],
    [2, [3]],
    [3, [4]],
    [4, [4, 5]],
    [5, [6]],
    [6, [0]]
]

from_to_R1 = [
    [0, [1]],
    [1, [2, 3]],
    [2, [3, 0]],
    [3, [0]]
]
from_to_R2 = [
    [0, [1]],
    [1, [2, 3]],
    [2, [3, 0]],
    [3, [0]]
]

master_transitions = {}
robotL_transitions = {}
robotR_transitions = {}


def transitionsCreate(name, statesmachine, transitionsMachine, fromto):
    for indices in fromto:
        from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
        for to_idx in to_idx_tuple:  # iterate over destinations from a source state
            op_identifier = name.format(from_idx, to_idx)  # parametrize identifier of a transition

            # create transition object and add it to the master_transitions dict
            transition = Transition(statesmachine[from_idx], statesmachine[to_idx], identifier=op_identifier)
            transitionsMachine[op_identifier] = transition

            # add transition to source state
            statesmachine[from_idx].transitions.append(transition)


transitionsCreate("m_{}_{}", st.master_states, master_transitions, from_to)
transitionsCreate("L_{}_{}", st.robotL_states, robotL_transitions, from_to_R1)
transitionsCreate("R_{}_{}", st.robotR_states, robotR_transitions, from_to_R2)
