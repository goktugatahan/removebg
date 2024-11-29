import os
from rembg import remove
from PIL import Image

input_dir = './images'
output_dir = './images-completed'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):

        input_path = os.path.join(input_dir, filename)
        image = Image.open(input_path)


        output_image = remove(image)


        if output_image.mode == 'RGBA':

            white_bg = Image.new("RGB", output_image.size, (255, 255, 255))

            white_bg.paste(output_image, (0, 0), output_image)
            output_image = white_bg

        output_path = os.path.join(output_dir, filename)


        output_image.save(output_path, format='PNG')

        print(f"Processed {filename}, saved to {output_path}")
