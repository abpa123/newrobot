# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       adityabanwasi                                                #
# 	Created:      12/29/2023, 2:04:58 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# region VEXcode Generated Robot Configuration
from vex import *

brain = Brain()


# ------------- Robot Initialization Code ------------- #

# ---------- Instructions --------- #

# To add a new device do the following:
# 1. Add a variable name and add the corresponding code
# 2. Define a function below in the Actual Code section
# 3. Call it in the system event handlers

# Cartridge Ratios:
# 1. Red Cartridge: 36 to 1 (100 RPM)
# 2. Green Cartridge: 18 to 1 (200 RPM)
# 3. Blue Cartridge: 6 to 1 (600 RPM)

# Motor Directions
# direction variable is set to False
# False is counterclockwise, Normal in vexcode v5
# True is clockwise, Reverse in vexcode v5

# drivetrain set to two direction and two not direction

# --------------------------------- #

# Robot Configuration Code

direction = False

# --- Controller and Drivetrain --- #

controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_6_1, not direction)
left_motor_b = Motor(Ports.PORT8, GearSetting.RATIO_6_1, not direction)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_6_1, direction)
right_motor_b = Motor(Ports.PORT7, GearSetting.RATIO_6_1, direction)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain_inertial = Inertial(Ports.PORT13) # change port number
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, drivetrain_inertial, 319.19, 320, 40, MM, 1)

# --------------------------------- #

# ----------- Mechanisms ---------- #

IntakeSpin = Motor(Ports.PORT11, GearSetting.RATIO_6_1, direction)
FlywheelUpDown = Motor(Ports.PORT12, GearSetting.RATIO_6_1, direction)
Flywheel = Motor(Ports.PORT1, GearSetting.RATIO_6_1, direction)
sideskirt = DigitalOut(brain.three_wire_port.h)

# --------------------------------- #

# ----------------------------------------------------- #



# **************************************** DO NOT TOUCH THIS CODE **************************************** #

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# ------------ Calibrate and Define Motors ------------ #

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

# ----------------------------------------------------- #

# ------------------ Controller Loop ------------------ #

def rc_auto_loop_function_controller_1():

    # I added backslashes to make the global span over multiple lines
    # Remove the "\" on each line and make it one singular line if it causes problems

    global drivetrain_l_needs_to_be_stopped_controller_1, \
    drivetrain_r_needs_to_be_stopped_controller_1, \
    controller_1_left_shoulder_control_motors_stopped, \
    controller_1_right_shoulder_control_motors_stopped, \
    controller_1_up_down_buttons_control_motors_stopped, \
    remote_control_code_enabled

    while True:

        # This code simply makes sure that the Drivetrain
        # functions as it should, starting and stopping
        # when needed and takes care of the inertial
        # sensor in the middle of the robot

        if remote_control_code_enabled:

            # ------ Inertial Sensor Code ----- #

            if drivetrain_inertial.is_calibrating():
                left_drive_smart.stop()
                right_drive_smart.stop()
                while drivetrain_inertial.is_calibrating():
                    sleep(25, MSEC)
            
            # --------------------------------- #

            # -------- Drivetrain Code -------- #
            
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
            
            # --------------------------------- #

            # ---------- Intake Code ---------- #
                
            # This code simply makes sure that the 
            # Intake functions as it should, starting 
            # and stopping when needed, to adjust 
            # directions change values for .spin() 
            # in both this and the controller code
            
            if controller_1.buttonL1.pressing():
                IntakeSpin.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                IntakeSpin.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                IntakeSpin.stop()
                controller_1_left_shoulder_control_motors_stopped = True

            # --------------------------------- #

            # --------- Flywheel Code --------- #

            # This code simply makes sure that the 
            # Flywheel functions as it should, starting 
            # and stopping when needed, to adjust 
            # directions change values for .spin() 
            # in both this and the controller code

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
                FlywheelUpDown.spin(REVERSE)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif controller_1.buttonDown.pressing():
                FlywheelUpDown.spin(FORWARD)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif not controller_1_up_down_buttons_control_motors_stopped:
                FlywheelUpDown.stop()
                controller_1_up_down_buttons_control_motors_stopped = True

            # --------------------------------- #
                
        wait(20, MSEC)

