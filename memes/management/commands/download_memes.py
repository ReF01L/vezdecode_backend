import datetime
import os
import sys
from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

import requests
from vk_api import VkApi

__author__ = 'Dmitry Salushkin <salushkin.ds@students.dvfu.ru>'
__date__ = '18.06.2022'
__version__ = '0.0.1'


def download(photo, output):
    r = requests.get(photo['sizes'][0]['url'])
    title = photo['id']
    with open(os.path.join(output, '%s.jpg' % title), 'wb') as f:
        for buf in r.iter_content(1024):
            if buf:
                f.write(buf)


def get_photos(connection, album_id, owner_id):
    return connection.method('photos.get', {'album_id': album_id, 'owner_id': owner_id, 'extended': 1})


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('username', help='vk.com username')
    parser.add_argument('password', help='vk.com password')

    args = parser.parse_args()

    start_time = datetime.datetime.now()

    login = args.username
    password = args.password
    connection = VkApi(login, password)
    connection.auth()

    response = get_photos(connection, 283939598, '-197700721')

    path_dir = os.path.join(Path(__file__).resolve().parent.parent.parent.parent, 'media', 'memes')

    if not os.path.exists(path_dir):
        os.makedirs(path_dir)

    for photo in response['items']:
        creator = connection.method('users.get', {'user_ids': photo['user_id']})[0]
        print(f'Like count: {photo["likes"]["count"]}')
        print(f'Mem creator: {creator["last_name"]} {creator["first_name"]}')
        download(photo, path_dir)
