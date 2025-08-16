import commands2
import commands2.button.commandxboxcontroller
import wpilib
import constants
from subsystems.drive_subsystem import DriveSubsystem

class DriveStraightCommand(commands2.Command):
    def __init__(self, drive_subsystem:DriveSubsystem, speed: float, duration: float):
        super().__init__() #"DriveDefaultCommand", drive_subsystem)
        self.drive_subsystem = DriveSubsystem
        self.speed = speed
        self.duration = duration
        self.addRequirements(drive_subsystem) # This command requires the drive subsystem
        self.timer = wpilib.Timer()

    def initialize(self):
        """
        Called once when the Command is initially scheduled.
        """
        self.timer.reset()
        self.timer.start()
        self.drive_subsystem.arcadeDrive(self.speed, 0)

    def execute(self):
        """
        Called repeatedly when this Command is scheduled to run.
        """
        pass

    def isFinished(self):
        """
        Returns true when this Command no longer needs to run execute().
        """
        return self.timer.hasElapsed(self.duration) # Default commands typically run indefinitely
    
    def end(self):
        """called once when the command ends or is interrupted."""
        self.timer.stop()
        self.drive_subsystem.stop() # stop the robot when the command ends.