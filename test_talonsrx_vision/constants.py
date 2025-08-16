#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

"""
A place for the constant values in the code that may be used in more than one place.
This offers a convenient resources to teams who need to make both quick and universal
changes.
"""

from wpimath.kinematics import DifferentialDriveKinematics
import wpilib
import math

# ID for the driver's joystick.
kDriverControllerPort = 0

# The CAN IDs for the drivetrain motor controllers.
kLeftMotor1CAN = 17
kLeftMotor2CAN = 16
kRightMotor1CAN = 18
kRightMotor2CAN = 19

# Encoders and their respective motor controllers.
kLeftEncoderSign = +1
kRightEncoderSign = -1  # reversed

# In meters, distance between wheels on each side of robot.
kTrackWidthMeters = 0.69
kDriveKinematics = DifferentialDriveKinematics(kTrackWidthMeters)

# Encoder counts per revolution/rotation.
kEncoderCPR = 1024
kWheelDiameterMeters = 0.15

# Please calibrate to your robot
kEncoderPositionConversionFactor = 0.7

# Addressable LED count
kLEDBuffer = 60

# Addressable LED port
kLEDPort = 0

class AutoConstants:
    kUseSqrtControl = True  # compatibility with commands from https://github.com/epanov1602/CommandRevSwerve/blob/main/docs/Command_Driving_Aiming.md
