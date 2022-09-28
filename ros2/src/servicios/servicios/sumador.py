import rclpy
from rclpy.node import Node
from mis_interfaces.srv import SumarDosEnteros


class Sumador(Node):

    def __init__(self):
        super().__init__('Sumador')
        self.sumar = self.create_service(SumarDosEnteros, 'sumar_dos_enteros', self.sumar)
    
    def sumar(self, request, response):
        response.res = request.a + request.b
        return response


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(Sumador())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
