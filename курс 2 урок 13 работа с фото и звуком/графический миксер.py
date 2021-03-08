def twist_image(input_file_name, output_file_name):
    from PIL import Image, ImageChops
    im = Image.open(input_file_name)
    x, _ = im.size
    im = ImageChops.offset(im, x // 2, 0)
    im.save(output_file_name)
