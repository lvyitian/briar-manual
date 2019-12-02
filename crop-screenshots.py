#!/usr/bin/env python3

import os

from PIL import Image

IMAGE_PATH = "static/img"
POSTFIX = '-cropped'


def main():
    crop('add-contact-options.png', 93, 65)
    crop('add-contact-pending.png', 22, 4)
    crop('manual_messaging.png', 50)
    crop('introduction-5.png', 77, 47)
    crop('manage-rss-feeds-2.png', 35)
    crop('manual_dark_theme_settings.png', 45)
    crop('manual_dark_theme_nav_drawer.png', 64)
    crop('manual_tor_settings.png', 65, 15)
    crop('manual_app_lock.png', 65, 18)
    crop('manual_app_lock_nav_drawer.png', 75)


def crop(file_name, bottom, top_offset=0, only_show=False):
    file_path = os.path.join(IMAGE_PATH, file_name)
    if not os.path.isfile(file_path):
        print("Warning: File not found %s" % file_path)
        return

    with Image.open(file_path) as image:
        left_c = 0
        top_c = image.size[1] * top_offset / 100
        right_c = image.size[0]
        bottom_c = image.size[1] * bottom / 100
        image_cropped = image.crop((left_c, top_c, right_c, bottom_c))
        if only_show:
            image_cropped.show()
        else:
            file_path_cropped = get_new_filename(file_path)
            image_cropped.save(file_path_cropped)


def get_new_filename(file_path):
    name, ext = os.path.splitext(file_path)
    return name + POSTFIX + ext


if __name__ == "__main__":
    main()
