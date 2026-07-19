import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize hand detector
detector = HandDetector(detectionCon=0.5, maxHands=1)

def is_peace(fingers):
    """
    Detect peace sign (V sign)
    fingers list: [thumb, index, middle, ring, pinky]
    1 = up, 0 = down
    """
    # Peace sign: index and middle finger up, others down
    if fingers[1] == 1 and fingers[2] == 1:  # index and middle up
        if fingers[3] == 0 and fingers[4] == 0:  # ring and pinky down
            return True
    return False

# Open camera
cap = cv2.VideoCapture(0)

print("Program berjalan! Tunjukkan gesture peace (✌️) untuk blur")
print("Tekan ESC untuk keluar")

while True:
    success, frame = cap.read()
    
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    
    peace_detected = False
    
    try:
        # Find hands (draw=False untuk tidak ada garis-garis)
        hands, img = detector.findHands(frame, draw=False)
        
        if hands:
            hand = hands[0]  # Get first hand
            fingers = detector.fingersUp(hand)
            
            if is_peace(fingers):
                peace_detected = True
        
        # Apply blur effect if peace sign detected
        if peace_detected:
            img = cv2.GaussianBlur(img, (61, 61), 0)
        
        cv2.imshow("Peace Blur", img)
        
    except Exception as e:
        # If there's an error, just show the frame without processing
        cv2.imshow("Peace Blur", frame)
    
    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("Program selesai!")
