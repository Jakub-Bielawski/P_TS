import setup

# show path from selected state to selected state
def showPath(valueInFrom, valueInTo):
    pathTemp = []
    pathFromTo = []

    # prepare string to use in conditions
    def Split(Index):
        value_tab = Index.split("_")
        return value_tab[0] + value_tab[1]

    # function to print path form state to state in robot graph
    def printRobot(path):
        flagFirstLoop = False
        flagFirstR = False
        for robotL, robotR in zip(setup.robotL_transitions, setup.robotR_transitions):
            StateL = Split(robotL)
            StateR = Split(robotR)

            # path from robot to main graph
            if (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and valueInTo[:1] != "L" and valueInTo[:1] != "R":
                if (StateL[1:] >= valueInFrom[1:] and StateL[:1] == valueInFrom[:1]) or (
                        StateL[1:] > valueInFrom[1:] and flagFirstLoop):
                    path.append(StateL)
                    path.append(StateR)
                    flagFirstLoop = True
                elif StateR[1:] >= valueInFrom[1:] and StateR[:1] == valueInFrom[:1]:
                    path.append(StateR)
                    if flagFirstR and StateR != valueInFrom:
                        path.append(StateL)
                    flagFirstR = True
                if StateL[1:] == valueInTo[1:] and StateL[:1] == valueInTo[:1] or \
                        StateR[1:] == valueInTo[1:] and StateR[:1] == valueInTo[:1]:
                    break
            # path from robot to robot graph
            elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and (valueInTo[:1] == "L" or valueInTo[:1] == "R"):
                if valueInFrom[1:] <= valueInTo[1:] and StateL[1:] >= valueInFrom[1:]:
                    if StateL[:1] == "L" and StateL == valueInTo:
                        path.append(StateL)
                    else:
                        if valueInFrom == StateR:
                            path.append(StateR)
                        else:
                            path.append(StateL)
                            path.append(StateR)
                    if StateL == valueInTo or StateR == valueInTo:
                        break
                elif valueInFrom[1:] > valueInTo[1:]:
                    if StateL[1:] > valueInTo[1:] or StateR[1:] > valueInTo[1:]:
                        if StateR[:1] == "R" and StateR == valueInFrom:
                            path.append(StateR)
                        else:
                            path.append(StateL)
                            path.append(StateR)
                    else:
                        pathTemp.append(StateL)
                        pathTemp.append(StateR)
                        if StateR[1:] == valueInTo[1:] and valueInTo[:1] == "L":
                            pathTemp.remove(StateR)


            # path from main to main and main to robot graph
            else:
                if StateL[:1] == "L" and StateL == valueInTo:
                    path.append(StateL)
                else:
                    path.append(StateL)
                    path.append(StateR)
                if StateL == valueInTo or StateR == valueInTo:
                    break

    # start checking path
    # first main state to main state
    if valueInFrom[:1] == "m" and valueInTo[:1] == "m":
        flagRobotDone = False
        removestate = "m4"
        # in main graph searching states to value
        for mainIndex in setup.master_transitions:
            currentState = Split(mainIndex)
            # Start from end. example: showPath("m3","m2")
            if valueInFrom[1:] > valueInTo[1:]:
                if currentState[1:] >= valueInFrom[1:]:
                    pathFromTo.append(currentState)
                    if currentState == "m4" and not flagRobotDone:
                        # add states to path from robot graph
                        printRobot(pathFromTo)
                        flagRobotDone = True
                    elif flagRobotDone and currentState == "m4":
                        pathFromTo.pop(len(pathFromTo)-1)


                elif currentState[1:] <= valueInTo[1:]:
                    pathTemp.append(currentState)
                    if currentState == "m4" and not flagRobotDone:
                        # add states to path from robot graph
                        printRobot(pathTemp)
                        flagRobotDone = True
            # Start normally. example: showPath("m1", "m5)
            elif valueInFrom[1:] < valueInTo[1:]:
                if valueInFrom[1:] <= currentState[1:] <= valueInTo[1:]:
                    pathFromTo.append(currentState)
                    if currentState == "m4" and not flagRobotDone:
                        # add states to path from robot graph
                        printRobot(pathFromTo)
                        flagRobotDone = True
                    elif flagRobotDone and currentState == "m4":
                        pathFromTo.pop(len(pathFromTo)-1)
        # add states in good order like in graph
        pathFromTo = pathFromTo + pathTemp

    # second main state to robot state
    elif valueInFrom[:1] == "m" and (valueInTo[:1] == "R" or valueInTo[:1] == "L"):
        flagDone = False
        flagDoneOther = False
        # in main graph searching states to value
        for mainIndex in setup.master_transitions:
            currentState = Split(mainIndex)
            if currentState[1:] >= valueInFrom[1:] and not flagDone:
                pathFromTo.append(currentState)
                if currentState == "m4":
                    # add states to path from robot graph
                    printRobot(pathFromTo)
                    flagDone = True
            if currentState[1:] < valueInFrom[1:] and not flagDoneOther:
                pathTemp.append(currentState)
                if currentState == "m4":
                    # add states to path from robot graph
                    printRobot(pathTemp)
                    flagDoneOther = True

        if valueInFrom <= "m4":
            # pathFromTo
            pass
        else:
            # add states in good order like in graph
            pathFromTo = pathFromTo + pathTemp

    # third robot state to main state
    elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and valueInTo[:1] == "m":
        # add states to path from robot graph
        printRobot(pathFromTo)
        flagEnd = False
        # in main graph searching states to value
        for mainIndex in setup.master_transitions:
            currentState = Split(mainIndex)
            if currentState[1:] > "4" and currentState[1:] <= valueInTo[1:]:
                pathFromTo.append(currentState)
                if valueInTo == currentState:
                    flagEnd = True
            elif currentState[1:] > "4" and currentState[1:] > valueInTo[1:] and flagEnd != True:
                pathFromTo.append(currentState)
            if currentState[1:] <= valueInTo[1:]:
                pathTemp.append(currentState)
        if valueInTo[1:] <= "4":
            if valueInTo == "m4":
                pathTemp.pop(int(valueInTo[1:]))
            # add states in good order like in graph
            pathFromTo = pathFromTo + pathTemp

    # fourth robot state to robot state
    elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and (valueInTo[:1] == "R" or valueInTo[:1] == "L"):
        # add states to path from robot graph
        printRobot(pathFromTo)
        # add states in good order like in graph
        pathFromTo = pathFromTo + pathTemp

    # add to shorts of states long names. example ["m1"] -> m1 : Spowolnienie tasmy
    for rename in pathFromTo:
        if rename[:1] == "m":
            print(rename, ": ", setup.master_states[int(rename[1:])].name)
        elif rename[:1] == "R":
            print(rename, ": ", setup.robotL_states[int(rename[1:])].name)
        elif rename[:1] == "L":
            print(rename, ": ", setup.robotR_states[int(rename[1:])].name)

# example of use
showPath("m1", "m6")