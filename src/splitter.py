import sys
import os
from PIL import Image


def generate_1d_box_limits(dim, num_divs):
    '''
    Generates the limits of a crop box in a single dimension
    Example, if dim is 512 pixels and num_divs is 5, it should return:
    [(0, 103), (103, 206), (206, 308), (308, 410), (410, 512)]
    '''
    assert dim >= num_divs

    div_size = dim / num_divs
    missing_pixels = dim % num_divs
    boxes = []
    d_0 = 0

    while d_0 < dim:
        d_1 = d_0 + div_size

        if missing_pixels > 0:
            d_1 += 1
            missing_pixels -= 1

        boxes.append((d_0, d_1))
        d_0 = d_1

    return boxes


def split_image(file_path, n_x, n_y, out_folder):
    '''
    Splits the image from file_path into n_x * n_y pieces and saves them inside out_folder
    '''
    os.mkdir(out_folder)
    original = Image.open(file_path)

    original_width, original_height = original.size
    boxes_x = generate_1d_box_limits(original_width, n_x)
    boxes_y = generate_1d_box_limits(original_height, n_y)

    # Merge 1d boxes into 2d boxes
    boxes = []
    for box_y in boxes_y:
        for box_x in boxes_x:
            box = (box_x[0], box_y[0], box_x[1], box_y[1])
            boxes.append(box)

    for box in boxes:
        region = original.crop(box)
        filename = str(box[0]) + '_' + str(box[1]) + '_' + str(box[2]) + '_' + str(box[3]) + '.bmp'
        out_path = os.path.join(out_folder, filename)
        region.save(out_path)


if __name__ == '__main__':
    split_image(sys.argv[1], 5, 5, sys.argv[2])
