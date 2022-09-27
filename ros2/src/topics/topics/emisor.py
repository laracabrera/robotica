#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Emisor(Node):
    def __init__(self):
        super().__init__('Emisor')
        self.publisher = self.create_publisher(String, "radio", 10)
        self.timer = self.create_timer(0.5, self.emitir_mensaje)
        self.get_logger().info("Radio station launch!")

    def emitir_mensaje(self):
        msg = String()
        msg.data = "Probando, probando..."
        self.publisher.publish(msg)

def main(args=None):
    try:
        rclpy.init(args=args)
        node = Emisor()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
