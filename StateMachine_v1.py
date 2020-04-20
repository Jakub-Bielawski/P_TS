from statemachine import StateMachine, State, Transition

# define states for a master (way of passing args to class)
options = [
    {"name": "Wjazd czesci w strefe robocza", "initial": True, "value": "idle"},  # 0
    {"name": "Spowolnienie tasmy", "initial": False, "value": "czujnik_1"},  # 1
    {"name": "Zatrzymanie tasmy i zamkniecie zatrzaskow", "initial": False, "value": "b"},  # 2
    {"name": "Zezwolenie na prace", "initial": False, "value": "c"},  # 3
    {"name": "Sprawdzenie pozycji robota", "initial": False, "value": "f"},  # 4
    {"name": "Wylaczenie zezwolenian prace robota i zwolnienie zatrzaskow", "initial": False, "value": "g"},  # 5
    {"name": "Wlaczenie tasmy", "initial": False, "value": "h"}]  # 6

options_Robot1 = [
    {"name": "Pozycja domowa", "initial": True, "value": "0"},  # 0
    {"name": "Sekwencja 1", "initial": False, "value": "1"},  # 1
    {"name": "Sekwencja 2", "initial": False, "value": "2"},  # 2
    {"name": "Srzygotowanie do ponownego wykonania", "initial": False, "value": "3"}  # 3

]

options_Robot2 = [
    {"name": "Pozycja domowa", "initial": True, "value": "0"},  # 0
    {"name": "Sekwencja 1", "initial": False, "value": "1"},  # 1
    {"name": "Sekwencja 2", "initial": False, "value": "2"},  # 2
    {"name": "Srzygotowanie do ponownego wykonania", "initial": False, "value": "3"}  # 3
]
# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in options]
robot1_states = [State(**opt) for opt in options_Robot1]
robot2_states = [State(**opt) for opt in options_Robot2]
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
        transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
        master_transitions[op_identifier] = transition

        # add transition to source state
        master_states[from_idx].transitions.append(transition)

# create transitions for a robot1 (as a dict)
robot1_transitions = {}
for indices in form_to_R1:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "r1_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(robot1_states[from_idx], robot1_states[to_idx], identifier=op_identifier)
        robot1_transitions[op_identifier] = transition

        # add transition to source state
        robot1_states[from_idx].transitions.append(transition)

# create transitions for a robot2 (as a dict)
robot2_transitions = {}
for indices in form_to_R2:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "r2_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(robot2_states[from_idx], robot2_states[to_idx], identifier=op_identifier)
        robot2_transitions[op_identifier] = transition

        # add transition to source state
        robot2_states[from_idx].transitions.append(transition)


# create a generator class
class Generator(StateMachine):
    states = []
    transitions = []
    states_map = {}
    current_state = None

    def __init__(self, states, transitions):

        # creating each new object needs clearing its variables (otherwise they're duplicated)
        self.states = []
        self.transitions = []
        self.states_map = {}
        self.current_state = states[0]

        # create fields of states and transitions using setattr()
        # create lists of states and transitions
        # create states map - needed by StateMachine to map states and its values
        for s in states:
            setattr(self, str(s.name).lower(), s)
            self.states.append(s)
            self.states_map[s.value] = str(s.name)

        for key in transitions:
            setattr(self, str(transitions[key].identifier).lower(), transitions[key])
            self.transitions.append(transitions[key])

        # super() - allows us to use methods of StateMachine in our Generator object
        super(Generator, self).__init__()

    # define a printable introduction of a class
    def __repr__(self):
        return "{}(model={!r}, state_field={!r}, current_state={!r})".format(
            type(self).__name__, self.model, self.state_field,
            self.current_state.identifier,
        )

    # method of creating objects in a flexible way (we can define multiple functions
    # which will create objects in different ways)
    @classmethod
    def create_master(cls, states, transitions) -> 'Generator':
        return cls(states, transitions)


# create paths from transitions (exemplary)
path_1 = ["m_0_1"]
# , "m_1_2", "m_2_1", "m_1_3", "m_3_4"
# path_2 = ["m_0_2", "m_2_3", "m_3_2", "m_2_4"]
# path_3 = ["m_0_3", "m_3_1", "m_1_2", "m_2_4"]
# paths = [path_1, path_2, path_3]
paths = [path_1]
# execute paths
for path in paths:

    # create a supervisor
    supervisor = Generator.create_master(master_states, master_transitions)
    robot1 = Generator.create_master(robot1_states, robot1_transitions)
    robot2 = Generator.create_master(robot2_states, robot2_transitions)
    print('\n' + str(supervisor))
    print('\n' + str(robot1))
    print('\n' + str(robot2))

    # run supervisor for exemplary path
    print("Executing path: {}".format(path))
    for event in path:

        # launch a transition in our supervisor
        master_transitions[event]._run(supervisor)
        print(supervisor.current_state)
        print(supervisor.current_state.value, "!!!")
        # add slave
        if supervisor.current_state.value == "czujnik_1":
            # # TODO: automata 1 (for) slave1
            # ...
            print("stan_A")
            # next = "m_1_2"
            path.append("m_1_2")
            print(supervisor.current_state.value)

        if supervisor.current_state.value == "b":
            # TODO: automata 2 (for) slave2
            ...
            print("Stan_b")

        if supervisor.current_state.value == "c":
            # TODO: automata 3 (for) slave3
            ...
            print("Stan_c")

        if supervisor.current_state.value == "f":
            # TODO: automata 3 (for) slave3
            ...
            print("Supervisor done!")
