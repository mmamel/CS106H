#Authors: <Aishwarya Vellanki, Melvin Ma, Kyle DuFrene>
#Assignment: Lab 4-5: Cozmo Task
#Date: 19/10/2018

import CozmOSU

def main(robot):

  robot.moveHead(0);

  timeout = 1;
  cube = robot.getVisibleCube(timeout);

  if cube:
    robot.pickupCube(cube);
  else:
    print("Could not find Cube");
  robot.turn(-90);
  robot.driveForward(400, 50);
  robot.turn(90);
  robot.driveForward(200, 50);
  robot.moveLift(0);
robot=CozmOSU.Robot();
robot.start(main);
