from statemachine import State

# define states for a master (way of passing args to class)
options = [
    {"name": "Wjazd czesci w strefe robocza", "initial": True, "value": "(czujnik_1&czujnik_2)==0"},  # 0
    {"name": "Spowolnienie tasmy", "initial": False, "value": "czujnik_1==1"},  # 1
    {"name": "Zatrzymanie tasmy i zamkniecie zatrzaskow", "initial": False, "value": "czujnik_2==1"},  # 2
    {"name": "Zezwolenie na prace", "initial": False, "value": "czujnik_3==1"},  # 3
    {"name": "Sprawdzenie pozycji robota", "initial": False, "value": "S1&S2==ON"},  # 4
    {"name": "Wylaczenie zezwolenian prace robota i zwolnienie zatrzaskow", "initial": False,
     "value": "(L_cycle2&R_cycle_2)==0"},  # 5
    {"name": "Wlaczenie tasmy", "initial": False, "value": "czujnik_3==0"}]  # 6

options_RobotL = [
    {"name": "Pozycja domowa", "initial": True, "value": "L_cycle1==1"},  # 0
    {"name": "Sekwencja 1", "initial": False, "value": "(L_cycle2&R_cycle)==1"},  # 1
    {"name": "Sekwencja 2", "initial": False, "value": "L_cycle2==0"},  # 2
    {"name": "Srzygotowanie do ponownego wykonania", "initial": False, "value": "Flag_Restart == ON"}  # 3

]

options_RobotR = [
    {"name": "Pozycja domowa", "initial": True, "value": "R_cycle1==1"},  # 0
    {"name": "Sekwencja 1", "initial": False, "value": "(L_cycle2&R_cycle)==1"},  # 1
    {"name": "Sekwencja 2", "initial": False, "value": "R_cycle2==0"},  # 2
    {"name": "Srzygotowanie do ponownego wykonania", "initial": False, "value": "Flag_Restart == ON"}  # 3
]

# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in options]
robotL_states = [State(**opt) for opt in options_RobotL]
robotR_states = [State(**opt) for opt in options_RobotR]
