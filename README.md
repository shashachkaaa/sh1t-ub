<p align="center">
    <img src="https://my.fl1yd.su/sh1t-ub_nobg.png">
    <br>
    <b>Sh1T UB (fork)</b> — крутой юзербот написанный на <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>
    <br>
    <a href="https://t.me/Sh1T_ub">Канал с обновлениями</a>
    •
    <a href="https://t.me/Sh1T_ub">Чат поддержки</a>
    •
    <a href="https://t.me/Sh1T_ub">Канал с модулями</a>
</p>

<a href="https://github.com/shashachkaaa/sh1t-ub/stargazers">
    <img src="https://badgen.net/github/stars/shashachkaaa/sh1t-ub" alt="stars">
</a>
<a href="https://github.com/shashachkaaa/sh1t-ub/watchers">
    <img src="https://badgen.net/github/watchers/shashachkaaa/sh1t-ub" alt="watchers">
</a>
<a href="https://github.com/shashachkaaa/sh1t-ub/commits/main">
    <img src="https://badgen.net/github/commits/shashachkaaa/sh1t-ub/main" alt="commits">
</a>
<br>
<a href="https://www.codefactor.io/repository/github/shashahchkaaa/sh1t-ub">
    <img src="https://www.codefactor.io/repository/github/shashachkaaa/sh1t-ub/badge" alt="CodeFactor"/>
</a>

# Sh1T UserBot (Fork by shashachkaaa)

Это форк оригинального проекта [Sh1t-ub](https://github.com/sh1tn3t/sh1t-ub), созданного [Sh1tN3t](https://github.com/sh1tn3t).

## Лицензия
Этот проект распространяется под лицензией GNU GPL v3. Подробнее см. в файле [LICENSE](LICENSE).

## Изменения
- Обновлен под актуальный Pyrogram (Kurigram)
- Обнволен под актуальный Aiogram 3.18.0
- Большие изменения почти в каждом файле
- Исправлено большое количество багов
- Исправлена проблема с крашем всех сессий

<h1>Описание</h1>

sh1t-ub — это ваш интерактивный многофункциональный помощник в Телеграме  
Многофункциональный и расширяемый юзербот позволит создавать любые модули, нужна лишь фантазия

Подключение к аккаунту происходит посредством создании новой (!) сессии

Наши преимущества:
<ul>
    <li>Удобство и простота в использовании</li>
    <li>Низкая ресурсозатраность</li>
    <li>Большой ассортимент готовых модулей</li>
    <li>Грамотное построение структуры каждого модуля</li>
    <li>Асинхронное выполнение каждой задачи</li>
    <li>Удобная загрузка и выгрузка модулей</li>
    <li>Инлайн бот</li>
</ul>


<h1>Установка</h1>

<h2>На свой сервер</h2>

Для начала нужно установить компоненты:

<pre lang="bash">
apt update && apt upgrade -y && apt install -y openssl git python3 python3-pip
</pre>

После этого клонировать репозиторий и установить зависимости:

<pre lang="bash">
git clone https://github.com/shashachkaaa/sh1t-ub.git && cd sh1t-ub
pip3 install -r requirements.txt
</pre>


<h1>Запуск</h1>

> При первом запуске потребуется ввести api_id и api_hash. Их можно получить на <a href="https://my.telegram.org">my.telegram.org</a>

<pre lang="bash">
python3 -m sh1t-ub
</pre>

вы также можете:

<pre lang="bash">
$ python3 -m sh1t-ub --help
usage: sh1t-ub [--help] [--log-level LOGLEVEL]

Телеграм юзербот разработанный sh1tn3t‘ом & shashachkaaa

optional arguments:
  --help, -h            Показать это сообщение
  --log-level LOGLEVEL, -lvl LOGLEVEL
                        Установить уровень логирования. Доступно: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL или число от 0 до 50

Канал оригинального sh1t-ub: @sh1tub
Канал форка: @sh1t_ub
</pre>

<h1>Пример модуля</h1>

> Больше примеров функций и полное описание смотри в файле <a href="./sh1t-ub/modules/_example.py">_example.py</a>

<pre lang="python">
from pyrogram import Client, types
from .. import loader, utils


@loader.module(name="Example")
class ExampleMod(loader.Module):
    """Описание модуля"""

    async def example_cmd(self, app: Client, message: types.Message):
        """Описание команды"""
        return await utils.answer(
            message, "Пример команды")

    @loader.on(lambda _, __, m: m and m.text == "Привет, это проверка вотчера щит-юб")
    async def watcher(self, app: Client, message: types.Message):
        return await message.reply(
            "Привет, все работает отлично")
</pre>


<h1>Ссылки</h1>

<ul>
    <li><a href="https://t.me/Sh1T_ub">Модули</a></li>
</ul>
