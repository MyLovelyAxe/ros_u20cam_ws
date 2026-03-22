import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    rviz_config_file = os.path.join(
        get_package_share_directory("u20cam_720p"),
        "config",
        "verbose_rviz_config.rviz",
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    camera_node = Node(
        package='u20cam_720p',
        executable='camera_node',
        name='camera_node',
    )
    
    return LaunchDescription([
        rviz_node,
        camera_node,
    ])