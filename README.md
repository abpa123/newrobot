# ‎‎VEX Team 21919A Github Repository

This is home of VEX Team 21919A's code, where all the code for their new robot lies. This repository houses the code that powers our innovative robot design, which features a flywheel mechanism for projectile launching. The code in this repository marks a significant departure from our previous catapult-based system. Read on to learn how to navigate this repository, contribute to the code, and access helpful documentation. 

To maintain code integrity and version control, we've implemented restricted access. To help someone get viewing and editing access to the files in this repository, simply ask the owner to invite them to collaborate. Cloning: Once granted access, proceed to clone the repository onto your local machine using the following command `git clone https://github.com/abpa123/newrobot` in your computer's built-in terminal or use github desktop for a more stable way to bring it to your code editor (steps are described below).

#### Navigating and Editing the Code:

Key Files and Folders in this repository: `.vscode`: This is just some VEX code setting and preliminary files settings for the project. You will not have to change anything in this file, since it does not affect robot fuctionality. `src`: Contains the primary source code files for the robot's functionality. `main.py`: This is the where the code file with all the important functions are. There is no other main code file that has to be downloaded to the robot. `.DS_store`: At the moment, I am not sure what this is. `.gitignore`: This is simply for github integration, no need to use this file. Finally, `README.md`: This is this very file you are reading right now.

> [!TIP]
> #### How to maintain and store working code:
> - Review: Please carefully review existing code before making modifications to ensure compatibility and avoid unintended consequences. There are clearly marked sections that should tell you what can and cannot be edited so that the VEX robot functions correctly and all mechanisms work to the desired effect.
> - Clear Comments: Add descriptive comments to explain any changes made for future reference and maintain code readability.
> - Testing: Test all code changes incrementally by testing small functions line by line. This is important due to the precision required in the robot, especially during the autonomous stages of the competition, where there is absolutley no input from the driver.

## How to Get Access to this Repository

There are multiple steps that need to be taken to use this github repository. One way throught your computer's built in terminal was outlined above, however to integrate this repository into Github Desktop, which is an application that smoothens the process of editing and viewing files connected with github, simply read the steps outlined below. There are also some important settings that you may need to change for editing and downloading code to the robot to work, which is also described below.

#### Open this Repository on Github Desktop:
> 1. Download Github Desktop. You can do this by going to https://desktop.github.com/ and downloading their software.
> 2. Open on Github Desktop. Once you have github desktop downloaded go to the github repository and look for the button that says "`<> Code`". The dropdown should allow you to "Open on Github Desktop".
> 3. Clone Repository. The popup should allow you to hit the clone button, which despite the wording actully simply opens it on your device and does not create a new version.

By completing the above steps you should be able to hit "Open in Visual Studio Code", which should allow you to start editing. You might see a different editor that is not Visual Studio Code. The steps to change you editor are outlined below. All the important preliminary setup that you need to do is also described below.

> [!IMPORTANT]
> #### Settings in these applications:
> - You may see in Github Desktop something other than Visual Studio Code, such as PyCharm. The code only works on Visual Studio Code. To change the app you open the repository with, simply go to Settings, Integration and change the external editor you are using.
> - In Visual Studio Code you need to have the VEX extension downloaded. For the code to download to a robot, or for it to actually run, you will need the Visual Studio Code extension downloaded. To do this, go to the extensions tab and search up "VEX". Look for the official VEX extension and download it. 


## Important Notes on editing the code

There are a few main sections you may find yourself editing when working on the code. There are specific sections in the code that should not be edited because the VEX robot relies on this code being there for certain crucial functions to work. However, most of the code is meant to be changed and the steps for editing and adding code to these sections are outlined in the descriptions below. 

### The Robot Initialization Code
This is the section of the robot code where all initial mechanisms and functions are defined. It is where all devices, as VEX refers to them, should be defined and eventually used in the program when defining functions in the controller code. It looks like this:

```
controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT7, GearSetting.RATIO_6_1, direction)
left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_6_1, direction)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT8, GearSetting.RATIO_6_1, not direction)
right_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_6_1, not direction)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain_inertial = Inertial(Ports.PORT21) # change port number
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, drivetrain_inertial, 319.19, 320, 40, MM, 1)
IntakeSpin = Motor(Ports.PORT11, GearSetting.RATIO_6_1, direction)
FlywheelUpDown = Motor(Ports.PORT12, GearSetting.RATIO_6_1, direction)
Flywheel = Motor(Ports.PORT1, GearSetting.RATIO_6_1, direction)
sideskirt = DigitalOut(brain.three_wire_port.h)
```

To add a device or change the code, add your device below and add the corresponding code such as `DigitalOut()` or `Motor()`. Then define a function that uses that device later in the `main.py` code file and finally call it in the system event handlers. Every device needs to be called in the system event handlers. It will not work without these steps.


### Driver Code

The driver code has commands for all types of driver functions. This is where you program things that the controller will execute. You should have defined the device that is performing the function in the robot initialization code. The basic layout of code in the driver code section looks like this:

```
def when_started1():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    IntakeSpin.set_velocity(100, PERCENT)
    FlywheelUpDown.set_velocity(70, PERCENT)
    Flywheel.set_velocity(100, PERCENT)
```