# ----------------------------------------------------- #


# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

# ******************************************************************************************************** #
# endregion VEXcode Generated Robot Configuration


# **************************************** START OF ACTUAL CODE **************************************** #

# ------------- Driver and Controller Code ------------ #

# The following functions are commands for the 
# controller to perform functions

# ------- Define a Function ------- #

# Method 1:
# Define normal mechanism
# def when_started[#]():
#   [code for mechanism]
# Call in system event handlers:
# ws[#] = Thread(when_started[#])

# Method 2:
# Define functions for letter buttons:
# def onevent_controller_1buttonA_pressed_0():
#   [code to be executed when A pressed]
# Call in system event handlers:
# controller_1.buttonA.pressed(onevent...)

# --------------------------------- #

# ------------- Setup ------------- #

def when_started1():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    IntakeSpin.set_velocity(100, PERCENT)
    FlywheelUpDown.set_velocity(70, PERCENT)
    Flywheel.set_velocity(100, PERCENT)

# --------------------------------- #

# ------------- Wings ------------- #

def when_started2():
    sideskirt.set(False) # orginally set to closed

# on the letter buttons on controller

def onevent_controller_1buttonX_pressed_0():
    sideskirt.set(True) # when X pressed, open wings


def onevent_controller_1buttonY_pressed_0():
    sideskirt.set(False) # when Y pressed, close wings

# --------------------------------- #

# ------------ Flywheel ----------- #

def when_started3():
    if controller_1.buttonDown.pressing():
        FlywheelUpDown.spin(FORWARD)
    else:
        FlywheelUpDown.stop()


def when_started4():
    if controller_1.buttonUp.pressing():
        FlywheelUpDown.spin(REVERSE)
    else:
        FlywheelUpDown.stop()


def when_started5():
    if controller_1.buttonR2.pressing():
        Flywheel.spin(REVERSE)
    else:
        Flywheel.stop()


def when_started6():
    if controller_1.buttonR1.pressing():
        Flywheel.spin(FORWARD)
    else:
        IntakeSpin.stop()

# --------------------------------- #

# ------------- Intake ------------ #

def when_started7():
    if controller_1.buttonL1.pressing():
        IntakeSpin.spin(FORWARD)
    else:
        IntakeSpin.stop()


def when_started8():
    if controller_1.buttonL2.pressing():
        IntakeSpin.spin(REVERSE)
    else:
        IntakeSpin.stop()

# --------------------------------- #

# ----------------------------------------------------- #


# ---------------- All Autonomous Code ---------------- #
  
# ---------- Both Autons ---------- #

# This is code applicable for both the 
# one min auton and fifteen second auton
# Intake Directions:
# Reverse is intake, Forward is outtake

