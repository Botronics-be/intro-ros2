import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MyFirstTalker(Node):
    def __init__(self):
        super().__init__("my_first_talker")
        self.publisher_ = self.create_publisher(String, "my_topic", 5)
        self.timer = self.create_timer(0.2, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Counter value is : {self.counter}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    talker = MyFirstTalker()

    rclpy.spin(talker)

    # (Optional) Destroy the node explicitly
    talker.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
