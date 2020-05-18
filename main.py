# built-in libraries
import argparse
import robopy.base.model as robot
import sys

# user libraries
from excercises import *
from automat import StateMachineStart
from pathFinder import showPath
from procesGraph import genereateGraph

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument("model", help="Model of robot (puma / orion)")
args = parser.parse_args()


# prepare main
def main():
    """""
    
    1. Set path from /setup/examplePath.py
    2. Set sequences for each robot in /automat/StateMachine.py
    
    If you want to check which states your path contains:
        use pathFinder.showPath(start_point, end_point) 
    To generate process graph:
        use procesGrpah.generateGraph()
    
    
    """""


    # generate graph
    # genereateGraph()

    # execute statemachine to get the path for robots
    statesL, statesR = StateMachineStart()

    # load model
    if str(args.model).lower() == "puma":
        model = robot.Puma560()
    elif str(args.model).lower() == "orion":
        model = robot.Orion5()
    else:
        print("Bad model specified. Try again.")
        sys.exit()

    # Start robot simulations
    joint_move.run(model, statesR)
    joint_move.run(model, statesL)


# run main
if __name__ == '__main__':
    main()
