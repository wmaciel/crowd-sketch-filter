import os
from PIL import Image

def blend_images_from_folder(folder_path, output_path):
    file_list = os.listdir(folder_path)
    path_list = map(lambda fn: os.path.join(folder_path, fn), file_list)
    img_list = map(lambda fp: Image.open(fp, 'r'), path_list)
    blended_img = blend_images(img_list)
    blended_img.save(output_path)

def blend_images(img_list):
    n = len(img_list)
    if n == 0:
        return None
    
    blended_img = img_list[0].copy()
    for i, img in enumerate(img_list):
        alpha = 1.0 - float(i) / float(i+1)
        print alpha
        blended_img = Image.blend(blended_img, img, alpha)
    
    return blended_img
    

if __name__ == '__main__':
    import sys
    blend_images_from_folder(sys.argv[1], sys.argv[2])