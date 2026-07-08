from ultralytics import YOLO

model = YOLO("models/yolov8s.pt")

def detect_objects(image, confidence):
    results = model.predict(
        image,
        conf=confidence,
        iou=0.45
    )
    return results