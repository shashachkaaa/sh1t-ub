__authors__ = "Sh1tN3t - @sh1tn3t"
__version__ = "0.71"

change_log = """
Буду сюда писать по поводу изменений.

Новая версия 0.2 (все еще бетка, релиз когда нибудь):

убрал кое че лишнее
добавил команду рестарт
работает хелп: -help <название модуля>
прикрутил бд


Новая версия 0.21 (все еще бетка, релиз когда нибудь):

добавлены алиасы для команд


Новая версия 0.3 (все еще бетка, релиз когда нибудь):

добавлен загрузчик сторонних модулей
добавлена выгрузка модулей
добавлена перезагрузка юзербота (полноценная, а не только модули)


Новая версия 0.4 (все еще бетка, релиз когда нибудь):

добавлена обработка сторонних хендлеров (например @app.on_message через eval)
новый пингер


Новая версия 0.5 (все еще бетка, релиз когда нибудь):

добавлена настройка конфига (api id/hash) при первом запуске бота


Новая версия 0.6 (все еще бетка, релиз когда нибудь):

сделан кастомный класс Message, добавлены функции get_args, get_full_command, answer
добавлена поддержка фильтров (в виде декоратора над функцией команды)
изменена база данных, а именно функции get, set и pop


Новая версия 0.7 (все еще бетка, релиз когда нибудь):

убран кастомный класс Message (из-за некоторых неудобств)
функция команды теперь может принимать аргумент args (обычные аргументы вместо utils.get_args(message)): async def func_cmd(self, app, message, args)
добавлена своя база данных основанная на LightDB
в названии сесси будет отображаться Sh1t-UB и текущая версия юзербота
в utils добавлены новые функции get_message_media, get_media_ext
функция answer в utils теперь принимает аргумент doc или photo, для отправки документа, если doc == True, или фото, если photo == True


Новая версия 0.71 (все еще бетка, релиз когда нибудь):

рефактор кода pep8
добавлена лицензия во все файлы
"""