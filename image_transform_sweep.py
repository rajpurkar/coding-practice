from PIL import Image, ImageEnhance
import numpy as np
from pathlib import Path
import os

def img_contrast_change(img, factor):
    new_img = ImageEnhance.Contrast(img)
    new_img = new_img.enhance(factor)
    return new_img

def img_transform_sweep(img, transform_fn_str, img_path):
    """

    Args:
        img (PIL img)
        transform_fn_str (String): "Contrast" or "Brightness"
        img_path (pathlib.Path object)
    """
    for factor in range(10):
        new_img = img_contrast_change(img, factor)
        new_name = img_path.resolve().stem + "_" + transform_fn_str + "_" + str(factor)
        new_path = img_path.parent / (new_name + img_path.suffix)
        new_img.save(str(new_path))

if __name__ == "__main__":
    path_str = "/Users/pranavrajpurkar/Desktop/sample.jpg"
    img_path = Path(path_str).absolute()
    img = Image.open(str(img_path))
    transform_fn_str = 'contrast'
    img_transform_sweep(img, transform_fn_str, img_path)
