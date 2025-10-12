#!/usr/bin/env pybricks-micropython

# Import things we need from libraries.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialise the EV3 Brick.
ev3 = EV3Brick()

# Robot say "Hello World".
ev3.speaker.set_volume(100)
ev3.speaker.say("Hello World!")

# Initialise the motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

# Turn motor at 360 °/second
left_motor.run_time(360,1000)