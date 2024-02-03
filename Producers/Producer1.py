import cv2
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

ip_camera_url_1 = 'rtsp://admin:mayis3794@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1'
cap1 = cv2.VideoCapture(ip_camera_url_1)

while cap1.isOpened():
    ret, frame = cap1.read()
    if not ret:
        break

    ret, buffer = cv2.imencode('.jpg', frame)
    producer.send('multiple_camera_topic', key=b'camera1', value=buffer.tobytes())

    time.sleep(0.02)

cap1.release()
producer.close()
