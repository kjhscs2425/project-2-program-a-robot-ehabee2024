import time
import random

# Simulating a Robot class
class Robot:
    def __init__(self):
        self.motor_left = 0
        self.motor_right = 0

    def move_forward(self, steps):
        """Moves the robot forward by a number of steps."""
        print(f"Moving forward {steps} steps.")
        self.motor_left = 1
        self.motor_right = 1
        time.sleep(1)

    def turn_left(self, angle):
        """Turns the robot left by a given angle."""
        print(f"Turning left by {angle} degrees.")
        self.motor_left = -1
        self.motor_right = 1
        time.sleep(1)

    def turn_right(self, angle):
        """Turns the robot right by a given angle."""
        print(f"Turning right by {angle} degrees.")
        self.motor_left = 1
        self.motor_right = -1
        time.sleep(1)

    def stop(self):
        """Stops the robot's movement."""
        print("Robot stopped.")
        self.motor_left = 0
        self.motor_right = 0

    def get_sonar_reading(self):
        """Simulate getting a sonar reading (random distance between 10 and 100 cm)."""
        return random.randint(10, 100)

# Function to get a valid user input
def get_valid_input(prompt, valid_choices):
    """Get a valid input from the user."""
    while True:
        user_input = input(prompt)
        if user_input in valid_choices:
            return user_input
        else:
            print(f"Invalid input. Please choose from {valid_choices}")

# Function to move the robot based on sonar readings
def move_based_on_sonar(robot):
    """Move robot based on sonar readings (avoid obstacles)."""
    sonar_distance = robot.get_sonar_reading()
    print(f"Sonar reading: {sonar_distance} cm")
    
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
    """Move the robot autonomously for a specified duration (seconds)."""
    start_time = time.time()
    while time.time() - start_time < duration:
        move_based_on_sonar(robot)
        time.sleep(1)  # Check the sensor and move every second

# Function to execute robot movements based on user choice
def execute_user_choice(robot):
    """Execute a user-defined movement based on input."""
    print("\nChoose a movement action:")
    print("1: Move Forward")
    print("2: Turn Left")
    print("3: Turn Right")
    print("4: Stop")
    print("5: Autonomous Movement")
    

    choice = get_valid_input("Enter your choice (1-5): ", ["1", "2", "3", "4", "5"])

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

# Main function to control robot behavior
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

if __name__ == "__main__":
    main()
