import cv2
import matplotlib.pyplot as plt

from ultralytics import YOLO

model = YOLO("yolo11m.pt")

def check_image_loading(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image: {image_path}")
        return None
    else:
        print(f"Image loaded successfully: {image_path}")
        return True

def detect_objects(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found or unable to read: {image_path}")
    results = model(img)
    annotated_frame = results[0].plot()
    plt.imshow(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    print("Hello from sample.py")
    img_path='img/utpal meme 1.jpg'
    if check_image_loading(img_path):
        detect_objects(img_path)