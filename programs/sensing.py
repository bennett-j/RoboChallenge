#!/usr/bin/env pybricks-micropython

# Import things we need from libraries.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialise the EV3 Brick and beep to notify.
ev3 = EV3Brick()
ev3.speaker.beep()

# Initialise the motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

# Initialise the colour sensor.
line_sensor = ColorSensor(Port.S3)

# Create 'robot' by initialising the drive base with motors and dimensions.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

######################
# NOTES FOR STUDENTS #
######################
# 'stopping_reflectance' refers to the reflectance value at which the robot will stop moving
# 'measured_reflectance' refers to the user inputted reflectance value measured from the robot's sensor
# NOTE default value for measured_reflectance is 3, which should make the robot stop on a black line
######################
# NOTES FOR STUDENTS #
######################
measured_reflectance = 3
stopping_threshold = measured_reflectance + 5

# While the reflection is brighter than the threshold (i.e. white), drive forwards.
while line_sensor.reflection() > stopping_threshold:
    robot.drive(100, 0)

# Stop driving.
robot.stop()