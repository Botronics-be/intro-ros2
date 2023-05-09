from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="zbar_ros",
                executable="barcode_reader",
                name="barcode_reader",
                remappings=[
                    ("image", "/zed2i/zed_node/rgb/image_rect_color"),
                ],
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        os.path.join(
                            get_package_share_directory("zed_wrapper"),
                            "launch",
                            "zed2i.launch.py",
                        )
                    ]
                ),
            ),
            Node(
                package="depthimage_to_laserscan",
                executable="depthimage_to_laserscan_node",
                name="depthimage_to_laserscan_node",
                remappings=[
                    ("depth", "/zed2i/zed_node/depth/depth_registered"),
                    ("depth_camera_info", "/zed2i/zed_node/depth/camera_info"),
                ],
                parameters=[
                    {
                        "output_frame": "zed2i_left_camera_frame",
                    }
                ],
            ),
        ]
    )
