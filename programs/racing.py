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
WHITE = 40
threshold = (BLACK + WHITE)/2

# Set forward speed
FORWARD_SPEED = 80

# BASIC
# TURN_SPEED = 100
# while True will loop forever
# while True:
    
#     # if white, turn right
#     if line_sensor.reflection() > threshold:
#         robot.drive(FORWARD_SPEED, TURN_SPEED)
#     else: # it's black, turn left
#         robot.drive(FORWARD_SPEED, -TURN_SPEED)


# Gain is a multiplier for how sensitive the robot turns according to the deviation.
# Bigger number => robot will turn more per deviation
P = 2.5

# while True will loop forever
while True:
    # Measure reflectance and determine deviation from line and multiply by gain
    measurement = line_sensor.reflection()
    deviation = measurement - threshold
    turn_rate = P * deviation
    
    # Update the robot's speeds
    robot.drive(FORWARD_SPEED, turn_rate)