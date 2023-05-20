#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

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

# While the reflection is brighter than the threshold (i.e. white), drive forwards
while line_sensor.reflection() > threshold:
    robot.drive(100, 0)

# Stop driving.
robot.stop()