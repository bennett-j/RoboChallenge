# LEGO® Robot Workshop

Welcome to your robot workshop! Today, we're going to use the LEGO® MINDSTORMS® EV3 robot to have some fun with robotics.

## Getting Started
### The Robot
[image of robot]

Let's turn the robot on. 

If the light behind the middle button is green then you're good to go. If there are no lights, press the middle button and wait for it to turn on. This could take a minute, so while you're waiting read on...

[img of controls]

... you'll see the robot has two wheels (that is uses to move) and a range of sensors (we'll get to them later) all held together by lego. At the centre is a big box that we call the `brick`; it tells every other part of the robot what to do. At this stage, robots are just a pile of lego and electronics - not very intelligent - until we tell them what to do. This requires a `program`. 

### Running a program
Let's run a program.
Use the buttons to navigate. `File browser > Hello World > main.py`. `main.py` is our program so clicking on that will "run" the program. You should hear the robot say "hello world", show it on the screen, and turn a wheel!

[image of file structure]

### Creating a program
Next we want to be able to write our own programs to get the robot to do what we want. You will write the code on the laptop using Visual Studio Code which is what students of computing sciences use throughout their degree courses.

1. Turn the laptop on and open up Visual Studio Code if not already.
1. Open the folder `Robot Workshop`.
1. Open the file `HelloWorld.py`. This was the program we just ran on the robot.

Explain the structure of the file.

Make the following changes:

1. Change it to say "Hello [your names]".
1. Change motor B to motor C to get the other wheel to turn.

> HINT: line x should be and line x should be. Maybe have a click here so they can't immediately see the link.

Great, you've written your first program. Now we need to upload it to the robot and run it.

1. Connect EV3 to PC with a cable. (EV3 must be on (green))
1. Open the Explorer (Ctrl+Shift+E) in the left panel of VSCode.
1. Expand the EV3DEV DEVICE BROWSER from the bottom of the panel and click 'Click here to connect to a device'.
1. Select your device (from the top of the screen).
1. Press F5 to download and run. Note you can re run the file unplugged as per the earlier instructions to run a program.

## Getting the robot to move

It would be inconvenient if we had to control the robot through the motor speeds individually so instead we use `DriveBase` which provides some useful functions.

```
straight()
turn()
drive()
```

- do some explaining
- say we previously moved motors individually but that's inconvenient
- we use `objects` that help us out. We will use `DriveBase`
- explain how to set up
- and what functionality it gives (i.e. which functions)
- then set some movement challenges

1. Drive forwards 1 metre
1. Drive backwards 1 metre
1. Turn 180° on the spot both ways
1. Drive in a square
1. Drive in a circle

> Challenge: get the robot to move by controlling the motors without `DriveBase`



## Sensing


1. Use the script `threshold-test.py` to determine the reflectance of the white background and the black line and make a note of these.



Practise: put a start and end line on the floor 1 metre apart. Get the robot to drive until it gets to the line.

## Racing
Now let's see if we can get our robot to race around the track by following the line!

> Challenge: Pause and see if you can work out an algorithm for the robot to follow the line.



## Thoughts
Add a start button

We're asking the robot to get from A to B but it's wearing a blindfold! It's no wonder it gets it a little bit wrong. Think about the sensory things you use to localise and navigate yourself. What could the robot use? If you were blindfolded, what might be a way you could navigate from A to B?