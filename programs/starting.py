#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Robot say "Hello World".
ev3.speaker.say("Hello World!")

# Initialize the motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

# Turn motor at 360 °/second
left_motor.run(360)