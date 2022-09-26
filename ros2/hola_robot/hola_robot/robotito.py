#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Robotito(Node):
    def __init__(self):
        super().__init__('Robotito')
        self.i = 0
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.i += 1
        self.get_logger().info(f'🤖 {self.i}')

def main(args=None):
    try:
        rclpy.init(args=args)
        node = Robotito()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
