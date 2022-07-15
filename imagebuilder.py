"""
Модуль реализующий удаление вотермарки на png изображении
"""
from PIL import ImageDraw


def imagereader(image):
    """ Функция определяющая цвет фона и выполняющая imageconverter """

    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    reds = pix[0, 0][0]
    greens = pix[0, 0][1]
    blues = pix[0, 0][2]
    draw = ImageDraw.Draw(image)
    if reds == blues and blues == greens and greens == 233:
        imageconverter(draw, width, height, pix, True)
    elif reds == blues and blues == greens and greens == 255:
        imageconverter(draw, width, height, pix, False)


def imageconverter(draw, width, height, pix, mode):
    """
    Функция перерисовывующая пиксели вотермарки в цвет фона и сохраняющая получившийся picture
    """

    if mode:
        for i in range(width):
            for j in range(height):
                redn = pix[i, j][0]
                greenn = pix[i, j][1]
                bluen = pix[i, j][2]
                if redn > 233 and greenn > 233 and bluen > 233:
                    draw.point((i, j), (233, 233, 233))
    else:
        for i in range(width):
            for j in range(height):
                redn = pix[i, j][0]
                greenn = pix[i, j][1]
                bluen = pix[i, j][2]
                if bollean(redn, 235, 255) and bollean(greenn, 235, 255) and bollean(bluen, 235, 255):
                    draw.point((i, j), (255, 255, 255))


def bollean(pixel, start, end):
    """ Функция перекрашивающая заданные пиксели вотермарки """

    return bool(pixel >= start and pixel != end)
