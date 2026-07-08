import cv2
import numpy as np

def draw_annotations(image, result):
    """
    Draw clean bounding boxes with object names.
    """

    # Convert PIL image to OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    boxes = result.boxes
    names = result.names

    for box in boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        class_id = int(box.cls[0])
        label = names[class_id]

        # Draw thin green rectangle
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        confidence = float(box.conf[0])
        text = f"{label} {confidence:.0%}"

        # Get text size
        (text_width, text_height), _ = cv2.getTextSize(
            text,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            1
        )

        # Draw green filled rectangle behind the text
        cv2.rectangle(
            img,
            (x1, y1 - text_height - 10),
            (x1 + text_width + 6, y1),
            (0, 255, 0),
            -1
        )

        # Draw white text
        cv2.putText(
            img,
            text,
            (x1 + 3, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
            cv2.LINE_AA
        )

    # Convert back to RGB for Streamlit
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img