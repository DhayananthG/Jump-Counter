import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence = 0.5,min_tracking_confidence = 0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        
        image = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(image,results.face_landmarks,mp_holistic.FACE_CONNECTIONS)

        cv2.imshow("Holistic Model Detection", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cap.destroyAllWindows()