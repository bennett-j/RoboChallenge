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

# Specify the reflectance of the line and the background and calculate the threshold using the midpoint.
LINE_REF = 5
BACKGROUND_REF = 50
threshold = (LINE_REF + BACKGROUND_REF)/2

# Set forward speed.
FORWARD_SPEED = 50

# Set turn gain.
# Turn gain is a multiplier for how sensitive the robot steers according to the deviation.
# Bigger number => robot will turn more per deviation
TURN_GAIN = 2.5

# while True will loop forever
while True:
    # Measure reflectance and determine deviation from line and multiply by gain
    measurement = line_sensor.reflection()
    deviation = measurement - threshold
    turn_rate = TURN_GAIN * deviation
    
    # Update the robot's speeds
    robot.drive(FORWARD_SPEED, turn_rate)