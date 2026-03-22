from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():


    comp_img_pub_node = Node(
        package='u20cam_720p',
        executable='comp_img_pub',
        name='comp_img_pub',
    )
    
    return LaunchDescription([
        comp_img_pub_node,
    ])