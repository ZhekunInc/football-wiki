from io import BytesIO
from django.core.management.base import BaseCommand
from django.core import files
from geo.models import Country

import requests
import PIL


class Command(BaseCommand):
    def handle(self, *args, **options):
        photo_qs = Country.objects.filter(flag_file__exact=None)
        print(len(photo_qs))

        for photo in photo_qs:
            link = photo.get_download_url_or_none()
            if not link:
                continue

            headers = {
                'User-Agent': "Mozilla/5.0 (X11; CrOS i686 0.12.433) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.77 Safari/534.30"
            }
            request = requests.get(link, stream=True, headers=headers)

            if request.status_code != 200:
                continue

            lf = BytesIO()

            for block in request.iter_content(1024 * 8):

                if not block:
                    break

                lf.write(block)
                print(lf.write(block))
            try:
                img_type = PIL.Image.open(lf).format.lower()

            except PIL.UnidentifiedImageError:
                print(
                    "Неможливо зчитати фотографію. "
                    "Збережене посилання: %s. "
                    "Посилання для завантаження: %s." % (photo.flag, link)
                )
                continue

            file_name = "%s.%s" % (photo.flag.split("/")[-1], img_type)

            photo.flag_file.save(file_name, files.File(lf))

            img_mode = PIL.Image.open(lf).mode
            if img_mode == "CMYK":
                image = PIL.Image.open(lf)
                image = image.convert('RGB')
                image.save(
                    photo.flag_file.path, format=img_type.upper(), quality=100
                )
