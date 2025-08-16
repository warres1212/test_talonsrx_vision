import commands2

from subsystems.drive_subsystem import DriveSubsystem

# Example autonomous commands which drive forwards for 1 second.


class Autos(commands2.Command):
    def __init__(self) -> None:
        pass

    def exampleAuto(drive_subsystem: DriveSubsystem) -> commands2.Command:
        return commands2.cmd.run(
            lambda: drive_subsystem.arcadeDrive(0.5, 0.0) # drive straight at 50% power
        ).withTimeout(1.0) # drive for 1.0 seconds