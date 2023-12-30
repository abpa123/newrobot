# VEX Team 21919A Github Repository

This is home of VEX Team 21919A's code, where all the code for their new robot lies. This is the code used for the robot redesign that utilized a flywheel 
in comparison to the catapult used before.

## How to Get Access to this Repository

There are multiple steps that need to be taken to use this github repository. They are the following:
> 1. Download Github Desktop. You can do this by going to https://desktop.github.com/ and downloading their software.
> 2. Open on Github Desktop. Once you have github desktop downloaded go to the github repository and look for the button that says "<> Code". The dropdown should allow you to "Open on Github Desktop".
> 3. Clone Repository. The popup should allow you to hit the clone button, which despite the wording actully simply opens it on your device and does not create a new version.

By completing the above steps you should be able to hit "Open in Visual Studio Code". There are some important catches though.

> Note: You need the following things in order to use the Repository
> 1. You may see in Github Desktop something other than Visual Studio Code, such as PyCharm. The code only works on Visual Studio Code. To change the app you open the repository with, simply go to Settings, Integration and change the external editor you are using.
> 2. In Visual Studio Code you need to have the VEX extension downloaded. For the code to download to a robot, or for it to actually run, you will need the Visual Studio Code extension downloaded. To do this, go to the extensions tab and search up "VEX". Look for the official VEX extension and download it. 

## Important Notes on editing the code

There are a few main sections you may find yourself editing when working on the code. These are:

### The Robot Initialization Code
This is an important part of the code that needs to be handled with care. It looks something like this:

```
# Robot configtguration code
controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)
left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)
right_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain_inertial = Inertial(Ports.PORT21)
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, drivetrain_inertial, 319.19, 320, 40, MM, 1)
IntakeSpin = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
FlywheelUpDown = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)
Flywheel = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
sideskirt = DigitalOut(brain.three_wire_port.h)
```

To add a device or change the code, add your device below and add the corresponding code such as `DigitalOut()` or `Motor()`. Then define a function that uses that device later in the `main.py` code file and finally call it in the system event handlers. It will not work without these steps.


### Driver Code

The driver code has commands for all types of driver functions. This is where you program things that the controller will execute. You should have defined the device that is performing the function in the robot initialization code. The basic layout of code in the driver code section looks like this:

```
def when_started1():
    global myVariable
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    IntakeSpin.set_velocity(100, PERCENT)
    FlywheelUpDown.set_velocity(70, PERCENT)
    Flywheel.set_velocity(100, PERCENT)
```

When adding your function, be sure to continue the number system when naming and function and including `myVariable` although I am not sure what it does. It could be useless, it could be a VEX robotics specific thing. Note that `whenstarted1()` is the initial function and it is where you define initial characteristics such as velocity for the driver period. After creating your function, be sure to call it in the system event handlers. They look like this:

```
ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
```

There are a few main ways to define a new function. In that same driver code, create a function that uses a button such as A, B, X, or Y. You can do this by creating a button function like the following: 

```
def onevent_controller_1buttonX_pressed_0():
    insert code here...
```

Then use this code later in the system event handlers by telling VEX that you are using that button and when that button is pressed, call the function you defined earlier. The function that will call is that `onevent_controller_1buttonX_pressed_0()` function. You can do this in the system event handlers by doing something like this, instead with your function name:


```
controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
```

### Autonomous Code

To create autonomous code, look for the `onauton_autonomous_0()` function. This is where you should put your code. If you want to create seperate functions to make the code more organized or to test specific sections, simply define it above and call it in the main autonomous function.

### All other Code

The driver and autonomous code is the main code that will be edited, however there are instructions in the code for what can and cannot be edited in other sections. It should be clearly marked in the comments (Things that look like this: `#`). Test the robot functionality if you make any changes to important VEX code.

## Documentation

While the visual studio code extension does not have much documentation or support, it is actually the same as the vexcode v5 app. The code is the same thing and vexcode v5 has documentation built in. In the app, or the web version, simply click the "?" to figure out what a command does and all the paramaters it uses. The vexcode v5 app commands are the same as the vscode extension commands. To access the web version go to https://codev5.vex.com/ and to download the app go here: https://www.vexrobotics.com/vexcode/install/v5 and download it for your operating system.












