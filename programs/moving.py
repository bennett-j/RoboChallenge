#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick and beep to notify.
ev3 = EV3Brick()
ev3.speaker.beep

# Initialize the motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Drive straight forwards 500 mm
robot.straight(500)