import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, detection_conf=0.7, max_hands=1):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_conf,)
        self.mp_draw = mp.solutions.drawing_utils
        
        
    def find_hands(self,frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BRG2RGB)
        results = self.hands.process(rgb)
        hands_landmarks = []
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                hands_landmarks.append(handLms)
                
        return(frame, hands_landmarks)
    
    
    def get_landmark_position(self, handLms, frame_shape):
        h, w, _ = frame_shape
        points = {}
        for id, lm in enumerate(handLms.landmark):
            points[id] = (int(lm.x * w), int(lm.y * h))
        return points