# Import the robot control commands from the library
from simulator import robot
import time
def move_robot (distance) : 
    robot.motors(1, 0, 1)
    robot.motors(0, 0, 1)
    robot.motors(1, -1, 1)
    robot.motors(1, -1, 1)
    robot.motors(1, 3, -1)
    robot.motors(1, -2, 1)
    robot.motors(1, 1, 3)
    robot.motors(1, 1, 3)
    robot.motors(1, 2, 3)
    robot.motors(-1, 1,2)
    robot.motors(2, 3, 1)
    robot.motors(1, 2, 2)
    robot.motors(1, 2 ,2)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(-1, 1,3)
    robot.motors(-1, 1,3)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(-1, 1,3)
    robot.motors(1, 1, 3)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(1, 2, 2)
    robot.motors(-1, 1,3)
    robot.motors(1, 2, 0)
    robot.motors(1, 1, 0)
    robot.motors(2, 1, 1)
    robot.motors(2, 1, 2)
    robot.motors(1, 2, 1)
    robot.motors(1, 1, 2)
    robot.motors(1, 3, 1)
    robot.motors(1, 2, 1)
    robot.motors(2, 1, 1)
    robot.motors(1, 2, 1)
    robot.motors(3, 2, 1)



   
    #Distance  (float): The distance the robot will move in meters
left, right = robot.sonars() #Simulate the robot moving a specific distance

