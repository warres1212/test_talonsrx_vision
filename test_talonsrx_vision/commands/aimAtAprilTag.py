import commands2
import wpimath.controller
import wpilib
from subsystems.drive_subsystem import DriveSubsystem
from subsystems.vision_subsystem import VisionSubsystem

class AimAtAprilTag(commands2.Command):
    def __init__(self, drive_subsystem: DriveSubsystem, vision_subsystem: VisionSubsystem, april_tag_id: int, target_yaw_setpoint: float = 0.0, turn_kP: float = 0.05):
        super().__init__()
        self.drive = drive_subsystem
        self.vision = vision_subsystem
        self.april_tag_id = april_tag_id
        self.target_yaw_setpoint = target_yaw_setpoint
        self.turn_kP = turn_kP  # Proportional gain for turning
        #Adjust the turn_kP to fine-tune the aiming response. 

        self.addRequirements(self.drive, self.vision)

        self.turn_controller = wpimath.controller.PIDController(self.turn_kP, 0.0, 0.0)
        self.turn_controller.setSetpoint(self.target_yaw_setpoint)
        self.turn_controller.setTolerance(1.0)  # Tolerance in degrees

        wpilib.SmartDashboard.putNumber("Turn_kP", self.turn_kP)
        wpilib.SmartDashboard.putNumber("Target Yaw Setpoint", self.target_yaw_setpoint)
        wpilib.SmartDashboard.putNumber("Target AprilTag ID", self.april_tag_id)

    def initialize(self):
        print("Initialize method")
        self.turn_controller.reset()

    def execute(self):
        #print(" made it to AimAtAprilTag execute")
        target_yaw = self.vision.get_target_yaw(self.april_tag_id)
        wpilib.SmartDashboard.putNumber("Turn Output", target_yaw)
        print(f"Target Yaw is: {target_yaw}")

        if target_yaw is not None:
            turn_output = self.turn_controller.calculate(target_yaw)
            xSpeed = 0.0  # no forward movement
            print(f"Turn output is: {turn_output}")
            wpilib.SmartDashboard.putNumber("Turn Output", turn_output)
            self.drive.arcadeDrive(self.drive, xSpeed, turn_output)  # Only turn, no forward movement
        else:
            print("AimatAprilTag stop motor")
            self.drive.stop() # Stop if no target found

    def isFinished(self) -> bool:
        print("AimatAprilTag isFinished method")
        return self.turn_controller.atSetpoint() or self.vision.get_target_yaw(self.april_tag_id) is None

    def end(self, interrupted: bool):
        print("AimatAprilTag end method")
        self.drive.stop()