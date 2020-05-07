import include

pathFromTo = []
valueInFrom = "m2"
valueInTo = "m1"
State = valueInFrom
pathTemp = []
flagOneMoreTime = False
flagRobotEnd = False
if valueInTo[1:] < valueInFrom[1:]:
    flagOneMoreTime = True

for mainIndex in include.master_transitions:
    if flagRobotEnd:

        break
    value_tab = mainIndex.split("_")
    State = value_tab[0] + value_tab[1]
    if value_tab[1] >= valueInFrom[1:]:
        pathFromTo.append(State)
        # end main path
        if State == valueInTo:
            break
        # add 2 robots to path
        if State == "m4":
            for robotL, robotR in zip(include.robotL_transitions, include.robotR_transitions):
                valueTabL = robotL.split("_")
                valueTabR = robotR.split("_")
                StateL = valueTabL[0] + valueTabL[1]
                StateR = valueTabR[0] + valueTabR[1]
                if valueInTo[:1] == "m":
                    pathFromTo.append(StateL)
                    pathFromTo.append(StateR)
                elif valueTabR[1] <= valueInTo[1:]:
                    pathFromTo.append(StateL)
                    pathFromTo.append(StateR)

                if StateL == valueInTo or StateR == valueInTo:
                    flagRobotEnd = True
                    break

    # add others state if start value is bigger than end
    elif flagOneMoreTime and flagRobotEnd:
        pathTemp.append(State)
pathFromTo = pathFromTo + pathTemp
print("")
print("Path from state: ",valueInFrom," to state: ",valueInTo,":")
print(pathFromTo)
print("")
# Change shorcut to Name of State
for rename in pathFromTo:
    # print(rename)
    if rename[:1] == "m":
        print(rename, ": ", include.master_states[int(rename[1:])].name)
    elif rename[:1] == "R":
        print(rename, ": ", include.robotL_states[int(rename[1:])].name)
    elif rename[:1] == "L":
        print(rename, ": ", include.robotR_states[int(rename[1:])].name)
