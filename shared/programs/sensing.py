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

# Set the reflectance value for the line that you measured.
LINE_REF = 3
# Calculate the stopping reflectance value by adding a margin to the line reflectance.
stop_reflectance = LINE_REF + 5

# While the reflection is brighter than the stopping reflectance, drive forwards.
while line_sensor.reflection() > stop_reflectance:
    robot.drive(100, 0)

# Stop driving.
robot.stop()