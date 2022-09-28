import rclpy
from rclpy.node import Node
from mis_interfaces.srv import SumarDosEnteros


class ClienteSumador(Node):

    def __init__(self):
        super().__init__('ClienteSumador')
        self.cliente = self.create_client(SumarDosEnteros, 'sumar_dos_enteros')
        # Esperamos a que el servicio esté disponible
        while not self.cliente.wait_for_service(timeout_sec=1.0):
            if not rclpy.ok():
                self.get_logger().error('Interruped while waiting for the server.')
                return
            else:
                self.get_logger().info('Server not available, waiting again...')
        self.request = SumarDosEnteros.Request()
    
    def peticion(self, a, b):
        self.request.a = a
        self.request.b = b

        # Llamada asíncrona
        self.futuro = self.cliente.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.futuro)
        return self.futuro.result()


def main(args=None):
    rclpy.init(args=args)
    
    cliente = ClienteSumador()
    resultado = cliente.peticion(20, 43)
    cliente.get_logger().info(f"Resultado de la operación: {resultado.res}")

    cliente.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
