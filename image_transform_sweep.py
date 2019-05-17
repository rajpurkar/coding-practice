from __future__ import print_function
from PIL import Image, ImageEnhance
import numpy as np
from pathlib import Path
import os


def img_transform(img, enhancement_class, factor):
    """
    Transform an image with an enhancement.

    Args:
        img (PIL Image): Input image.
        enhancement_class (ImageEnhance Class): Enhancement to use.
        factor (float): Controlling the enhancement.
                        Factor 1.0 always returns a copy of
                        the original image.

    Returns:
        new_img (PIL Image): Output image.
    """
    new_img = enhancement_class(img)
    new_img = new_img.enhance(factor)
    return new_img


def img_transform_sweep(img, img_path, transform_str, num_images_to_sweep,
        verbose=0, dry=0):
    """
    Sweep over a bunch of transformations to an image.

    Args:
        img (PIL image): Input image.
        img_path (pathlib.Path object): Path to the image.
        transform_str (String): Transformation mapping to ImageEnhance class name.
                                Options are Color, Contrast, Brightness, Sharpness
        num_images_to_sweep (int): Number of images to output.
        verbose (bool): Whether to print progress (verbose=1) or not (verbose=0).
        dry (bool): If true, don't write new images to file

    Returns:
        new_imgs (list of PIL images)
    """
    if transform_str == 'Brightness':
        smallest_factor = 0.75
        largest_factor = 1.5
    elif transform_str == 'Contrast':
        smallest_factor = 0.5
        largest_factor = 2
    elif transform_str == 'Sharpness':
        smallest_factor = 0.125
        largest_factor = 2
    else:
        raise ValueError("Transformation not defined")
    factors = list(np.linspace(smallest_factor, largest_factor,
                   num_images_to_sweep-1)) + [1.0]
    factors.sort()
    for factor in factors:
        enhancement_class = getattr(ImageEnhance, transform_str)
        new_img = img_transform(img, enhancement_class, factor)
        new_name = img_path.resolve().stem + "_" + transform_str + "_" + str(factor)
        new_path = img_path.parent / (new_name + img_path.suffix)
        if not dry:
            new_img.save(str(new_path))
        if verbose:
            print("Saved" + str(new_path))


if __name__ == "__main__":
    path_str = "/Users/pranavrajpurkar/Desktop/sample.jpg"
    img_path = Path(path_str).absolute()
    img = Image.open(str(img_path))
    transform_strs = ['Contrast', 'Brightness', 'Sharpness']
    num_images_to_sweep = 10
    for transform_str in transform_strs:
        img_transform_sweep(img, img_path, transform_str, num_images_to_sweep,
                verbose=1, dry=0)
