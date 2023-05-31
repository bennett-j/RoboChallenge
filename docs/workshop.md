# LEGO® Robot Workshop

Welcome to your robot workshop! Today, we're going to use the LEGO® MINDSTORMS® EV3 robot to have some fun with robotics.

![Image of Robot](/assets/robot_overview.jpg)

## Getting Started
### The Robot

Let's turn the robot on. If the light behind the middle button is green then you're good to go. If there are no lights, press the middle button and wait for it to turn on. This could take a minute, so while you're waiting read on.

![Image of controls](/assets/ev3brick_labelled.png)

You will see the robot has two wheels (that it uses to move) and a range of sensors (we'll get to them later) all held together by lego. At the centre is a big box that we call the `brick`; it tells every other part of the robot what to do. At this stage, robots are just a pile of lego and electronics - not very intelligent - until we tell them what to do. This requires a `program`. 

### Running a program
Let's run a program.
Use the buttons to navigate `File browser > programs > starting.py`. Clicking `starting.py` will "run" that program. You should hear the robot say "Hello World", and turn a wheel! Press the `back` button to stop the program.

![Image of file structure](/assets/run_program_manual.png)

### Creating a program
Next we want to be able to write our own programs to get the robot to do what we want. You will write the code on the laptop using Visual Studio Code which is what students and many professionals use to write code.

1. Turn the laptop on and open up Visual Studio Code if not already.
1. Open the folder `Robot Workshop` from the Desktop using the file menu.
1. Click `File > Save As...` and save with your name.
1. Open the file `starting.py` by clicking on it in the `Explorer` left panel. This was the program we just ran on the robot.

> Note: any line starting with # is a comment which the robot ignores. Every other line of code tells the robot to do something.

Make the following changes:

1. Change it to say "Hello [your names]".
1. Change the program to get the other wheel to turn.

Great, you've written your first program. Now we need to download it to the robot and run it.

1. Connect EV3 to PC with a cable. (EV3 must be on and the light lit green)
1. Open the Explorer in the left panel of VSCode.
1. Expand the EV3DEV DEVICE BROWSER from the bottom of the panel and click 'Click here to connect to a device'.
1. Select your device (from the top of the screen).
1. Press F5 to download and run your program to the robot. 

> Note: the robot will start running the program whilst still plugged in. You can uplug it once it has finished downloading and you can re-run the program unplugged as per the earlier instructions to run a program.

![Connecting to EV3](/assets/connecting_ev3.png)

## Getting the robot to move

It would be inconvenient if we had to control the robot through the motor speeds individually so instead we use `DriveBase` which provides some useful functions to control the robot:
```
robot.straight(distance)
```
Drive the robot in a straight line for the given distance in mm.
```
robot.turn(angle)
```
Turn the robot on the spot the given angle in degrees (°).
```
robot.drive(drive_speed, turn_rate)
```
The robot will drive forwards at the speed `drive_speed` and turn at the speed `turn_rate`. This function starts the robot moving and it will continue until another command is given.


Open the file `moving.py`. You will see we have added the line `robot = DriveBase(...)`. Using the functions above, attempt the following movements.

1. Drive forwards 1 metre
1. Drive backwards 1 metre
1. Turn 180° on the spot both ways
1. Drive in a square
1. Drive in a circle

> Hint: values can be negative.

> Challenge: get the robot to move by controlling the motors without `DriveBase`.

## Sensing

Did the robot finish exactly where it started when you drove in a square? The robot has no way to "see" where it is. Just like you trying to walk in a big square whilst blindfolded. To let our robots "see", we use **_sensors_** on them. In this part, we'll use the reflectance sensor. It shines some light onto the floor beneath it and measures how much is reflected, if the floor is light (white) it will have a high reflectance but if it's dark (black) the reflectance will be low.

1. Use the script `threshold-test.py` to determine the reflectance of the white background and the black line and make a note of these. 

You will see in the program we have added the sensor with the line 
```
line_sensor = ColorSensor(Port.S3)
```
and that we measure the reflectance and show it on the robot's screen with
```
ev3.screen.print(line_sensor.reflection())
```

2. Now open `sensing.py` and input the values you measured for `BLACK` and `WHITE`.
1. Put a finish line on the floor for your robot to stop at. 
1. Get the robot to drive then stop at the finish line by running the program.
1. Examine the code and see if you can explain to a demonstrator how it works.


## Racing
Now let's see if we can get our robot to race around the track by following the line!

> Challenge: Pause before you look at the program and see if you can work out an **_algorithm_** for the robot to follow the line.

1. Open `racing.py` and run the program.
1. Read the comments that explain how the program works.
1. Adjust `FORWARD_SPEED` and `P` so that the robot can complete the racetrack!

Note: the robot follows the edge of a line.
The `threshold` is defined as grey, the average of white and black. If the black line is on the left and the white background on the right, when the sensor sees more white than the threshold it needs to turn to the left to find the line.

# Finishing
Congratulations for completing this workshop
Turn off robot and PC