import commands2
from commands.drive_straight_command import DriveStraightCommand # Assuming a DriveStraightCommand
from commands2 import SequentialCommandGroup
from subsystems.drive_subsystem import DriveSubsystem

class AutonomousCommand(commands2.Command):
    def __init__(self, drive_subsystem:DriveSubsystem):
        super().__init__(
            DriveStraightCommand(drive_subsystem, 1.0, 3.0)) # Drive straight at 1.0 speed for 3 seconds
        # Add more commands sequentially for autonomous routine