from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD',
            snow_color='#FFFAFA', trunk_color='#A45A52',
            needls_color='#01796F', sun_color='#FFDB00'):
    im = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(im)

    draw.rectangle(((0, int(height * 0.8)), (width, height)),
                   snow_color)

    draw.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)

    draw.rectangle(((int(0.45 * width), int(height * 0.7)),
                    (int(0.55 * width), int(height * 0.9))),
                   trunk_color)

    draw.polygon(((int(0.50 * width), int(height * 0.10)),
                  (int(0.60 * width), int(height * 0.30)),
                  (int(0.55 * width), int(height * 0.30)),
                  (int(0.65 * width), int(height * 0.50)),
                  (int(0.60 * width), int(height * 0.50)),
                  (int(0.70 * width), int(height * 0.70)),
                  (int(0.30 * width), int(height * 0.70)),
                  (int(0.40 * width), int(height * 0.50)),
                  (int(0.35 * width), int(height * 0.50)),
                  (int(0.45 * width), int(height * 0.30)),
                  (int(0.40 * width), int(height * 0.30))),
                 needls_color)
    im.save(file_name)