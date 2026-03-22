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

    raw_img_pub_node = Node(
        package='u20cam_720p',
        executable='raw_img_pub',
        name='raw_img_pub',
    )
    
    return LaunchDescription([
        rviz_node,
        raw_img_pub_node,
    ])