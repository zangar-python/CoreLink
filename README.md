Этот проект создан для того чтобы я мог попркһактиковаться на реальных задачах и оценить насколько они сложные.



запустит можно:
    Перед запуском проверьте скачано ли нужные пакеты.
    Пакеты : djangorestframework , redis , celery , psycopg2-binary
    Можете установить их  с помощью команды "pip install **название-пакета"
    DRF - сперва перейдите на папку corelink,дальше в терминале напишите команду "python manage.py runserver"
    celery-worker - перейдите на папку corelink,напишите команду "celery -A infrastructure worker --pool=solo -l info"
    celery-beat - перейдите на папку corelink,напишите команду "celery -A infrastructure beat -l info"

url:

/api/register/	POST	регистрация
/api/login/	POST	вход, получить токен
/api/	GET	профиль
/api/wiki/	GET/POST	список или создать вики
/api/wiki/<id>/	GET/PATCH/DELETE	отдельная статья
/api/wiki/top/	GET	топ вики
/api/wiki/<wiki_id>/change/	POST	подать заявку на изменение
/api/change/	GET DELETE	все заявки 
/api/change/my/	GET мои заявки
/api/change/<id>/ GET POST DELETE посмотреть принять отказать
/api/admin/users/	GET	список пользователей
/api/admin/top/	POST	задать топ-вики
/api/admin/del-active/	DELETE	удалить активность
/api/admin/del-user/<id>/	DELETE	удалить пользователя