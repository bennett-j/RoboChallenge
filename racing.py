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

# Set the reflectance values for the line and background
# The target reflectance is the midpoint of the line and background reflectance
LINE_REF = 70         # white line
BACKGROUND_REF = 15   # black road
reflectance_setpoint = (LINE_REF + BACKGROUND_REF)/2

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
    deviation = measurement - reflectance_setpoint
    turn_rate = TURN_GAIN * deviation
    
    # Update the robot's speeds
    robot.drive(FORWARD_SPEED, turn_rate)