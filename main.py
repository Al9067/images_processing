from PIL import Image
import os

IMG_DIR = 'PATH_TO_FOLDER/Photos'
NEW_SIZE = (1200, 1600)
IMG_RESIZED_DIR = 'PATH_TO_FOLDER/Photos_resized'
IMG_BG_DIR = 'PATH_TO_FOLDER/Images_bg'

os.listdir(IMG_DIR)
if not os.path.exists(IMG_RESIZED_DIR) or not os.path.exists(IMG_BG_DIR):
    os.makedirs(IMG_RESIZED_DIR)
    os.makedirs(IMG_BG_DIR)

for file in os.listdir(IMG_DIR):
    image = Image.open(f'{IMG_DIR}/{file}')
    img_w, img_h = image.size
    background = Image.new('RGB', (2000, 3000), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = (int((bg_w - img_w)/2), int((bg_h - img_h)/2))
    background.paste(image, offset)
    background.save(f'{IMG_BG_DIR}/bg_{file}')
    image_to_resize = Image.open(f'{IMG_BG_DIR}/bg_{file}')
    image_resized = image_to_resize.resize(NEW_SIZE, Image.Resampling.LANCZOS)
    image_resized.save(f'{IMG_RESIZED_DIR }/{file}')


