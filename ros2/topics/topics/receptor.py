#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Receptor(Node):
    def __init__(self):
        super().__init__('Receptor')
        self.canal = self.create_subscription(String, "radio", self.procesar_mensaje, 10)

    def procesar_mensaje(self, msg):
        self.get_logger().info(f"Mensaje recibido: {msg.data}")

def main(args=None):
    try:
        rclpy.init(args=args)
        node = Receptor()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
