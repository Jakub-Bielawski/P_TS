from statemachine import StateMachine
import include

for path in include.main_paths:
    # create a supervisor
    supervisor = include.Generator.create_master(include.master_states, include.master_transitions)
    robot1 = include.Generator.create_master(include.robotL_states, include.robotL_transitions)
    robot2 = include.Generator.create_master(include.robotR_states, include.robotR_transitions)
    print('\n' + str(supervisor))
    print('\n' + str(robot1))
    print('\n' + str(robot2))

    # run supervisor for exemplary path
    print("Executing path: {}".format(path))
    for event in path:

        # launch a transition in our supervisor
        include.master_transitions[event]._run(supervisor)
        print(supervisor.current_state)
        print(supervisor.current_state.value, "!!!")
        # add slave
        if supervisor.current_state.value == "czujnik_1":
            # # TODO: automata 1 (for) slave1
            # ...
            print("Czujnik_1")
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
