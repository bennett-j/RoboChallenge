#!/usr/bin/env pybricks-micropython

# Import things we need from libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

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

# 'adjusting_reflectance' refers to the reflectance value at which the robot will stop moving
# 'measured_reflectance' refers to the user inputted reflectance value measured from the robot's sensor
# NOTE default value for measured_reflectance is 3, which should make the robot stop on a black line
measured_reflectance = 3
adjusting_threshold = measured_reflectance + 5

# Set forward speed - default is 50
FORWARD_SPEED = 50

# Set turn gain - default is 2.5
# Turn gain is a multiplier for how sensitive the robot steers according to the deviation.
# Bigger number => robot will turn more per deviation
TURN_GAIN = 2.5

# while True will loop forever
while True:
    # Measure reflectance and determine deviation from line and multiply by gain
    measurement = line_sensor.reflection()
    deviation = measurement - adjusting_threshold
    turn_rate = TURN_GAIN * deviation
    
    # Update the robot's speeds
    robot.drive(FORWARD_SPEED, turn_rate)