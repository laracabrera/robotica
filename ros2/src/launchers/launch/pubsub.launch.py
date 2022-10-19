from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(Node(
        package='topics', 
        executable='emisor',
        name='NodoEmisor',
        remappings=[
            ('radio', 'nueva_radio')
        ]))
    ld.add_action(Node(
        package='topics', 
        executable='receptor',
        name='NuevoReceptor',
        remappings=[
            ('radio', 'nueva_radio')
        ]))

    return ld
