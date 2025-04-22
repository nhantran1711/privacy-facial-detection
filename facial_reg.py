import cv2

def draw_bound(img, classifer, scaleFactor, minNeighbor, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert into gray
    features = classifer.detectMultiScale(gray_img, scaleFactor, minNeighbor) # Detect features
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA) # Text on top y - 5
        coords = [x, y, w, h]

    return coords, img
    
def detect(img, faceCassade):
    color =  {"blue" : (255, 0, 0),
           "red" : (0, 0, 255),
           "green" : (0, 255, 0)
           }
    coords, img = draw_bound(img, faceCassade, 1.2 , 12, color["blue"], "Face")
    return img

faceCassade = cv2.CascadeClassifier("./data/raw/haarcascade_frontalface_default.xml")
print(faceCassade)

# Default webcam
video_cam = cv2.VideoCapture(0)

while True:
    _, img = video_cam.read()
    img = detect(img, faceCassade)
    cv2.imshow("facial detecion", img)

    # Loop breaking
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_cam.release()
cv2.destroyAllWindows()