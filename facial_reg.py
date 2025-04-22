import cv2

# Default webcam
video_cam = cv2.VideoCapture(0)

while True:
    _, img = video_cam.read()
    cv2.imshow("facial detecion", img)
    # Loop breaking
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_cam.release()
cv2.destroyAllWindows()