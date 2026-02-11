from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    agent_a = Node(
        package='micro_ros_agent',
        executable='micro_ros_agent',
        name='micro_ros_agent_a',
        output='screen',
        arguments=[
            'serial',
            '--dev', '/dev/serial/by-path/pci-0000:00:14.0-usb-0:6.1:1.0-port0',
            '-b', '115200'
        ]
    )

    agent_b = Node(
        package='micro_ros_agent',
        executable='micro_ros_agent',
        name='micro_ros_agent_b',
        output='screen',
        arguments=[
            'serial',
            '--dev', '/dev/serial/by-path/pci-0000:00:14.0-usb-0:6.2:1.0-port0',
            '-b', '921600'
        ]
    )

    return LaunchDescription([
        agent_a,
        agent_b
    ])

