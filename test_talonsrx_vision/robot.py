import wpilib
import commands2
import typing
from robotcontainer import RobotContainer

class MyRobot(commands2.TimedCommandRobot):
    """
    The main robot class.
    """

    autonomousCommand: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should be used for any initialization code.
        """
        self.container = RobotContainer()

    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode"""

    def disabledPeriodic(self) -> None:
        """this function is called periodically when disabled"""

    def autonomousInit(self) -> None:
        """This function is called every time the robot enters autonomous mode."""
        self.autonomousCommand = self.container.getAutonomousCommand()
        if self.autonomousCommand:
            self.autonomousCommand.schedule()
    
    def autonomousPeriodic(self) -> None:
        """this function is called periodically during autonomous"""

    def teleopInit(self) -> None:
        """This function is called every time the robot enters teleoperated mode."""
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    #def robotPeriodic(self):
        """This function is called every robot packet, no matter the mode."""
        # This is where the CommandScheduler is run.
        #commands2.CommandScheduler.getInstance().run()

    def teleopPeriodic(self) -> None:
        """This function is called periodically during teleoperated mode."""
        # Add any periodic teleop logic here

    def testInit(self) -> None:
        """ This function is called every time the robot enters test mode. """
        commands2.CommandScheduler.getInstance().cancelAll()

