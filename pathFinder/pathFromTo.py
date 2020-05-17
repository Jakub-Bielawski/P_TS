import setup

# TODO: tego nie sprzątam na razie
def showPath(valueInFrom, valueInTo):
    pathTemp = []
    pathFromTo = []

    def Split(Index):
        value_tab = Index.split("_")
        return value_tab[0] + value_tab[1]

    def printRobot(path):
        flagFirstLoop = False
        flagFirstR = False
        for robotL, robotR in zip(setup.robotL_transitions, setup.robotR_transitions):
            StateL = Split(robotL)
            StateR = Split(robotR)

            # path for r to m
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
            # r to r
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


            # path for m to m and m to r
            else:
                if StateL[:1] == "L" and StateL == valueInTo:
                    path.append(StateL)
                else:
                    path.append(StateL)
                    path.append(StateR)
                if StateL == valueInTo or StateR == valueInTo:
                    break

    if valueInFrom[:1] == "m" and valueInTo[:1] == "m":
        flagRobotDone = False
        removestate = "m4"
        for mainIndex in setup.master_transitions:
            currentState = Split(mainIndex)
            # Zaczynamy od dupy strony
            if valueInFrom[1:] > valueInTo[1:]:
                # Aktualny stan większy od startowego
                if currentState[1:] >= valueInFrom[1:]:
                    pathFromTo.append(currentState)
                    if currentState == "m4" and not flagRobotDone:
                        printRobot(pathFromTo)
                        flagRobotDone = True
                    elif flagRobotDone and currentState == "m4":
                        pathFromTo.pop(len(pathFromTo)-1)


                # Aktualny stan mniejszy od docelowego
                elif currentState[1:] <= valueInTo[1:]:
                    pathTemp.append(currentState)
                    if currentState == "m4" and not flagRobotDone:
                        printRobot(pathTemp)
                        flagRobotDone = True
            # Zaczynamu normalnie
            elif valueInFrom[1:] < valueInTo[1:]:
                if valueInFrom[1:] <= currentState[1:] <= valueInTo[1:]:
                    pathFromTo.append(currentState)
                    if currentState == "m4" and not flagRobotDone:
                        printRobot(pathFromTo)
                        flagRobotDone = True
                    elif flagRobotDone and currentState == "m4":
                        pathFromTo.pop(len(pathFromTo)-1)

        pathFromTo = pathFromTo + pathTemp

        print(pathFromTo)
    elif valueInFrom[:1] == "m" and (valueInTo[:1] == "R" or valueInTo[:1] == "L"):
        print(valueInTo)
        flagDone = False
        flagDoneOther = False
        for mainIndex in setup.master_transitions:
            currentState = Split(mainIndex)
            if currentState[1:] >= valueInFrom[1:] and not flagDone:
                pathFromTo.append(currentState)
                if currentState == "m4":
                    printRobot(pathFromTo)
                    flagDone = True
            if currentState[1:] < valueInFrom[1:] and not flagDoneOther:
                pathTemp.append(currentState)
                if currentState == "m4":
                    printRobot(pathTemp)
                    flagDoneOther = True
            # remove value if we have valueInTo
            # if flagDone:
            #     pathFromTo.remove(currentState)
        print(pathTemp)
        print(pathFromTo)
        if valueInFrom <= "m4":
            # pathFromTo
            pass
        else:
            pathFromTo = pathFromTo + pathTemp
        print(pathFromTo)

    elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and valueInTo[:1] == "m":
        printRobot(pathFromTo)
        flagEnd = False
        for mainIndex in setup.master_transitions:
            currentState = Split(mainIndex)
            # TODO simplify  to ?  "4" < currentState[1:] <= valueInTo[1:]
            if currentState[1:] > "4" and currentState[1:] <= valueInTo[1:]:
                pathFromTo.append(currentState)
                print(currentState)
                if valueInTo == currentState:
                    flagEnd = True
            elif currentState[1:] > "4" and currentState[1:] > valueInTo[1:] and flagEnd != True:
                pathFromTo.append(currentState)
            if currentState[1:] <= valueInTo[1:]:
                pathTemp.append(currentState)
        if valueInTo[1:] <= "4":
            if valueInTo == "m4":
                pathTemp.pop(int(valueInTo[1:]))
            pathFromTo = pathFromTo + pathTemp
        print(pathFromTo)

    elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and (valueInTo[:1] == "R" or valueInTo[:1] == "L"):
        printRobot(pathFromTo)
        pathFromTo = pathFromTo + pathTemp
        print(pathTemp)
        print(pathFromTo)

    for rename in pathFromTo:
        # print(rename)
        if rename[:1] == "m":
            print(rename, ": ", setup.master_states[int(rename[1:])].name)
        elif rename[:1] == "R":
            print(rename, ": ", setup.robotL_states[int(rename[1:])].name)
        elif rename[:1] == "L":
            print(rename, ": ", setup.robotR_states[int(rename[1:])].name)


showPath("m1", "R3")