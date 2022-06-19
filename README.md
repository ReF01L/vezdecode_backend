# vezdecode_backend
# Task 1
Необходимо создать .env файл в корневой директории
И внести следующие поля:
owner_id=*
album_id=*

`python -m venv venv`

`./venv/bin/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py download_memes start`

# Task 2
Необходимо дополнительно запустить сервер:

`python manage.py runserver`

Далее регистрируем пользователя, по запросу

POST/ `http://127.0.0.1:8000/register`
в тело передаем login и пароль

необходимо иметь NodeJS >=14.0

Далее поднимаем фронтенд

`cd dashboadrd_client`

`npm install`

`npm run serve`

Got to - `127.0.0.1:8080/images` in your browser

На этой странице реализован минимальный GUI для взаимодействия с картинками

Сходий с этим запрос будет лайкать\анлайкать запись `127.0.01:8000/post/like?photo_id={photo_id}`, photo_id = 457240793


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

# Task 4
Далее запустить `python manage.py download_memes start` и ожидать, пока не закончится заполнение БД.

# Task 5
Необходимо иметь предустановленный nodejs

`cd dashboadrd_client`

`npm install`

`npm run serve`

Got to - `127.0.0.1:8080/` in your browser

На текущий момент, дашборд может просматривать только первый зарегистрировавшийся пользователь (с id = 1), отправляется всегда он, дабы это изменить нужно залезть в код:
dashboard_client/src/components/DashboardPage -> 13 строка
