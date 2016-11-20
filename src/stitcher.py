import os
from PIL import Image

def stitch_images(original_path, folder_path, out_path):
    '''
    Stitches images back into its original locations
    Uses the image at original_path as a backdrop
    Pastes the image pieces from folder_path
    Saves the new image into out_path
    '''
    original = Image.open(original_path)

    file_list = os.listdir(folder_path)
    for file_path in file_list:
        file_name = os.path.splitext(file_path)[0]
        box = tuple(map(int, file_name.split('_')))

        region = Image.open(os.path.join(folder_path, file_path))
        original.paste(region, box)

    original.save(out_path)


if __name__ == '__main__':
    stitch_images('lena.bmp', 'lena_divs', 'lena_stitched.bmp')
