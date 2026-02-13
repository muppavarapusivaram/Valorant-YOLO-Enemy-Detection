from datasets import load_from_disk
import os

data_path = r"C:\Users\SIVA RAM\PycharmProjects\PythonProject\ValorantAimbot\valorant_data"
output_path = r"C:\Users\SIVA RAM\PycharmProjects\PythonProject\ValorantAimbot\yolov5\small_data"
os.makedirs(os.path.join(output_path, "images"), exist_ok=True)
os.makedirs(os.path.join(output_path, "labels"), exist_ok=True)

ds = load_from_disk(data_path)

def convert_bbox_coco_to_yolo(img_width, img_height, bbox):
    x, y, w, h = bbox
    x_center = (x + w / 2) / img_width
    y_center = (y + h / 2) / img_height
    width = w / img_width
    height = h / img_height
    return x_center, y_center, width, height

count = 0
for i, item in enumerate(ds):
    if count >= 200: break
    objects = item["objects"]
    if 1 in objects["category"]:  # Enemy only
        img = item["image"]
        img_width = item["width"]
        img_height = item["height"]
        img_path = os.path.join(output_path, "images", f"img_{count}.jpg")
        img.save(img_path)

        label_path = os.path.join(output_path, "labels", f"img_{count}.txt")
        with open(label_path, "w") as f:
            for j, cat in enumerate(objects["category"]):
                if cat == 1:
                    bbox = objects["bbox"][j]
                    x_center, y_center, w, h = convert_bbox_coco_to_yolo(img_width, img_height, bbox)
                    f.write(f"0 {x_center} {y_center} {w} {h}\n")
        count += 1

print(f"Saved {count} enemy images to", output_path)