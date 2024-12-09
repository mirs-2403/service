import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class ExampleServiceServer(Node):
    def __init__(self):
        super().__init__('example_service_server')
        self.srv = self.create_service(SetBool, '/example_service', self.handle_request)

    def handle_request(self, request, response):
        if request.data:
            response.success = True
            response.message = "Success: Received TRUE!"
        else:
            response.success = False
            response.message = "Failure: Received FALSE!"
        self.get_logger().info(f"Request: {request.data}, Response: {response.message}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ExampleServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
