#!/usr/bin/env pybricks-micropython

# Import things we need from libraries.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

# Initialise the EV3 Brick and beep to notify.
ev3 = EV3Brick()
ev3.speaker.beep()

# Initialise the color sensor.
line_sensor = ColorSensor(Port.S3)

while True:
    ev3.screen.print(line_sensor.reflection())