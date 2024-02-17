import cv2
import mediapipe as mp
import numpy as np
import math
import os
from keras.models import load_model
import typing
import tensorflow as tf
from imageio import imread


os.makedirs("images", exist_ok=True)


def _normalized_to_pixel_coordinates(
    normalized_x: float, normalized_y: float, image_width: int, image_height: int
) -> typing.Union[None, typing.Tuple[int, int]]:
    """Converts normalized value pair to pixel coordinates."""

    # Checks if the float value is between 0 and 1.
    def is_valid_normalized_value(value: float) -> bool:
        return (value > 0 or math.isclose(0, value)) and (
            value < 1 or math.isclose(1, value)
        )

    if not (
        is_valid_normalized_value(normalized_x)
        and is_valid_normalized_value(normalized_y)
    ):
        return None
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)
    return x_px, y_px


def get_labels():
    return {
        0: "Frustration",
        1: "Confusion",
        2: "Frustration",
        3: "Delight",
        4: "Boredom",
        5: "Engaged",
        6: "Engaged",
    }


Emotion_model = tf.keras.models.load_model("ai/EfficientNet_best_model_final.hdf5")


def predict_sample(image):
    im = np.asarray(image)[None, ...]
    prediction = Emotion_model.predict(im, verbose=0)
    pred_idx = np.argmax(prediction)
    return pred_idx


import matplotlib.pyplot as plt

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


def face_location(image):
    with mp_face_detection.FaceDetection(
        min_detection_confidence=0.5, model_selection=1
    ) as face_detection:
        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        media_results = face_detection.process((image))
        try:
            for detection in media_results.detections:
                det = detection.location_data.relative_bounding_box
            xmin, ymin, w, h = det.xmin, det.ymin, det.width, det.height

            return xmin, ymin, w, h, det
        except:
            return False


def crop_face(image, xmin, ymin, w, h):
    try:
        target_size = (48, 48, 1)
        # yolo_bbox1 = (xmin,ymin,w,h)
        W, H = 1280, 720
        rect_start_point = _normalized_to_pixel_coordinates(xmin, ymin, W, H)

        rect_end_point = _normalized_to_pixel_coordinates(xmin + w, ymin + h, W, H)
        image_arr = image
        if not (rect_start_point is None or rect_end_point is None):

            image_arr = image_arr[
                rect_start_point[1] : rect_end_point[1],
                rect_start_point[0] : rect_end_point[0],
            ]

        image_arr = cv2.resize(image_arr, (target_size[0], target_size[1]))
        image_arr = image_arr.astype(np.uint8)
        # print(rect_start_point[1],rect_end_point[1],rect_start_point[0],rect_end_point[0])

        width_ratio = 640 / 640
        height_ratio = 480 / 480

        left = int(rect_start_point[0] / width_ratio)
        right = int(rect_end_point[0] / width_ratio)
        top = int(rect_start_point[1] / height_ratio)
        bottom = int(rect_end_point[1] / height_ratio)
        # print(top,bottom,left,right)
        return image_arr, left, top, right, bottom
    except:
        return False


def crop_face_emotion(image, xmin, ymin, w, h):
    try:

        target_size = (48, 48, 3)
        # yolo_bbox1 = (xmin,ymin,w,h)
        W, H = 1280, 720
        yolo_bbox1 = (xmin, ymin, w, h)
        W, H = 1280, 720
        rect_start_point = _normalized_to_pixel_coordinates(xmin, ymin, W, H)

        rect_end_point = _normalized_to_pixel_coordinates(xmin + w, ymin + h, W, H)
        image_arr = tf.keras.preprocessing.image.img_to_array(image)
        if not (rect_start_point is None or rect_end_point is None):

            image_arr = image_arr[
                rect_start_point[1] : rect_end_point[1],
                rect_start_point[0] : rect_end_point[0],
            ]

        image_arr = tf.image.resize(image_arr, (target_size[0], target_size[1])).numpy()

        return image_arr
    except:
        return False


def preprocess_input(x, v2=True):
    x = x.astype("float32")
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x


emotion_model_path = "ai/EfficientNet_best_model_final.hdf5"
emotion_classifier = tf.keras.models.load_model(emotion_model_path, compile=False)


class_names = ["Boredom", "Engagement", "Confusion", "Frustration", "Delight"]
# integer_mapping = {i: x for i,x in enumerate(class_names)}
integer_mapping = get_labels()


# def process_image(image, iterator: int) -> str:
def process_image(image) -> str:
    src = imread(image)
    image = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

    if not (face_location(image)):
        return "no face detected"
    bbox_array = np.zeros([720, 1280, 4], dtype=np.uint8)

    xmin, ymin, w, h, _ = face_location(image)
    bbox = [xmin, ymin, h, w]
    if not crop_face(image, xmin, ymin, w, h):
        return "no face detected"
    im, left, top, right, bottom = crop_face(image, xmin, ymin, w, h)
    # emotion_image = crop_face(image,xmin,ymin,w,h)

    gray_image = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    gray_image = preprocess_input(gray_image, True)

    gray_image = np.expand_dims(gray_image, axis=0)

    gray_image = gray_image.reshape(-1, 48, 48, 1)

    # emotion_labels = get_labels()
    emotion_label_arg = np.argmax(emotion_classifier.predict(gray_image, verbose=0))
    emotion = integer_mapping[emotion_label_arg]
    # print('emotion_label_arg',emotion_label_arg)
    colour1 = (255, 255, 255)
    colour2 = (12, 12, 255)

    bbox_array = cv2.rectangle(bbox_array, (left, top), (right, bottom), (colour2), 4)
    bbox_array = cv2.putText(
        bbox_array,
        "{} ".format(emotion),
        (left, top - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (colour1),
        3,
    )

    bbox_array[:, :, 3] = (bbox_array.max(axis=2) > 0).astype(int) * 255

    emotion_string = emotion
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    cv2.putText(
        image,
        "Facial Emotion: " + emotion,
        (445, 495),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 255),
        2,
    )

    # cv2.imwrite(f"./images/image{iterator}.png", image)
    return emotion_string
