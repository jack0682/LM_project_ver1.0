import rclpy
from rclpy.node import Node

class MainNode(Node):
    def __init__(self):
        super().__init__('main_node')
        self.get_logger().info('🚀 LM Core Main Node is running!')

def main(args=None):
    rclpy.init(args=args)
    node = MainNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
