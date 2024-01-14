import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=True)
    
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3
        f = 668
        d = (W * f) / w
        cvzone.putTextRect(img, f'Distance from camera: ~{int(d)}cm', (face[10][1]-75, face[10][1]-50), scale=2)
    
    cv2.imshow("image", img)
    
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):  # 27 is the ASCII code for the Escape key
        break

cap.release()
cv2.destroyAllWindows()
