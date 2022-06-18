# vezdecode_backend
# Task 1
Необходимо создать .env файл в корневой директории
И внести следующие поля:
login=*
password=*
owner_id=*

`python -m venv venv`

`./venv/bin/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py download_memes start`

# Task 2
Необходимо дополнительно запустить сервер:

`python manage.py runserver`

GET/

`127.0.01:8000/post/like?photo_id={photo_id}`, photo_id = 457240793

Лайкнет или анлайкнет выбранный пост

GET/

`127.0.0.1:8000/posts`

Вернет все добавленные посты

# Task 3
Необходимо дополнительно запустить сервер:

`python manage.py runserver`

GET/
`127.0.0.1:8000/post/priority?photo_id={photo_id}`, photo_id = 457240806

Установит данную фотографию в приоритет и снимет с приоритета другую, если таковая имелась

GET/
`127.0.0.1:8000/posts`

Вернет все добавленные посты, при этом если есть фотография, установленная в приоритет - она будет в топе
