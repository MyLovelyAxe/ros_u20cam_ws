import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from .camera import U20Camera
from .constants import CALIB_PARAM_JSON

class U20CAMLiveStreamImagePublisher(Node):
    def __init__(self):
        super().__init__('u20cam_live_stream_image_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera/undistorted_image', 10)
        self.timer = self.create_timer(0.05, self.timer_callback)  # 20Hz
        self.u20cam = U20Camera.create_from_json(CALIB_PARAM_JSON)
        self.bridge = CvBridge()
        self.count = 0

        if not self.u20cam.camera_connected:
            self.get_logger().error('Could not open u20cam.')
            rclpy.shutdown()
        else:
            self.get_logger().info('u20cam opened successfully.')


    def timer_callback(self):
        
        frame = self.u20cam.get_frame()
        if frame is None:
            self.get_logger().warning("No frame is returned")
            return
        else:
            if self.count % 100 == 0:
                self.get_logger().info(f"The {self.count}th frame shape: {frame.shape}")

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # ori_square_img = cvt_raw_image_squre(raw_image=rgb_frame)
        img_msg = self.bridge.cv2_to_imgmsg(rgb_frame, encoding='rgb8')
        self.publisher_.publish(img_msg)
        self.count += 1


    def destroy_node(self):

        self.u20cam.release_capture()
        super().destroy_node()



def main(args=None):

    rclpy.init(args=args)
    node = U20CAMLiveStreamImagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()
