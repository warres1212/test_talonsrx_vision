import commands2
import wpilib
import phoenix5
import wpilib.drive


class DriveSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        # Define Talon SRX motor controllers with their CAN IDs
        #phoenix5.WPI_TalonSRX(constants.kLeftMotor1CAN)
        self.left_front_motor = phoenix5.WPI_TalonSRX(17)
        self.left_rear_motor = phoenix5.WPI_TalonSRX(16)
        self.right_front_motor = phoenix5.WPI_TalonSRX(18)
        self.right_rear_motor = phoenix5.WPI_TalonSRX(19)

        # Invert motors if necessary (adjust based on robot wiring)
        self.right_front_motor.setInverted(True)
        self.right_rear_motor.setInverted(True)

        # Create a differential drive for easier control
        self.drive = wpilib.drive.DifferentialDrive(
            wpilib.MotorControllerGroup(self.left_front_motor, self.left_rear_motor),
            wpilib.MotorControllerGroup(self.right_front_motor, self.right_rear_motor),
        )

    #def arcadeDrive(self, drive_subsystem, x_speed, z_rotation):
        #self.drive.arcadeDrive(x_speed, z_rotation)

    # method to drive the robot with joysticks using the differential drive method 'arcadeDrive'
    def arcadeDrive(
        self,
        drive_subsystem,
        xSpeed: lambda xSpeed: xSpeed,
        zRotation: lambda zRotation: zRotation,
        ) -> commands2.Command:
        """
        Drives the robot using arcade drive kinematics.
        :param x_speed: The robot's speed along the X axis (-1.0 to 1.0).
        :param z_rotation: The robot's rotation rate around the Z axis (-1.0 to 1.0).
        """        
        print(f"made it to drive_subsystem arcadeDrive with parameters speed: {xSpeed} and rotation {zRotation}")
        return commands2.cmd.run(
            lambda: self.drive.arcadeDrive(xSpeed(), zRotation()), drive_subsystem,)

    def turn(self, turn_speed):
        turn_output = self.clamp(turn_speed, -0.5, 0.5)  # Clamps the controller output to between -0.5 and 0.5
        self.drive.arcadeDrive(0.0, turn_output)

    def clamp(self, v, minval, maxval):
        # Python doesn't have a builtin clamp function
        return max(min(v, maxval), minval)

    def stop(self):
        """
        Stops the drivetrain motors.
        """
        self.drive.stopMotor()
