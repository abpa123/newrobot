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


### Driver Code, Autonomous Code, and Other Code

This is what you will be editing most of the time to code driver commands and autonomous commands for the robot. Steps editing for each section are outlined in comments (Things that look like this: `#`) in the code.
