# Toy robot

## Description
The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units. There are no other obstructions on the table surface.

The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.


Create an application that can read in commands of the following form:
* PLACE X,Y,F
* MOVE
* LEFT
* RIGHT
* REPORT


PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed. 


MOVE will move the toy robot one unit forward in the direction it is currently facing. 


LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. 

REPORT will announce the X,Y and orientation of the robot. 

A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands. 

Provide test data to exercise the application.


## Constraints:
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.


Example Input and Output:
a) PLACE 0,0,NORTH MOVE REPORT Output: 0,1,NORTH

b) PLACE 0,0,NORTH LEFT REPORT Output: 0,0,WEST

c) PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT Output: 3,3,NORTH


## Deliverables:
The source files, the test data and any test code.

## Implementation
As the language for the implementation was not specified, I have implemented in Python.
Developed on Python version 3.60 but should work with anything above 3.4 (using enumerations that were added in version 3.4)

The only relevant files are:
* toy_robot.py
* test_toyRobot.py


toy_robot.py is main application file, it contains:
* ToyRobot class that is implementation of the solution for the task given.
* Direction class that is a helper, enumeration for directions used in application
* infinite loop reading and interpreting user console input

test_toyRobot.py is unit test file with all defined unit tests, both for private and public elements of the ToyRobot class

All other files are part of the PyCharm IDE solution, my favourite Python development IDE, made by JetBrains (https://www.jetbrains.com/pycharm/)

## Usage
I'm assuming you have Python installed on your computer.
Start python script from command line with:
python toy_robot.py


Application will read any text you have entered after you've presed enter.
Application will parse the text entered and try to extract command from it. The parsing of the command is fairly forgiving, upper and lower caps are interpreted the same, spaces before, after on between command and parameter are ignored. This is important only for the place command, all other commands are siggle word only and no parameters.

So all of the following and similar combinations will be interpreted as valid:
* place 0, 0, north
* PLACE 0, 0, NORTH
*         place             0,      0,     north
* plACE  0, 0, NOrtH

You can exit the application with Ctrl+C

If I haven't forgot anything, that should be all for this task.
