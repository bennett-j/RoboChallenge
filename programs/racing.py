#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick and beep to notify.
ev3 = EV3Brick()
ev3.speaker.beep

# Initialize the motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

# Initialize the colour sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the white/black threshold using the midpoint.
BLACK = 8
WHITE = 45
threshold = (BLACK + WHITE)/2

# BASIC
FORWARD_SPEED = 100
TURN_SPEED = 100
# while True will loop forever
# while True:
    
#     # if white, turn right
#     if line_sensor.reflection() > threshold:
#         robot.drive(FORWARD_SPEED, TURN_SPEED)
#     else: # it's black, turn left
#         robot.drive(FORWARD_SPEED, -TURN_SPEED)

#     #wait(1)

# MORE ADVANCED
# Using a P controller
P = 3
D = 2
P2 = 4
D2 = 4
prev_deviation = 0
# # while True will loop forever
# while True:
    
#     deviation = line_sensor.reflection() - threshold
#     turn_rate = P * deviation
#     robot.drive(FORWARD_SPEED, turn_rate)

#     #wait(5)

while True:
    
    deviation = line_sensor.reflection() - threshold
    diff = deviation-prev_deviation

    turn_rate = P * deviation + D*diff
    forward_speed = 200 - (P2 * abs(deviation) + D2*diff)
    robot.drive(forward_speed, turn_rate)

    prev_deviation = deviation
    
    #wait(5)