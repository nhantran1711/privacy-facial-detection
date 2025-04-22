import cv2

def draw_bound(img, classifer, scaleFactor, minNeighbor, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert into gray
    features = classifer.detectMultiScale(gray_img, scaleFactor, minNeighbor) # Detect features
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA) # Text on top y - 5
        coords = [x, y, w, h]


    return coords
    
def detect(img, faceCascade, eyeCascade):
    color =  {"blue" : (255, 0, 0),
           "red" : (0, 0, 255),
           "green" : (0, 255, 0)
           }
    coords = draw_bound(img, faceCascade, 1.2 , 14, color["blue"], "Face")

    if len(coords) == 4:
        x, y, w, h = coords
        cropped = img[y:y + h, x:x + w]
        coords = draw_bound(cropped, eyeCascade, 1.1 , 20, color["green"], "Eyes")    
    return img



faceCascade = cv2.CascadeClassifier("./data/raw/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("./data/raw/rawDataEye.xml")

# Error Handling
if faceCascade.empty():
    raise IOError("Failed to load face cascade classifier.")

print(faceCascade)

# Default webcam
video_cam = cv2.VideoCapture(1)

while True:
    _, img = video_cam.read()
    img = detect(img, faceCascade, eyeCascade)
    cv2.imshow("facial detecion", img)

    # Loop breaking
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_cam.release()
cv2.destroyAllWindows()