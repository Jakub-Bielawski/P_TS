# Define points. Implement move_j between them.

import numpy as np
from robopy.base import pose
from commands.moves import move_j


def run(robot, pathToExecute):

    # compute path
    all_points=[]
    for idx, config in enumerate(pathToExecute):
        if idx <= (len(pathToExecute) - 2):
            Path = move_j(robot, config, pathToExecute[idx + 1])
            all_points.append(Path)
    # concatenate entire path

    path = np.concatenate(tuple(all_points), axis=0)
    print(path)

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')