When adding your function, be sure to continue the number system when naming the function. Note that `whenstarted1()` is the initial function and it is where you define initial characteristics such as velocity for the driver period. After creating your function, be sure to call it in the system event handlers. They look like this:

```
ws2 = Thread(when_started2)
ws3 = Thread(when_started3)
```

There are a few main ways to define a new function. In that same driver code, create a function that uses a button such as A, B, X, or Y. You can do this by creating a button function like the following: 

```
def onevent_controller_1buttonX_pressed_0():
    insert code here...
```

Then use this code later in the system event handlers by telling VEX that you are using that button and when that button is pressed, call the function you defined earlier. In this example, the function that will call is that `onevent_controller_1buttonX_pressed_0()` function. You can do this in the system event handlers by doing something like this, instead with your function name, which should be named similarly:


```
controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
```

Note that everything eventually should be called in the system event handlers, in order for the function defined in the controller code to run in the first place, either by using the `ws2 = Thread(when_started2)` approach or the `controller_1.buttonX.pressed(onevent...` version depending on the type of event being executed. Use the second type when trying to execute an action using one of the letter buttons.

### Autonomous Code

The Autonomous Code is broken down into many functions in order to allow for better testing and the creation of new functions. VEX primarily has only two main times pre-programmed code is run. This is in the fifteen second autonomous and the one minute autonomous skills challenge. There is a section in the code deemed "Both Autons" which is code applicable for both of these autonomous programs. Then there is the "One Min Auton" part, which is only to be used for the skills challenge. To add a function that performs a specific task, such as scoring a matchload, define a function in one of these areas:

```
def score_matchload():

    # Score Matchload in close goal

    drivetrain.drive_for(FORWARD, 60, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 12, INCHES)
    IntakeSpin.spin(REVERSE) # score matchload
```

Now this function needs to be called in either the `fifteen_second_auton()` function, the `one_min_auton()` or both. One of these function will finally be called in the main autonomous function, `onauton_autonomous_0()`. Change the function that is called in this function to the right autonomous code, depending on whether you are doing skills or a normal match. This main function is later called in the `vexcode_auton_function()`, which is what runs when autonomous is enabled during competition. To outline these steps, each of the functions are shown below in order (just the matchload function is displayed for understanding).

```
[a lot of code here]

def fifteen_second_auton():
    score_matchload()

def one_min_auton():
    score_matchload()

[a lot of code here]

def onauton_autonomous_0():
    initialization() # needed for both autons
    fifteen_second_auton()

[more code]

def vexcode_auton_function():
    auton_task_0 = Thread(onauton_autonomous_0) # call main auton function
    while(competition.is_autonomous() and competition.is_enabled()):
        wait(10, MSEC)
    auton_task_0.stop()
```

### All other Code

The driver and autonomous code is the main code that will be edited, however there are instructions in the code for what can and cannot be edited in other sections. It should be clearly marked in the comments (Things that look like this: `#`). Test the robot functionality if you make any changes to important VEX code.

## Documentation


> While the visual studio code extension does not have much documentation or support, the code used for the extension is actually the same as the code used for the vexcode v5 app. The advantage of the extension is github is compatible with the code editor, so your code can be saved in stages. Vexcode v5 has documentation built into their application. In the app, or the web version, simply click the "?" to figure out what a command does and all the paramaters it uses. The vexcode v5 app commands are the same as the vscode extension commands. To access the web version go to https://codev5.vex.com/ and to download the app go here: https://www.vexrobotics.com/vexcode/install/v5 and download it for your operating system.

## Tips and Information for the Tournament

### Autonomous:

- Close Fifteen Second Autonomous is Slot 1: This ends up scoring the matchload and intaking and scoring two triballs for a total score of 15 points in the autonomous. It scores 3 triballs with about a 75 percent accuracy, two triballs with a 90 percent accuracy and one triball at a 100 percent accuracy. 
- Far Fifteen Second Autonomous is Slot 2: This ends up simply scoring one matchload for a total of 5 points.
- One Minute Autonomous is Slot 3: This starts with the matchload functionality where the flywheel arm raises and the flywheel spins. Two people will matchload into the flywheel. 2 points are scored for every triball that lands up on the other side (not scored) and 5 points for each one scored. When we ran this we got about 50 or more points.

### Match-loading:

- Try to matchload the triballs as fast as possible during driver skills and programming skills. For driver skills, matchload for 25 seconds, which is when the controller shows 35 seconds remain. Then try scoring the triballs on the field. When we did this we got about 80 points, although higher is totally possible.
- Remember that the bottom right shoulder button (R2) makes the flywheel spin in the direction so that it shoots towards the goal. The up arrow moves the arm up and the down arrow moves it down.
- Remember to hold the up arrow when match-loading so the arm doesn't fall back down.

### General Advice:

- Stay calm, but also attempt to do things efficiently and quickly. If something breaks, tell the team and don't panic. You will get it done before your next match.
- Always keep in mind when you will do driver skills, programming skills, and judging. These can be very valuable and you do not want to miss out on them.
- Talk with your alliance beforehand and try to get a sense of what your opponents will do. Think about who you could pair up with during the tournament.
