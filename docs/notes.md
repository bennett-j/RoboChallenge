- Laptop should be on and VS code running, but not essential.
- Ensure the hello world script is on the robot.
- Best to turn the robot on before but not essential.

- pybricks-stubs for intellisense

- the robot needs to be on (green light) to connect from vscode

- the robot will spit out an error log that can be uploaded to the pc (from the robot) and viewed in a text editor

- derivative didn't seem to be that useful when I briefly tried it

```
from pybricks.tools import wait
```
also robot.stop() both useful in moving the robot around

- taken the approach of not explaining too much of the code in the instruction sheet, believing that is better done by a demonstrator face to face.
- with `sensing.py` students will probably hold the robot in the air when starting and find no wheels turn when they put it down. That is because the sensor sees black when there is no surface in front of it and therefore stops instantly. The robot needs to be on the floor when the program starts.


# Ideas
- control the forward speed (faster when lower error?)