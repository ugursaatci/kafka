import cv2
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

ip_camera_url_2 = 'rtsp://username:password@IP_ADDRESS_2:PORT/stream_path'
cap2 = cv2.VideoCapture(0)

while cap2.isOpened():
    ret, frame = cap2.read()
    if not ret:
        break

    ret, buffer = cv2.imencode('.jpg', frame)
    producer.send('multiple_camera_topic', key=b'camera2', value=buffer.tobytes())

    time.sleep(0.02)

cap2.release()
producer.close()
