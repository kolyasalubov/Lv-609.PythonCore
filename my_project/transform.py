from image import Image
import numpy as np


def brighten(image, factor):

    x_pixels, y_pixels, num_channels = image.array.shape

    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels,
                   num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = image.array[x, y, c] * factor

    return new_im


def adjust_contrast(image, factor, mid):

    x_pixels, y_pixels, num_channels = image.array.shape

    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels,
                   num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (
                    image.array[x, y, c] - mid) * factor + mid

    # or:
    new_im.array = image.array * factor

    return new_im


def blur(image, kernel_size):

    x_pixels, y_pixels, num_channels = image.array.shape

    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels,
                   num_channels=num_channels)

    neighbor_range = kernel_size // 2
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):

                total = 0
                for x_i in range(max(0, x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1):
                    for y_i in range(max(0, y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size ** 2)
    return new_im


if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # brightening
    # brightened_im = brighten(lake, 1.7)
    # brightened_im.write_image('brightened.png')

    # # darkening
    # darkened_im = brighten(lake, 0.3)
    # darkened_im.write_image('darkened.png')

    # # # increase contrast
    # incr_contrast = adjust_contrast(lake, 2, 0.5)
    # incr_contrast.write_image('increased_contrast.png')

    # # decrease contrast
    # decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    # decr_contrast.write_image('decreased_contrast.png')

    # blur using kernel 3
    # blur_3 = blur(city, 3)
    # blur_3.write_image('blur_k3.png')

    # # blur using kernel size of 15
    # blur_15 = blur(city, 15)
    # blur_15.write_image('blur_k15.png')
