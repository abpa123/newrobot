# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       adityabanwasi                                                #
# 	Created:      12/29/2023, 2:04:58 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

#region VEXcode Generated Robot Configuration
from vex import *

brain=Brain()


# ------------- Robot Initialization Code ------------- #

# To add a new device do the following:
# 1. Add a variable name and add the corresponding code
# 2. Define a function below in the Actual Code section
# 3. Call it in the system event handlers

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

# ---------------------------------------------------- #



# **************************************** DO NOT TOUCH THIS CODE **************************************** #

# wait for rotation sensor to fully initialize
wait(30, MSEC)

def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    drivetrain_inertial.calibrate()
    while drivetrain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


def play_vexcode_sound(sound_name): # sound stuff, no need to touch this
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")



controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True
controller_1_up_down_buttons_control_motors_stopped = True
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False


# Edit Dec 29: I added backslashes to make the global span over multiple lines
# Remove the "\" on each line and make it one singular line if it causes problems

def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, \
    drivetrain_r_needs_to_be_stopped_controller_1, \
    controller_1_left_shoulder_control_motors_stopped, \
    controller_1_right_shoulder_control_motors_stopped, \
    controller_1_up_down_buttons_control_motors_stopped, \
    remote_control_code_enabled
    
    # ------------- Drivetrain Code ------------- #

    while True:
        if remote_control_code_enabled:
            if drivetrain_inertial.is_calibrating():
                left_drive_smart.stop()
                right_drive_smart.stop()
                while drivetrain_inertial.is_calibrating():
                    sleep(25, MSEC)
            
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    left_drive_smart.stop()
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    right_drive_smart.stop()
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
            
    # ------------------------------------------- #

            # ------------- Intake Code ------------- #
            
            if controller_1.buttonL1.pressing():
                IntakeSpin.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                IntakeSpin.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                IntakeSpin.stop()
                controller_1_left_shoulder_control_motors_stopped = True

            # --------------------------------------- #


            # ------------- Flywheel Code ------------- #

            if controller_1.buttonR1.pressing():
                Flywheel.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                Flywheel.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                Flywheel.stop()
                controller_1_right_shoulder_control_motors_stopped = True
            if controller_1.buttonUp.pressing():
                FlywheelUpDown.spin(FORWARD)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif controller_1.buttonDown.pressing():
                FlywheelUpDown.spin(REVERSE)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif not controller_1_up_down_buttons_control_motors_stopped:
                FlywheelUpDown.stop()
                controller_1_up_down_buttons_control_motors_stopped = True

            # ----------------------------------------- #

        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration


# ******************************************************************************************************** #


# **************************************** START OF ACTUAL CODE **************************************** #

# ------------- Driver Code ------------- #

# The following functions are commands for the 
# controller to perform functions, I am not sure 
# what "myVariable" does at the moment


# How to define new function in this code:

# def when_started#(): (continue the convention)
#   global myVariable
#   insert code here...


myVariable = 0

def when_started1():
    global myVariable
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    IntakeSpin.set_velocity(100, PERCENT)
    FlywheelUpDown.set_velocity(70, PERCENT)
    Flywheel.set_velocity(100, PERCENT)

def when_started2():
    global myVariable
    sideskirt.set(False)

def onevent_controller_1buttonX_pressed_0():
    global myVariable
    sideskirt.set(True)

def onevent_controller_1buttonY_pressed_0():
    global myVariable
    sideskirt.set(False)

def when_started3():
    global myVariable
    if controller_1.buttonDown.pressing():
        FlywheelUpDown.spin(REVERSE)
    else:
        FlywheelUpDown.stop()

def when_started4():
    global myVariable
    if controller_1.buttonL1.pressing():
        IntakeSpin.spin(FORWARD)
    else:
        IntakeSpin.stop()

def when_started5():
    global myVariable
    if controller_1.buttonL2.pressing():
        IntakeSpin.spin(REVERSE)
    else:
        IntakeSpin.stop()

def when_started6():
    global myVariable
    if controller_1.buttonUp.pressing():
        FlywheelUpDown.spin(FORWARD)
    else:
        FlywheelUpDown.stop()

def when_started7():
    global myVariable
    if controller_1.buttonR2.pressing():
        Flywheel.spin(REVERSE)
    else:
        Flywheel.stop()

def when_started8():
    global myVariable
    if controller_1.buttonR1.pressing():
        Flywheel.spin(FORWARD)
    else:
        IntakeSpin.stop()

# --------------------------------------- #



# ------------- Autonomous Code ------------- #

# Add in auton code in the function below here
# Define seperate functions to make code readable
# above, make sure to call them in function below

def onauton_autonomous_0():
    global myVariable
    drivetrain.drive_for(FORWARD, 200, MM) # placeholder for now

# Call the autonomous function - do not touch this
def vexcode_auton_function():
    auton_task_0 = Thread( onauton_autonomous_0 )
    while( competition.is_autonomous() and competition.is_enabled() ):
        wait( 10, MSEC )
    auton_task_0.stop()

# ------------------------------------------- #



# ------------- Call Things Code - Do Not Touch This ------------- #

# Call the driver function - do not touch this
def vexcode_driver_function():
    while( competition.is_driver_control() and competition.is_enabled() ):
        wait( 10, MSEC )


# register the competition functions - do not touch this
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# Calibrate the Drivetrain - do not touch this
calibrate_drivetrain()

# ---------------------------------------------------------------- #




# ------------- System Event Handlers ------------- #

# these commands call the functions defined above
# note: add a new line below 
# (eg. controller_1.buttonA.pressed(onevent)...) to tell 
# VEX that you are using a new type of button to do 
# something, won't work without this

controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
controller_1.buttonY.pressed(onevent_controller_1buttonY_pressed_0)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Call all the functions below 
# (including new ones you defined), VEX abbreviates the 
# "when started #" functions "ws#", follow convention

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
ws4 = Thread( when_started4 )
ws5 = Thread( when_started5 )
ws6 = Thread( when_started6 )
ws7 = Thread( when_started7 )
ws8 = Thread( when_started8 )
when_started1()

# -------------------------------------------------- #

# ****************************************************************************************************** #

        
