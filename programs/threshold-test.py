#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

# Initialize the EV3 Brick and beep to notify.
ev3 = EV3Brick()
ev3.speaker.beep

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

while True:
    ev3.screen.print(line_sensor.reflection())