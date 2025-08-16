import wpilib
import commands2
from commands import aimAtAprilTag
import constants
from wpilib.interfaces import GenericHID
from subsystems.drive_subsystem import DriveSubsystem
from commands.Autos import Autos
from subsystems.vision_subsystem import VisionSubsystem
from commands.aimAtAprilTag import AimAtAprilTag

class RobotContainer:
    def __init__(self) -> None: #, speed, duration
        # Create subsystems
        self.drive_subsystem = DriveSubsystem()
        self.vision_subsystem = VisionSubsystem()

        # The driver's controller
        self.driver_controller = commands2.button.CommandXboxController(constants.kDriverControllerPort) # or use Joystick if appropriate

        #self.aimAtAprilTag = aimAtAprilTag() #self.drive_subsystem, self.vision_subsystem, april_tag_id = 7)

        self.autos = Autos()

        # Configure button bindings
        self.configureButtonBindings()

    # Function to bind commands to buttons on the driver and operator controllers.
    def configureButtonBindings(self):
        
        self.drive_subsystem.setDefaultCommand(
            self.drive_subsystem.arcadeDrive(
                self.drive_subsystem,
                lambda: -self.driver_controller.getLeftY(), #control forward and back
                lambda: -self.driver_controller.getRightX(),  #control left and right #removed a comma Aug15, did this change anything?
            )
        )
        
        """
        commands2.button.JoystickButton(self.driver_controller, 1).whileTrue(
            aimAtAprilTag(self.drive_subsystem, self.vision_subsystem, april_tag_id = 7)) # Replace with your chosen AprilTag ID
        """
        
        self.driver_controller.b().whileTrue(AimAtAprilTag(self.drive_subsystem, self.vision_subsystem, april_tag_id = 7)) #should this be "and" with latest_result.hasTargets()???

    def getAutonomousCommand(self) -> commands2.Command:
        #return self.autos.exampleAuto(self.drive_subsystem) #TODO need to enderstan why error is created for sending 2 variables
        pass