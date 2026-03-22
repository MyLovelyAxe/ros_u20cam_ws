import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Header
from cv_bridge import CvBridge
import cv2
from .camera import U20Camera
from .constants import CALIB_PARAM_JSON

class U20CAMLiveStreamImagePublisher(Node):
    def __init__(self):

        super().__init__('u20cam_live_stream_image_publisher')

        # Setup publisher for sending compressed images from camera
        self.publisher_ = self.create_publisher(
            CompressedImage,
            "/camera/image_raw/compressed",
            10,
        )
        self.timer = self.create_timer(0.05, self.timer_callback)  # 20Hz
        self.u20cam = U20Camera.create_from_json(CALIB_PARAM_JSON)
        self.bridge = CvBridge()
        self.count = 0
        self.jpeg_quality = 95 # for compressed image

        # Confirm if the camera is opened correctly
        if not self.u20cam.camera_connected:
            self.get_logger().error('Could not open u20cam.')
            rclpy.shutdown()
        else:
            self.get_logger().info('u20cam opened successfully.')


    def timer_callback(self):
        
        cv2_bgr_frame = self.u20cam.get_frame()
        if cv2_bgr_frame is None:
            self.get_logger().warning("No frame is returned")
            return
        else:
            if self.count % 100 == 0:
                self.get_logger().info(f"The {self.count}th frame shape: {cv2_bgr_frame.shape}")

        # Encode to JPEG
        ok, buf = cv2.imencode(
            ext=".jpg", 
            img=cv2_bgr_frame,
            params=[int(cv2.IMWRITE_JPEG_QUALITY), self.jpeg_quality],
        )
        if not ok:
            self.get_logger().warn("Failed to encode image")
            return
        
        comp = CompressedImage()
        comp.header = Header()
        comp.header.stamp = self.get_clock().now().to_msg()
        comp.header.frame_id = "u20cam_comp_img_frame"
        comp.format = "jpeg"
        comp.data = buf.tobytes()
        self.publisher_.publish(comp)
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
