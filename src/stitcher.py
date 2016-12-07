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


def stitch_images_from_object(original_path, object_list, out_dir):
    originals = []

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for i in range(len(object_list[0]['img'])):
        originals.append(Image.open(original_path))

    for o in object_list:
        file_name = o['file']
        for i, img in enumerate(o['img']):
           box = tuple(map(int, file_name.split('_')))
           img = img.resize((box[2] - box[0], box[3] - box[1]), Image.LANCZOS)
           originals[i].paste(img, box)
    
    for i, o in enumerate(originals):
        o.save(os.path.join(out_dir, str(i)+'.jpeg'))

def stitch_images_from_sorted_object(original_path, object_list, num_pics, out_dir):
    originals = []
    
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    
    # hardcode the number of images, as crowdsourcing is not an exact science.... asked for 5, get 6 sometimes...
    for i in range(num_pics):
        originals.append(Image.open(original_path))

    for o in object_list:
        file_name = o['file']
        o['img'].reverse()
        for i in range(num_pics):
            box = tuple(map(int, file_name.split('_')))
            img = o['img'][i].resize((box[2] - box[0], box[3] - box[1]), Image.LANCZOS)
            originals[i].paste(img, box)
    
    for i, o in enumerate(originals):
        o.save(os.path.join(out_dir, str(i)+'.jpeg'))


if __name__ == '__main__':
    stitch_images('lena.bmp', 'lena_divs', 'lena_stitched.bmp')
