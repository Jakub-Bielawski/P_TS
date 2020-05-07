import include

#
# pathFromTo = []
# valueInFrom = "m2"
# valueInTo = "R2"
# State = valueInFrom
# pathTemp = []
# flagOneMoreTime = False
# flagRobotEnd = False
# if valueInTo[1:] < valueInFrom[1:]:
#     flagOneMoreTime = True
#
# for mainIndex in include.master_transitions:
#     if flagRobotEnd:
#         break

#     value_tab = mainIndex.split("_")
#     State = value_tab[0] + value_tab[1]
#     # end main path
#     if State == valueInTo:
#         break
#
#     if value_tab[1] >= valueInFrom[1:]:
#         pathFromTo.append(State)
#
#         # add 2 robots to path
#         if State == "m4":
#             for robotL, robotR in zip(include.robotL_transitions, include.robotR_transitions):
#                 valueTabL = robotL.split("_")
#                 valueTabR = robotR.split("_")
#                 StateL = valueTabL[0] + valueTabL[1]
#                 StateR = valueTabR[0] + valueTabR[1]
#                 if valueInTo[:1] == "m":
#                     pathFromTo.append(StateL)
#                     pathFromTo.append(StateR)
#                 elif valueTabR[1] <= valueInTo[1:]:
#                     pathFromTo.append(StateL)
#                     pathFromTo.append(StateR)
#
#                 if StateL == valueInTo or StateR == valueInTo:
#                     flagRobotEnd = True
#                     break
#
#     # add others state if start value is bigger than end
#     elif flagOneMoreTime and flagRobotEnd:
#         pathTemp.append(State)
# pathFromTo = pathFromTo + pathTemp
# print("")
# print("Path from state: ",valueInFrom," to state: ",valueInTo,":")
# print(pathFromTo)
# print("")
# # Change shorcut to Name of State
# for rename in pathFromTo:
#     # print(rename)
#     if rename[:1] == "m":
#         print(rename, ": ", include.master_states[int(rename[1:])].name)
#     elif rename[:1] == "R":
#         print(rename, ": ", include.robotL_states[int(rename[1:])].name)
#     elif rename[:1] == "L":
#         print(rename, ": ", include.robotR_states[int(rename[1:])].name)
#


pathFromTo = []
valueInFrom = "m1"
valueInTo = "m5"
State = valueInFrom
pathTemp = []
flagOneMoreTime = False
flagRobotEnd = False


def Split(Index):
    value_tab = Index.split("_")
    return value_tab[0] + value_tab[1]


def printRobot(path):
    for robotL, robotR in zip(include.robotL_transitions, include.robotR_transitions):
        StateL = Split(robotL)
        StateR = Split(robotR)
        path.append(StateL)
        path.append(StateR)


if valueInFrom[:1] == "m" and valueInTo[:1] == "m":
    for mainIndex in include.master_transitions:
        currentState = Split(mainIndex)
        # Zaczynamy od dupy strony
        if valueInFrom[1:] > valueInTo[1:]:
            # Aktualny stan większy od startowego
            if currentState[1:] >= valueInFrom[1:]:
                pathFromTo.append(currentState)
                if currentState == "m4":
                    printRobot(pathFromTo)
            # Aktualny stan mniejszy od docelowego
            elif currentState[1:] <= valueInTo[1:]:
                pathTemp.append(currentState)
                if currentState == "m4":
                    printRobot(pathTemp)
        # Zaczynamu normalnie
        elif valueInFrom[1:] < valueInTo[1:]:
            if valueInFrom[1:] <= currentState[1:] <= valueInTo[1:]:
                pathFromTo.append(currentState)
                if currentState == "m4":
                    printRobot(pathFromTo)

    pathFromTo = pathFromTo + pathTemp

    print(pathFromTo)
elif valueInFrom[:1] == "m" and (valueInTo[:1] == "R" or valueInTo[:1] == "L"):
    print(valueInTo)

    for mainIndex in include.master_transitions:
        currentState =Split(mainIndex)
        # Zaczynamy od dupy strony
        if valueInFrom[1:] > valueInTo[1:]:
            # Aktualny stan większy od startowego
            if currentState[1:] >= valueInFrom[1:]:
                pathFromTo.append(currentState)
                if currentState == "m4":
                    # TODO : tutaj powinna byc obsluga robota, sprawdzanie czy aktualny stan to koncowy
                    ...
            # Aktualny stan mniejszy od docelowego
            elif currentState[1:] <= valueInTo[1:]:
                pathTemp.append(currentState)
                if currentState == "m4":
                    # TODO : tutaj powinna byc obsluga robota, sprawdzanie czy aktualny stan to koncowy
                    ...

        # Zaczynamu normalnie
        elif valueInFrom[1:] < valueInTo[1:]:
            if valueInFrom[1:] <= currentState[1:] <= valueInTo[1:]:
                pathFromTo.append(currentState)
                if currentState == "m4":
                    # TODO : tutaj powinna byc obsluga robota, sprawdzanie czy aktualny stan to koncowy
                    ...


    pathFromTo = pathFromTo + pathTemp



elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and valueInTo[:1] == "m":
    print(valueInTo, "!!!")
    ...

elif (valueInFrom[:1] == "R" or valueInFrom[:1] == "L") and (valueInTo[:1] == "R" or valueInTo[:1] == "L"):
    print(valueInTo, "@@@@@")
    ...
