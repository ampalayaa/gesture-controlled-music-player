import cv2
from hand_tracker import HandTracker
from volume_controller import VolumeController
from utils import calculate_distance


tracker = HandTracker()
volume = VolumeController()

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame, hands  = tracker.find_hands(frame)
    
    if hands:
        landmarks = tracker.get_landmark_positions(hands[0], frame.shape)
        if 4 in landmarks and 0 in landmarks:
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            cv2.line(frame, thumb_tip, index_tip, (0, 255, 0), 2)
            lenght = calculate_distance(thumb_tip, index_tip)
            vol = volume.set_volume_by_distance(lenght)
            cv2.putText(frame, f'Volume: {int(vol)} dB', (10, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            cv2.imshow("Gesture Volume Contol", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
cap.release()
cv2.destroyAllWindows()