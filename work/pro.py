from deepface import DeepFace
import cv2
import sys
import json

def is_sad(image_path, threshold=0.5):
    """
    คืนค่า dict: {"sad_score": float, "is_sad": bool, "all_emotions": {...}}
    threshold = ค่าตัดสินใจ ถ้า score ของ 'sad' >= threshold -> ถือเป็นเศร้า
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # deepface will detect face(s) and return emotion predictions
    result = DeepFace.analyze(img_path = image_path, actions = ['emotion'], enforce_detection = True)
    # DeepFace.analyze returns either a dict for single face or list for multiple faces.
    # Normalize to list
    if isinstance(result, dict):
        faces = [result]
    else:
        faces = result

    outputs = []
    for face in faces:
        emotions = face['emotion']
        sad_score = emotions.get('sad', 0.0) / 100.0 if max(emotions.values()) > 1 else emotions.get('sad',0.0)
        # deepface sometimes gives 0-100; normalize to 0-1 range
        if sad_score > 1:
            sad_score = sad_score / 100.0
        is_sad_flag = sad_score >= threshold
        outputs.append({
            "sad_score": round(float(sad_score),3),
            "is_sad": bool(is_sad_flag),
            "all_emotions": emotions,
            "region": face.get("region", None)
        })
    return outputs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict_sad_deepface.py image.jpg [threshold]")
        sys.exit(1)
    img = sys.argv[1]
    threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    res = is_sad(img, threshold)
    print(json.dumps(res, ensure_ascii=False, indent=2))
