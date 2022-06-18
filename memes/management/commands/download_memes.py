import os
from pathlib import Path

import requests
from django.conf import settings
from django.core.management import BaseCommand
from vk_api import VkApi

__author__ = 'Dmitry Salushkin <salushkin.ds@students.dvfu.ru>'
__date__ = '18.06.2022'
__version__ = '0.0.1'

from memes.models import Post
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(settings.BASE_DIR, "../../../.env"))


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('start', nargs='+', type=None)

    def handle(self, *args, **options):
        login = os.environ.get('login', '89940128262')
        password = os.environ.get('password', '12344321qWWs')
        connection = VkApi(login, password)
        connection.auth()

        path_dir = os.path.join(Path(__file__).resolve().parent.parent.parent.parent, '../../../media', 'memes')

        if not os.path.exists(path_dir):
            os.makedirs(path_dir)

        for i in range(len(self.get_photos(connection, 283939598, os.environ.get('owner_id', '-197700721'), offset=0)['items']) // 50 + 1):
            response = self.get_photos(connection, 283939598, os.environ.get('owner_id', '-197700721'), offset=i * 50)
            for photo in response['items']:
                creator = connection.method('users.get', {'user_ids': photo['user_id']})[0]
                print(f'Like count: {photo["likes"]["count"]}')
                print(f'Mem creator: {creator["last_name"]} {creator["first_name"]}')
                print('-' * 15)

                if not Post.objects.filter(photo_id=photo['id'], owner_id=photo['user_id']).exists():
                    Post.objects.create(photo_id=photo['id'], owner_id=photo['user_id'], likes=photo['likes']['count'])
                    self.download(photo, path_dir)

    def download(self, photo, output):
        r = requests.get(photo['sizes'][0]['url'])
        title = photo['id']
        with open(os.path.join(output, '%s.jpg' % title), 'wb') as f:
            for buf in r.iter_content(1024):
                if buf:
                    f.write(buf)

    def get_photos(self, connection, album_id, owner_id, offset):
        return connection.method('photos.get', {'album_id': album_id, 'owner_id': owner_id, 'extended': 1, 'offset': offset})
