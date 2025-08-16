import commands2
import commands2.button.commandxboxcontroller
import wpilib.drive
import constants
from subsystems.drive_subsystem import DriveSubsystem

class DriveDefaultCommand(commands2.Command):
    def __init__(self, drive_subsystem:DriveSubsystem, driver_controller):
        super().__init__() #"DriveDefaultCommand", drive_subsystem)
        self.drive_subsystem = DriveSubsystem
        self.driver_controller = driver_controller
        self.addRequirements(DriveSubsystem) # This command requires the drive subsystem

    def execute(self):
        """
        Called repeatedly when this Command is scheduled to run.
        """
        # Get joystick input and use it to control the drivetrain
        x_speed = -self.driver_controller.getLeftY() # Invert Y if needed
        z_rotation = self.driver_controller.getRightX() # X-axis for rotation

        self.drive_subsystem.arcadeDrive(x_speed, z_rotation)

    def isFinished(self):
        """
        Returns true when this Command no longer needs to run execute().
        """
        return False # Default commands typically run indefinitely