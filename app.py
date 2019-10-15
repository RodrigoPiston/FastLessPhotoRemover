import os, os.path
from os import remove
from PIL import  Image, ImageStat
from pathlib import Path

# -- Variables -- #
list_2_delete = []
FOLDER_IMAGES = r"C:\Escritorio Viejo\Primera entrega de programacion\Inmobiliaria\bin\Debug\resources\Maldonado"
EXTENSION     = "jpg"       

# --- Functions -- #
def hash_image(image_path):
    img = Image.open(image_path).resize((8,8), Image.LANCZOS).convert(mode="L")
    mean = ImageStat.Stat(img).mean[0]
    return sum((1 if p > mean else 0) << i for i, p in enumerate(img.getdata()))

# -- Program -- #
list_files = Path(FOLDER_IMAGES).glob('**/*.'+EXTENSION)
for file_a in list_files:
    try:
        list_sub_files = Path(str(os.path.dirname(os.path.abspath(file_a)))).glob('**/*.'+EXTENSION)
        for file_b in list_sub_files :
            if file_a != file_b:
                file_path_a = str(file_a)
                file_path_b = str(file_b)
                hash_a = str(hash_image(file_a))
                hash_b = str(hash_image(file_b))
                if hash_a == hash_b:
                    print("The same:\n")
                    print(" - HASH_A" + str(hash_a) +"\tPath:\t" + str(file_a))
                    print(" - HASH_B" + str(hash_b) +"\tPath:\t" + str(file_b))
                    
                    img_a = Image.open(file_a)
                    img_b = Image.open(file_b)
                    width_a, height_a = img_a.size
                    width_b, height_b = img_b.size 
                    
                    print(" - Width_A:"  + str(width_a)  + "\tWidth_B:"  + str(width_b))
                    print(" - Height_A:" + str(height_a) + "\theight_B:" + str(height_b))
                    
                    if width_a > width_b  and height_a > height_a:
                        list_2_delete.append(file_path_b)
                    elif width_a < width_b and height_a < height_b:
                        list_2_delete.append(file_path_a)
                    elif width_a == width_b and height_a == height_b:
                        list_2_delete.append(file_path_b)
                    elif width_a < width_b and height_a > height_b or width_a > width_b and height_a < height_b :
                        print("¿¿¿")
                        #????
                    else:
                        print("???")
                        #?==?=
                        
                    # 2 mach    
                    list_sub_files = [f for f in list_sub_files if (file_b == f)]

    except  WindowsError as e:
        print("\nError\t"+e.values)


for eliminar in list_2_delete:
    try:
        remove(eliminar)
        print("2 Del:"+eliminar)
    except WindowsError as e:
        print("\nError\t"+e.values)
