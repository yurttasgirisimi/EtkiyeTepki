import os
import json

image_folder = "arsiv"

image_extensions = (".jpg", ".jpeg", ".png", ".gif")

image_files = [
    f"arsiv/{filename}"
    for filename in os.listdir(image_folder)
    if filename.lower().endswith(image_extensions)
]

data = {"gorseller": image_files}

with open("gorseller.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)

print("gorseller.json üretildi!")