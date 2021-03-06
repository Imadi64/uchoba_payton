from PIL import Image, ImageFilter
import numpy as np


def bw_convert():  # делает фото черно-бедым
    img = Image.open('image.jpg')
    image = np.asarray(img)
    # узнаем размерность массива
    x, y, _ = image.shape
    k = np.array([0.2989, 0.587, 0.114])
    arr = np.round(np.sum(image * k, axis=2)).astype(np.uint8).reshape((x, y))
    image2 = Image.fromarray(arr)
    image2.save('res.jpg')


def negative(source, res):  # делает фото в негативе
    source = Image.open(source)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    result.save(res, "JPEG")


def image_filter(pixels, i, j):  # Заменяет цвет исходного пикселя на средний, относительно его окружения
    r, g, b = 0, 0, 0
    for row in range(11):
        for col in range(11):
            if row != i or col != j:
                r += pixels[row, col][0]
                g += pixels[row, col][1]
                b += pixels[row, col][2]
    return int(r / 120), int(g / 120), int(b / 120)


def transparency(file1, file2):  # позволяет наложить одно фото на другое сделав первое полу прозрачным
    im1 = Image.open(file1)
    im2 = Image.open(file2)
    x, y = im1.size
    pix1 = im1.load()
    pix2 = im2.load()
    for i in range(x):
        for j in range(y):
            r1, g1, b1 = pix1[i, j]
            r2, g2, b2 = pix2[i, j]
            r = int(0.5 * r1 + 0.5 * r2)
            g = int(0.5 * g1 + 0.5 * g2)
            b = int(0.5 * b1 + 0.5 * b2)
            pix1[i, j] = r, g, b
    im1.save('res.jpg')


def razmitie(n):  # делает ВСЕ фото размытым
    im = Image.open("image.jpg")
    im = im.filter(ImageFilter.GaussianBlur(radius=n))
    im.save('res.jpg')