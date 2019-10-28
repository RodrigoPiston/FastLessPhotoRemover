import os
from PIL import Image, ImageStat
from pathlib import Path

# -- Variables -- #
FOLDER_IMAGES = r"C:\Images"
EXTENSION = "jpg"


# --- Functions -- #
def hash_image(image_path):
    img = Image.open(image_path).resize((8, 8), Image.LANCZOS).convert(mode="L")
    mean = ImageStat.Stat(img).mean[0]
    sum_aux = sum((1 if p > mean else 0) << i for i, p in enumerate(img.getdata()))
    # Quedaba abierta?
    img.close()
    return sum_aux


# -- Program -- #
files = Path(FOLDER_IMAGES).glob('**/*.' + EXTENSION)
final_files = []
files_aux = []
for file in files:
    for file_aux in files_aux:
        if hash_image(file_aux) == hash_image(file):
            continue
        files_aux.append(file)
    if file not in files_aux:
        final_files.append(file)
    else:
        os.remove(Path(file))
