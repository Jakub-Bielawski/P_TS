# Define points. Implement move_j between them.

import numpy as np
from robopy.base import pose
from commands.moves import move_j


def run(robot, pathToExecute):
    # create configurations from path

    # define joint positions
    start = [0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    middle = [90.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    stop = [90.0, 90.0, 30.0, 0.0, 0.0, 0.0]

    # compute path
    # path1 = move_j(robot, start, middle)
    # path2 = move_j(robot, middle, stop)
    wszystkie_pathy=[]
    for idx, config in enumerate(pathToExecute):
        if idx <= (len(pathToExecute) - 2):
            Path = move_j(robot, config, pathToExecute[idx + 1])
            wszystkie_pathy.append(Path)
    # concatenate entire path

    path = np.concatenate(tuple(wszystkie_pathy), axis=0)
    print(path)

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')
