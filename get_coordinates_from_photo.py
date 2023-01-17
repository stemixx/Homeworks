"""
папка photos должна быть в одной директории с этим скриптом
pip install exif
"""

import os
from exif import Image
import glob

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PHOTO_FOLDER = os.path.join(PROJECT_FOLDER, 'photos')


def getting_images():
    for image_path in glob.glob(f'{PHOTO_FOLDER}\**\*.jpg', recursive=True):
        try:
            with open(image_path, 'rb') as image:
                print(image_path)
                data_image = Image(image)
                yield data_image
        except Exception as ex:
            print(ex)
            yield None


def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    if coordinates_ref == 'S' or coordinates_ref == 'W':
        decimal_degrees = -decimal_degrees
    return '%.6f' % decimal_degrees


def convert_dms_to_dd_all_files(images):
    for index, image in enumerate(images):
        if image:
            print(f'Latitude: {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}')
            print(f'Longitude: {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}')
            print('-' * 20)


if __name__ == '__main__':
    convert_dms_to_dd_all_files(getting_images())
