# Running the RoboRacers session
Designed to be run in 45 mins with yr 8/9 class.

The main idea behind the session is to introduce the idea that robots need sensors to see the world and be useful.

## Start of the day
- Layout laptop, charger, cable, robot, worksheet at each location
- make racetrack(s) - check whether white or black tape is best
- make some lines (for sensing)


## Start of each session
- Open VSCode
- Open the `RoboChallenge` folder
- In the terminal (command prompt, not powershell), choose the `RoboRacers` branch (`git checkout RoboRacers`) and execute `git reset --hard` to take back to latest commit (if latest commit isn't the correct one, do this...[something with origin/HEAD or origin/branchname])
- (turn on the robot) Upload the code (F5 or Fn+F5)
- Run `starting.py` on the robot to test

## The session
During the session you should circulate the room, checking no groups are falling behind. Answer questions and freely offer help so that they can experience concepts (get them to do some thinking too but they don't need to learn it as such). Try and challenge them to think. The sheet just tells them what to do to complete the task so you should be prompting them to think about what they are doing/what it means/how it can be applied or extended. A good way to do this is ask them to explain to you how it works.

Specifically from the front, do these:

- **_Start_** by getting students to sit 2 to a laptop then introduce yourselves, robotics and the session and start. For example:
    > "Hello and welcome to this RoboRacers session! I'm James and I'm from UEA where I research agricultural robotics, which is robots to help farmers produce food. Today we have some robots and you're going to be programming them. We want you to have a go and experience some of the concepts, capability and challenges of robotics. You have a worksheet that tells you everything you need to do and X and I will be helping you with it all. [commence demo] The goal by the end of the session is to get your robot to race around these racetracks - hopefully faster than this one. Make a start and ask us if you have any questions."
    - It's really good to set a robot off around the track to demo what the goal is. The default racing program goes very slowly but it captivates them that it can follow the line and saying they can do it quicker is good motivation.
- **_Half way_** through, (at least 20 mins before end) summarise work so far and move onto sensing. You could say (it's quite good to say this because they won't read the sheet): 
    > "So I can see you've all done well in getting the robot to move around, who got it to drive in a square? Did you find your robot always moved the exact amount you asked it to? Did it finish the square where it started? It's very difficult for the robot to do this - it's like asking you to walk around this room blindfolded. What we need to do is give the robot a way to _see_. In robotics, we call this sensing. You'll see that your robots are equipped with a reflectance sensor on the front which shines a light beam and measures how much the surface reflects the light. A light surface will reflect a lot and a dark surface a little. In that way, the robot can see the colour of the surface beneath it. You all have a line of black tape on your desk and you're all going to move onto the sensing part of the worksheet where you will get your robot to drive up to the black line and stop. After the robot seeing the line works, you can move onto racing around the racetracks."
- **_End_** with a summary and get them to complete feedback sheets. For example:
    > "Well done on what you've all achieved today. We hope you enjoyed yourself and have understood a little of how robots work and one of the ways in which they can see the world. You probably all experienced the challenge of tuning the robot to complete the racetrack quickly but accurately. Challenges such as this - (maybe not robot racers but) of how to complete a task quickly and accurately."
    - You could ask some of the students to tell the class of their experience or if they did something special.
    - Maybe explain to the whole class how the algorithm works.

### Starting
There aren't any solutions. The purpose is just to get them running and downloading code to the robot. They can't do anything wrong if they follow the sheet - but they probably won't so you need to be very proactive in helping them through this bit.

### Moving
Solutions
1. Forwards
    ```
    robot.straight(500)
    ```
1. Backwards
    ```
    robot.straight(-500)
    ```
1. Turn
    ```
    robot.turn(180)
    ```
1. Square
    ```
    robot.straight(300)
    robot.turn(90)
    robot.straight(300)
    robot.turn(90)
    robot.straight(300)
    robot.turn(90)
    robot.straight(300)
    robot.turn(90)
    ```
1. Circle
    The basic idea is to use this line (ratio of forward to turn speed changes circle size)
    ```
    robot.drive(100,60)
    ```
    The difference is, robot.drive() is non-blocking (unlike straight and turn) so the line will execute (instantaneously) and then the next line executed and if there is no line the program will end. HOWEVER, in /.vscode/launch.json, interactive terminal is set true which means the program will(should) stay running.
    to ensure this works in a purer sense possible solutions are
    ```
    robot.drive(100,60)
    wait(5000) # wait 5 seconds
    ```
    where using wait() for pybricks.tools (import) makes the program stay running for 5 s. Perhaps purer solution is:
    ```
    while True:
        robot.drive(100,60)
    ```
    will drive continuously

### Sensing
If they run the program whilst holding the robot in the air, nothing will happen because there's no surface infront of the sensor and it sees black so stops and the program ends.

### Racing
Starting values forward = 50, turn gain = 2.5. I've found turn can be increased to about 4 before it becomes silly. Forward speed can comfortably be increased above 100, maybe even above 200 depending on the radii of the turns.

The goal here is trial and error. Don't tell them what values to use. Get them to change them and observe the behaviour of the robot - and repeat! Eventually they will get it as good as they can (hardware and choice of control algorithm become limiting factor).

You can try and discuss with them how the robot is working. [explanation pending]
 - why does it follow the edge of one line
 - why only one side of the line
 - does it turn left/right better? (sensor placement)


## At the end (packdown)
- turn off robots
- turn off laptops
- put everything in boxes

## Troubleshooting
| issue | solution |
|-------|-----------|
| robot dies | change batteries |
| weird sensor readings | check it is parallel and correct distance from surface (about 5 mm) |
| EV3DEV device browser not showing in explorer panel | try opening a FOLDER (not a single file)|

## Extensions
Some _challenges_ are suggested throughout the worksheet

Other ideas to extend racing:
- implement bang bang control 
    ```
    FORWARD_SPEED = 80
    TURN_SPEED = 100

    while True:
        # if white, turn right
        if line_sensor.reflection() > threshold:
            robot.drive(FORWARD_SPEED, TURN_SPEED)
        else: # it's black, turn left
            robot.drive(FORWARD_SPEED, -TURN_SPEED)
    ```
- implement PI control
    ```
    FORWARD_SPEED = 50
    TURN_P = 2.5
    TURN_I = ?

    deviation_sum = 0 

    while True:
        measurement = line_sensor.reflection()
        deviation = measurement - threshold
        deviation_sum = deviation_sum + deviation
        turn_rate = TURN_P * deviation + TURN_I * deviation_sum
        
        robot.drive(FORWARD_SPEED, turn_rate)
- implement a controller on forward speed (in addition to steering) so it slows for corners (I haven't got this working smoothly yet)


# Setup (Laptop)
- VSCode
- Mindstorms extension
- pybricks, pybricks stubs
- git
- git clone <the repo> (then git checkout branch)






# Temp notes
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

- Racing: forward speed 50 and P 2.5 to start with can increase forward speed to over 100 depending on corner radii and P > 4 can be a bit jerky

## to open/setup/files
git clone <some repo>
between each group do `git reset --hard` -this will take the working directory back to the most recent commit. This is great unless they somehow commit something.
Then do `git reset --hard origin/HEAD` which will take you back to the point of the clone (or the latest pull). Alternatively, do `git log --oneline` and find the hash of the commit you want to refert to and do `git reset --hard <commithash>` - do this especially if you want to keep some of the local commits.
Instead of origin/HEAD, probably need origin/BRANCHNAME. Also give guidance on git checkout to change branch.

# Ideas
- control the forward speed (faster when lower error?)