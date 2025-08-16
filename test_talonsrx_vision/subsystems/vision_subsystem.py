import wpilib
import wpimath.geometry
import commands2
from photonlibpy import PhotonCamera, PhotonPoseEstimator, PoseStrategy
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout
from wpimath.geometry import Transform3d, Pose3d
from wpilib import SmartDashboard
from commands2 import Subsystem

kRobotToCam = wpimath.geometry.Transform3d(
    wpimath.geometry.Translation3d(0.0, 0.0, 0.0),  #0.5, 0.0, 0.5),
    wpimath.geometry.Rotation3d.fromDegrees(0.0, 0.0, 0.0)  #0.0, -30.0, 0.0),
)

class VisionSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        # Replace 'your_camera_name' with the actual name of your PhotonVision camera
        self.camera = PhotonCamera("leftcamera") #

        # Transform from the robot's origin to the camera's position
        # Replace these values with your robot's specific camera mounting
        self.robot_to_camera_transform = kRobotToCam

        # Create a PhotonPoseEstimator to estimate robot pose from AprilTags
        # Replace AprilTagFieldLayout with your specific field layout
        # (e.g., load from a JSON file)
        self.field_layout = None  # You would load this from a JSON or define it manually
        self.photon_pose_estimator = PhotonPoseEstimator(
            self.field_layout,
            PoseStrategy.MULTI_TAG_PNP_ON_COPROCESSOR, # Recommended strategy
            self.camera,
            self.robot_to_camera_transform
        )

        self.camPoseEst = PhotonPoseEstimator(
            AprilTagFieldLayout.loadField(AprilTagField.kDefaultField),
            PoseStrategy.LOWEST_AMBIGUITY,
            self.camera,
            kRobotToCam,
        )

    def get_latest_result(self):
        return self.camera.getLatestResult()

    def get_estimated_robot_pose(self):
        return self.photon_pose_estimator.update()

    def get_target_yaw(self, april_tag_id: int):
        result = self.get_latest_result()
        if result.hasTargets():
            for target in result.getTargets():
                if target.getFiducialId() == april_tag_id:
                    # Yaw is reported CW-positive, convert to CCW-positive if needed
                    # depending on your drivetrain's convention
                    return target.getYaw()
        return None

    def periodic(self):
        # Update any vision-related information on SmartDashboard
        #print("made it to VisionSubsystem periodic")
        latest_result = self.get_latest_result()
        SmartDashboard.putBoolean("Has AprilTag Target", latest_result.hasTargets())
        """
        results = self.camera.getAllUnreadResults()
        if len(results) > 0:
            result = results[-1]  # take the most recent result the camera had
            for target in result.getTargets():
                if target.getFiducialId() == 7:
                    # Found tag 7, record its information
                    targetVisible = True
                    targetYaw = target.getYaw()
        """
        
        # Optionally, display the estimated robot pose
        estimated_pose = self.get_estimated_robot_pose()
        if estimated_pose:
            SmartDashboard.putNumberArray("Estimated Pose", [
                estimated_pose.estimatedPose.x, estimated_pose.estimatedPose.y, estimated_pose.estimatedPose.rotation().angle_degrees()
            ])