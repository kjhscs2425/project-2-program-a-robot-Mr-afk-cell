# Import the robot control commands from the library
from simulator import robot
import time

def turnleft(seconds):
    robot.motors(-1,1, seconds)

def turnright(seconds):
    robot.motors(1, -1, seconds)
def forward():
    robot.motors(1, 1, 60)
def backwards(): 
    robot.motors(-1, -1, 0)
    return 1
def jump():
    forward()
    backwards()
    return 1

#keep robot open until told to stop
while True:
    # print out instructions for user
    print("type stop to quit")
    print("type go to jump")
    # ask user to type 
    some_string = input('ask: ')
    # if type stop they exit
    if some_string == "stop":
        robot.exit()
    #when type jump should jump
    if some_string == "go" : 
        robot.motors(1,1,2)
    #ask the user how old they are
    age = input("How old are you?") 
    # ask the user what is their favourite color
    color = input("What is your favourite color?")
    animal = input("What is your favourite animal?")
    name = input("What is your name?")
    
    #if type turn they turn
    if  some_string == "turn":
      turnleft(20)

    a = jump()