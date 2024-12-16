# Import the robot control commands from the library
from simulator import robot
import time

def move_robot (distance) : 
    robot.moves(1, 0, 1)
    robot.moves(0, 1, 0)
    robot.moves(0, 1, 1)
    robot.moves(1, 1, 0)
    robot.moves(1, 1, 1)
    robot.moves(1, 1, 2)
    robot.moves(1, 2, 1)
    robot.moves(1, 2, 1)
    robot.moves(1, 2, 2)
    robot.moves(2, 1, 1)
    robot.moves(2, 2, 1)
    robot.moves(3, 2, 1)
    robot.moves(3, 2, 2)
    robot.moves(3, 3, 3)
    
    # Simulate the robot's motor control systemclass Robot:
        self.motor_left = 0
        self.motor_right = 0
    
def move_forward(self, steps):
        """Moves the robot forward by a number of steps"""
        self.motor_left = 1
        self.motor_right = 1
    
def turn_left(self, angle):
        """Turns the robot left by a given angle"""
        print(f"Turning left by {angle} degrees.")
        self.motor_left = -1
        self.motor_right = 1
    
def turn_right(self, angle):
        """Turns the robot right by a given angle"""
        print(f"Turning right by {angle} degrees.")
        self.motor_left = 1
        self.motor_right = -1
    
def stop(self):
        """Stops the robot's movement"""
        self.motor_left = 0
        self.motor_right = 0
        print("Robot stopped.")
    
def get_sonar_reading(self):
        """Simulate getting a sonar reading"""
       
# Function to get a valid user input
def get_valid_input(prompt, valid_choices):
    """Get a valid input from the user"""
    while True:
        user_input = input(prompt)
        if user_input in valid_choices:
            return user_input
        else:
            print(f"Invalid input. Please choose from {valid_choices}")

# Function to move the robot based on sensor reading
def move_based_on_sonar(robot):
    """Move robot based on sonar readings (avoid obstacles)"""
    
    if sonar_distance < 20:
        print("Obstacle detected! Turning left.")
        robot.turn_left(90)
    elif sonar_distance < 50:
        print("Approaching obstacle. Slowing down.")
        robot.stop()
        time.sleep(2)
    else:
        print("Path clear. Moving forward.")
        robot.move_forward(5)

# Recursive function to keep checking sensor and moving the robot
def autonomous_move(robot, duration):
    """Move the robot autonomously for a specified duration (seconds)"""
    start_time = time.time()
    while time.time() - start_time < duration:
        move_based_on_sonar(robot)
        time.sleep(1)  # Check the sensor and move every second

# Function to execute robot movements based on user choice
def execute_user_choice(robot):
    """Execute a user-defined movement based on input"""
   
    if choice == "1":
        steps = int(input("How many steps forward? "))
        robot.move_forward(steps)
    elif choice == "2":
        angle = int(input("How many degrees to turn left? "))
        robot.turn_left(angle)
    elif choice == "3":
        angle = int(input("How many degrees to turn right? "))
        robot.turn_right(angle)
    elif choice == "4":
        robot.stop()
    elif choice == "5":
        duration = int(input("How many seconds should the robot move autonomously? "))
        autonomous_move(robot, duration)

def main():
    # Initialize the robot
    robot = Robot()

    # User-driven loop
    while True:
        print("\n-- Robot Control --")
        execute_user_choice(robot)

        # Ask user if they want to continue or exit
        continue_choice = get_valid_input("Do you want to continue? (yes/no): ", ["yes", "no"])
        if continue_choice == "no":
            print("Exiting robot control...")
            break




   
    #Distance  (float): The distaZnce the robot will move in meters
left, right = robot.sonars() #Simulate the robot moving a specific distance

