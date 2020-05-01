from statemachine import StateMachine
import include
import matplotlib

for path in include.main_paths:
    # create a supervisor
    supervisor = include.Generator.create_master(include.master_states, include.master_transitions)
    robotL = include.Generator.create_master(include.robotL_states, include.robotL_transitions)
    robotR = include.Generator.create_master(include.robotR_states, include.robotR_transitions)
    print('\n' + str(supervisor))
    print('\n' + str(robotL))
    print('\n' + str(robotR))

    # run supervisor for exemplary path
    print("Executing path: {}".format(path))
    for event in path:

        # launch a transition in our supervisor

        # add slave
        if supervisor.current_state.value == "(czujnik_1&czujnik_2)==0":
            # # TODO: automata 1 (for) slave1
            # ...
            print("------------------------")
            print("(czujnik_1&czujnik_2)=0")
            print(supervisor.current_state)

        if supervisor.current_state.value == "czujnik_1==1":
            # TODO: automata 2 (for) slave2
            ...
            print("------------------------")
            print("czujnik_1=1")
            print(supervisor.current_state)

        if supervisor.current_state.value == "czujnik_2==1":
            # TODO: automata 3 (for) slave3
            ...
            print("------------------------")
            print("czujnik_2=1")
            print(supervisor.current_state)
        if supervisor.current_state.value == "czujnik_3==1":
            # TODO: automata 3 (for) slave3
            ...
            print("------------------------")
            print("czujnik_3=1")
            print(supervisor.current_state)

        if supervisor.current_state.value == "S1&S2==ON":
            # TODO: automata 3 (for) slave3
            ...
            print("------------------------")
            print("S1&S2=ON")
            print(supervisor.current_state)
            # supervisor.current_state.value="dupa"
            # print(supervisor.current_state.value)

            for pathL, pathR in zip(include.rL_paths, include.rR_paths):
                for eventL, eventR in zip(pathL, pathR):
                    if robotL.current_state.value == "L_cycle1==1":
                        print("")
                        print("")
                        print("L_cycle1 = 1")
                        print(robotL.current_state)
                    if robotL.current_state.value == "(L_cycle2&R_cycle2)==1":
                        print("")
                        print("")
                        print("(L_cycle2&R_cycle2) = 1")
                        print(robotL.current_state)
                    if robotL.current_state.value == "L_cycle2==0":
                        print("")
                        print("")
                        print("L_cycle2 = 0")
                        print(robotL.current_state)

                    if robotL.current_state.value == "Flag_Restart == ON":
                        print("")
                        print("")
                        print("Flag_Restart = 1")
                        print(robotL.current_state)

                    if robotR.current_state.value == "R_cycle1==1":
                        print("")
                        print("")
                        print("R_cycle1 = 1")
                        print(robotR.current_state)
                    if robotR.current_state.value == "(L_cycle2&R_cycle2)==1":
                        print("")
                        print("")
                        print("(R_cycle2&R_cycle2) = 1")
                        print(robotR.current_state)
                    if robotR.current_state.value == "R_cycle2==0":
                        print("")
                        print("")
                        print("R_cycle2 = 0")
                        print(robotR.current_state)

                    if robotR.current_state.value == "Flag_Restart == ON":
                        print("")
                        print("")
                        print("Flag_Restart = 1")
                        print(robotR.current_state)

                    include.robotL_transitions[eventL]._run(robotL)
                    include.robotR_transitions[eventR]._run(robotR)

        if supervisor.current_state.value == "(L_cycle2&R_cycle_2)==0":
            # TODO: automata 3 (for) slave3
            ...
            print("------------------------")
            print("(L_cycle2&R_cycle_2)=0")
            print(supervisor.current_state)

        if supervisor.current_state.value == "czujnik_3==0":
            # TODO: automata 3 (for) slave3
            ...
            print("------------------------")
            print("czujnik_3=0")
            print(supervisor.current_state)

        include.master_transitions[event]._run(supervisor)
        # print(supervisor.current_state)
        # print(supervisor.current_state.value)
