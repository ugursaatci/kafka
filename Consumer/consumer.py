from kafka import KafkaConsumer
import cv2
import numpy as np

consumer = KafkaConsumer('multiple_camera_topic', bootstrap_servers='localhost:9092')

for message in consumer:
    if message.key == b'camera1':
        camera_id = "Camera 1"
    elif message.key == b'camera2':
        camera_id = "Camera 2"
    else:
        continue

    frame = cv2.imdecode(np.frombuffer(message.value, np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow(camera_id, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
