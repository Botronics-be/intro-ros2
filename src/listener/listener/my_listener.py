import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MyFirstListener(Node):
    def __init__(self):
        super().__init__("my_first_listener")
        self.create_subscription(String, "my_topic", self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Counter message received: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    listener = MyFirstListener()

    rclpy.spin(listener)

    listener.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
