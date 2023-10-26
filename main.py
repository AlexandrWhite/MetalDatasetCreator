import image_processing as imp
from PIL import Image

import os
import re

grey_data_path = 'data_grey/'
colored_data_path = 'data_colored/'

result_colored_data_path = 'result_colored/'
result_grey_data_path = 'result_grey/'


def img_transform(path):
    """
    здесь будет изменения, которые необходимо
    сделать с изображением независимо окрашено оно или нет
    """
    pred = imp.crop_image(path, debug=True)
    return pred


for file in os.listdir(grey_data_path):
    if re.match(r'(.+)\.jpg', file) is None:
        continue

    only_name = re.match(r'(.+)\.jpg', file).groups()[0]
    result_path = result_grey_data_path + only_name + '.png'

    if os.path.exists(result_path):
        continue

    result = img_transform(grey_data_path+file)
    Image.fromarray(result, 'RGB').save(result_path)


for file in os.listdir(colored_data_path):
    if re.match(r'(.+)\.(jpg|png)', file) is None:
        continue

    only_name = re.match(r'(.+)\.(jpg|png)', file).groups()[0]
    result_path = result_colored_data_path + only_name + '.png'

    if os.path.exists(result_path):
        continue

    result = img_transform(colored_data_path + file)
    imp.make_image(result, result_path)
