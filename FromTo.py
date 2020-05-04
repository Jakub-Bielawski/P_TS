import include
pathFromTo = []
valueInFrom = "m3"
valueInTo = "m5"
State = valueInFrom
pathTemp = []
flagOneMoreTime = False
if valueInTo[1:] < valueInFrom[1:]:
    flagOneMoreTime = True
    print(flagOneMoreTime)
for mainIndex in include.master_transitions:
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
                print(valueTabL)
                StateL = valueTabL[0] + valueTabL[1]
                StateR = valueTabR[0] + valueTabR[1]
                print(StateL)
                print(StateR)
                print("cosik")
                print(valueInFrom[1:])
                if valueTabL[0] != valueInFrom[:1]:
                    pathFromTo.append(StateL)
                if valueTabR[0] != valueInFrom[:1]:
                    pathFromTo.append(StateR)
                # if valueTabL[0] == valueInFrom[:1]:
                #     if valueTabL[1] >= valueInFrom[1:]:
                #     # end robots path
                #     if StateL == valueInTo:
                #         break
                # if valueTabR[1] >= valueInFrom[1:]:
                #
                #     # end robots path
                #     if StateR == valueInTo:
                #         break
    # add others state if start value is bigger than end
    elif flagOneMoreTime:
        pathTemp.append(State)
pathFromTo = pathFromTo + pathTemp
print(pathFromTo)
# Change shorcut to Name of State
for rename in pathFromTo:
    print(rename)
    if rename[:1] == "m":
        print(include.master_states[int(rename[1:])].name)
    elif rename[:1] == "R":
        print(include.robotL_states[int(rename[1:])].name)
    elif rename[:1] == "L":
        print(include.robotR_states[int(rename[1:])].name)
