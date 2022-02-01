import picamera
print("Say Cheese")
with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.capture('..Pictures/Cam_Test1.jpg')
print("Click")
