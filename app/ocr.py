import re

from PIL import Image
import pytesseract


def get_letters_from_image(path):
    """
    Extract letters from the image by input the path of image
    :param path: the path of the image, such as 'media/image/2020/04/30/01.png'
    :type path: str
    :return: a list of letters which are extracted from the image, such as ['letter1', 'letter2']
    """
    res = list()
    print('path', path)
    letters = pytesseract.image_to_string(Image.open(path))
    if letters:
        res = re.split(r'\s', letters)
    return res
