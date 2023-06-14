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

# Ideas
- control the forward speed (faster when lower error?)