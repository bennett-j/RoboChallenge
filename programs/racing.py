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
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE)/2

# BASIC

# while True will loop forever
while True:
    
    # if white, turn right
    if line_sensor.reflection() > threshold:
        robot.drive(100, 20)
    else: # it's black, turn left
        robot.drive(100, -20)

    wait(5)

# MORE ADVANCED
# Using a P controller
P = 1.2

# while True will loop forever
while True:
    
    deviation = line_sensor.reflection() - threshold
    turn_rate = P * deviation
    robot.drive(100, turn_rate)

    wait(5)