def initialization():

    # Set everything up, Set velocities

    drivetrain.set_drive_velocity(80, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    IntakeSpin.set_velocity(100, PERCENT)
    FlywheelUpDown.set_velocity(70, PERCENT)
    Flywheel.set_velocity(100, PERCENT)


def score_matchload():

    # Score Matchload in close goal

    drivetrain.drive_for(FORWARD, 98, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    IntakeSpin.spin(FORWARD) # score matchload
    drivetrain.drive_for(FORWARD, 12, INCHES)
    # wait(500, MSEC) # wait while scoring
    drivetrain.drive_for(REVERSE, 4, INCHES)
    wait(500, MSEC)


def score_triball():

    # Intake One Triball and score it
    
    wait(50, MSEC)
    IntakeSpin.spin(REVERSE) # start intaking while driving
    drivetrain.drive_for(REVERSE, 27, INCHES)
    drivetrain.set_turn_velocity(50, PERCENT) # lower turn velocity
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.set_drive_velocity(15, PERCENT)
    drivetrain.drive_for(FORWARD, 12, INCHES)
    drivetrain.set_drive_velocity(80, PERCENT)
    IntakeSpin.spin(REVERSE) # intake triball
    wait(500, MSEC) # wait while intaking
    drivetrain.drive_for(REVERSE, 12, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 20, INCHES)
    IntakeSpin.spin(FORWARD) # score triball
    wait(500, MSEC) # wait while scoring
    drivetrain.drive_for(FORWARD, 6, INCHES) # push triball in


def knock_triball():

    # Go to corner, Knock triball out of 
    # match load zone using wings

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 98, INCHES)
    sideskirt.set(True) # deploy wings
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.turn_for(RIGHT, 360, DEGREES) # knocks triball out


def touch_elev_bar():
    # Touch Elevation Bar
    drivetrain.drive_for(FORWARD, 54, INCHES)

# --------------------------------- #

# ------- Only One Min Auton ------ #

# Only use this for the one minute auton,
# since it exceeds fifteen seconds in the
# normal match autonomous

def one_min_auton_second_triball():
    # Intake another triball and score it
    drivetrain.turn_for(LEFT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 48, INCHES)
    IntakeSpin.spin(FORWARD) # intake triball
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 48, INCHES)
    IntakeSpin.spin(REVERSE) # score triball

# --------------------------------- #

# ------ Final Main Functions ----- #

# Call the functions above in the 
# respsective autons below, finally 
# calling it in the main function

# --- Fifteen Second --- #

def fifteen_second_auton():

    # This ends up scoring the matchload,
    # intaking and scoring one triball,
    # knocking the triball in the match
    # load zone out, and touching the 
    # elevation bar

    score_matchload()
    score_triball()
    # knock_triball()
    # touch_elev_bar()

# ---------------------- #

# ----- One Minute ----- #

def one_min_auton():

    # This ends up scoring the matchload,
    # and intaking and scoring two triballs

    score_matchload()
    score_triball()
    one_min_auton_second_triball()

# ---------------------- #

# Call the auton function below,
# either the fifteen_second_auton()
# or the  one_min_auton()
    
# Change function before skills

# ----- Main Auton ----- #

# This is the final main auton 
# function that will end up 
# running in competition

def onauton_autonomous_0():

    # This ends up initilizating velocities,
    # and it calls the autonomous function

    initialization()
    fifteen_second_auton()

# ---------------------- #

# --------------------------------- #

# ----------------------------------------------------- #



# ----- Call Driver and Autonomous - Do Not Touch ----- #

# Call the main, overall autonomous function - do not touch this
def vexcode_auton_function():
    auton_task_0 = Thread(onauton_autonomous_0) # call main auton function
    while(competition.is_autonomous() and competition.is_enabled()):
        wait(10, MSEC)
    auton_task_0.stop()


# When it is the driver section, start driver functions - do not touch this
def vexcode_driver_function():
    while(competition.is_driver_control() and competition.is_enabled()):
        wait(10, MSEC)


# register the competition functions - do not touch this
competition = Competition(vexcode_driver_function, vexcode_auton_function)

# Calibrate the Drivetrain - do not touch this
calibrate_drivetrain()

# ----------------------------------------------------- #



# --------------- System Event Handlers --------------- #

# these commands call the functions defined above
# note: add a new line below 
# (eg. controller_1.buttonA.pressed(onevent)...) to tell 
# VEX that you are using a new type of button to do 
# something, won't work without this

controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
controller_1.buttonY.pressed(onevent_controller_1buttonY_pressed_0)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Call all the when_started() functions below 
# (including new ones you defined), VEX abbreviates the 
# "when started #" functions "ws#", follow convention

ws2 = Thread(when_started2)
ws3 = Thread(when_started3)
ws4 = Thread(when_started4)
ws5 = Thread(when_started5)
ws6 = Thread(when_started6)
ws7 = Thread(when_started7)
ws8 = Thread(when_started8)
when_started1() # Intial Setup Function

# ----------------------------------------------------- #

# ****************************************************************************************************** #

