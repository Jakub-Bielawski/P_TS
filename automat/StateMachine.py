import setup


def sequenceL1():
    configurations = [[90.0, 90.0, 0.0, 0.0, 0.0, 0.0],
                      [90.0, 90.0, 0.0, 0.0, 0.0, 90.0],
                      [90.0, 90.0, 30.0, 0.0, 0.0, 0.0]]
    return configurations


def sequenceL2():
    configurations = [[90.0, 90.0, 0.0, 0.0, 0.0, 0.0],
                      [-90.0, 90.0, 0.0, 0.0, 0.0, 90.0],
                      [-90.0, 0.0, 30.0, 90.0, 0.0, 0.0]]
    return configurations


def sequenceR1():
    configurations = [[90.0, 90.0, 0.0, 0.0, 0.0, 0.0],
                      [90.0, 45.0, 0.0, 34.0, 20.0, 90.0],
                      [90.0, 70.0, 30.0, 0.0, -60.0, 0.0]]
    return configurations


def sequence2():
    configurations = [[90.0, 90.0, 0.0, 0.0, 0.0, 0.0],
                      [-90.0, 90.0, 0.0, 0.0, 0.0, 90.0],
                      [-90.0, 0.0, 30.0, 90.0, 0.0, 0.0]]
    return configurations


def StateMachineStart():
    """""
    Executing the statemachine and create 
    
    :return  List of positions for each robot 
    """""
    robotLHome = [0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    robotRHome = [0.0, -90.0, 0.0, 0.0, 0.0, 0.0]
    robotLMoves = [robotLHome]
    robotRMoves = [robotRHome]
    for path in setup.main_paths:
        # create a supervisor
        supervisor = setup.Generator.create_master(setup.master_states, setup.master_transitions)
        # create robots
        robotL = setup.Generator.create_master(setup.robotL_states, setup.robotL_transitions)
        robotR = setup.Generator.create_master(setup.robotR_states, setup.robotR_transitions)
        print('\n' + str(supervisor))
        print('\n' + str(robotL))
        print('\n' + str(robotR))

        # run supervisor for exemplary path
        print("Executing path: {}".format(path))
        for event in path:

            # add slave
            if supervisor.current_state.value == "(czujnik_1&czujnik_2)==0":
                print(supervisor.current_state)

            if supervisor.current_state.value == "czujnik_1==1":
                print(supervisor.current_state)

            if supervisor.current_state.value == "czujnik_2==1":
                print(supervisor.current_state)

            if supervisor.current_state.value == "czujnik_3==1":
                print(supervisor.current_state)

            if supervisor.current_state.value == "S1&S2==ON":
                print(supervisor.current_state)

                for pathL, pathR in zip(setup.rL_paths, setup.rR_paths):
                    for eventL, eventR in zip(pathL, pathR):

                        ##############################################
                        #########         ROBOT L      ###############
                        ##############################################
                        if robotL.current_state.value == "L_cycle1==1":
                            print(robotL.current_state)
                            # create list of positions
                            for configuration in sequenceL1():
                                robotLMoves.append(configuration)

                        if robotL.current_state.value == "(L_cycle2&R_cycle2)==1":
                            print(robotL.current_state)
                            # create list of positions
                            for configuration in sequenceL2():
                                robotLMoves.append(configuration)

                        if robotL.current_state.value == "L_cycle2==0":  # GO HOME
                            print(robotL.current_state)
                            robotLMoves.append(robotLHome)

                        if robotL.current_state.value == "Flag_Restart == ON":
                            # TODO: Reset robot lewy
                            print(robotL.current_state)


                        ##############################################
                        #########         ROBOT R      ###############
                        ##############################################
                        if robotR.current_state.value == "R_cycle1==1":
                            print(robotR.current_state)
                            # create list of positions
                            for configuration in sequenceR1():
                                robotRMoves.append(configuration)

                        if robotR.current_state.value == "(L_cycle2&R_cycle2)==1":
                            print(robotR.current_state)
                            # create list of positions
                            for configuration in sequenceR1():
                                robotRMoves.append(configuration)

                        if robotR.current_state.value == "R_cycle2==0":
                            print(robotR.current_state)
                            robotRMoves.append(robotRHome)

                        if robotR.current_state.value == "Flag_Restart == ON":
                            print(robotR.current_state)
                            # TODO: Reset robot prawy

                        setup.robotL_transitions[eventL]._run(robotL)
                        setup.robotR_transitions[eventR]._run(robotR)

            if supervisor.current_state.value == "(L_cycle2&R_cycle_2)==0":
                print(supervisor.current_state)

            if supervisor.current_state.value == "czujnik_3==0":
                print(supervisor.current_state)

            setup.master_transitions[event]._run(supervisor)

    return robotLMoves, robotRMoves
