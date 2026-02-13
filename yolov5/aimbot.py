import cv2
import numpy as np
import mss
import pyautogui
import torch
import keyboard
from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes
from utils.augmentations import letterbox

# Load YOLOv5 model
model = DetectMultiBackend('runs/train/exp9/weights/best.pt', device='cpu')
stride = model.stride
names = model.names

# Screen capture setup
sct = mss.mss()
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}  # Adjust to your screen resolution
screen_width, screen_height = monitor["width"], monitor["height"]
aimbot_active = False

# Mouse settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

def process_frame(frame):
    # Preprocess frame for YOLOv5
    img = letterbox(frame, 320, stride=stride, auto=True)[0]
    img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to('cpu').float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    pred = model(img, augment=False, visualize=False)
    pred = non_max_suppression(pred, conf_thres=0.1, iou_thres=0.4, classes=None, max_det=1)

    # Process detections
    for det in pred:
        if len(det):
            det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], frame.shape).round()
            for *xyxy, conf, cls in det:
                x1, y1, x2, y2 = map(int, xyxy)
                label = f'{names[int(cls)]} {conf:.2f}'
                print(f"Detected enemy at: ({x1}, {y1}, {x2}, {y2}) with confidence {conf:.2f}")
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Aim at head (top of box)
                if aimbot_active:
                    head_x = (x1 + x2) // 2
                    head_y = y1 + (y2 - y1) // 4  # Aim 1/4 down from top
                    screen_x = head_x + monitor["left"]
                    screen_y = head_y + monitor["top"]
                    print(f"Moving mouse to: ({screen_x}, {screen_y})")
                    pyautogui.moveTo(screen_x, screen_y)
    return frame

# Mouse click callback for fallback toggle
def toggle_aimbot(event, x, y, flags, param):
    global aimbot_active
    if event == cv2.EVENT_LBUTTONDOWN:
        aimbot_active = not aimbot_active
        print(f"Aimbot {'ON' if aimbot_active else 'OFF'} (Mouse Toggle)")

# Set up OpenCV window and mouse callback
cv2.namedWindow("Aimbot")
cv2.setMouseCallback("Aimbot", toggle_aimbot)

print("Aimbot started. Press 'f1' to toggle (or click the window), 'q' to quit.")
print("Run Valorant in windowed mode (1920x1080) for best results.")
while True:
    # Capture screen
    frame = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

    # Process frame
    frame = process_frame(frame)

    # Display frame
    cv2.imshow("Aimbot", frame)

    # Controls using keyboard library
    if keyboard.is_pressed('q'):
        print("Quitting...")
        break
    if keyboard.is_pressed('f1'):
        aimbot_active = not aimbot_active
        print(f"Aimbot {'ON' if aimbot_active else 'OFF'} (Key Toggle)")
        while keyboard.is_pressed('f1'):
            pass

    # OpenCV waitKey (minimal delay)
    cv2.waitKey(1)

cv2.destroyAllWindows()
sct.close()