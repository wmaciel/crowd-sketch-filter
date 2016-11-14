from PIL import Image
import os

def stitch_images(original_path, folder_path, out_path):
    original = Image.open(original_path)

    file_list = os.listdir(folder_path)
    for f in file_list:
        file_name, file_ext = os.path.splitext(f)
        box = tuple(map(int, file_name.split('_')))

        region = Image.open(os.path.join(folder_path, f))
        original.paste(region, box)

    original.save(out_path)


if __name__ == '__main__':
    stitch_images('lena.bmp', 'lena_divs', 'lena_stitched.bmp')
