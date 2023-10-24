from PIL import Image
import numpy as np

colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]


def closest(color):
    global colors
    colors = np.array(colors)
    distances = np.sqrt(np.sum((colors - color) ** 2, axis=1))
    index_of_smallest = np.where(distances == np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance


def make_image(arr, result_path):
    # img = Image.open(orig_path).convert('RGB')
    # img = np.array(img)

    img = arr

    h, w, k = img.shape

    result = np.empty((h, w, 3), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            close = closest(img[i, j])[0]
            result[i, j] = close

    result_image = Image.fromarray(result, 'RGB')
    result_image.save(result_path)


def crop_image(orig_path, debug=False):
    if debug:
        print(orig_path)
    img = Image.open(orig_path).convert('RGB')
    img = np.array(img)
    h, w, k = img.shape

    result = np.empty((h - 200, w, 3), dtype=np.uint8)

    for i in range(h - 200):
        for j in range(w):
            result[i, j] = img[i, j]

    return result


