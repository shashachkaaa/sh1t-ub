#    Sh1t-UB (telegram userbot by sh1tn3t)
#    Copyright (C) 2021-2022 Sh1tN3t

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import asyncio

import os
import re
import sys

import atexit
import tempfile

import requests

from typing import List

from git import Repo
from git.exc import GitCommandError

from pyrogram import Client, types
from .. import loader, utils

VALID_URL = r"[-[\]_.~:/?#@!$&'()*+,;%<=>a-zA-Z0-9]+"
VALID_PIP_PACKAGES = re.compile(
    r"^\s*# required:(?: ?)((?:{url} )*(?:{url}))\s*$".format(url=VALID_URL),
    re.MULTILINE,
)
GIT_REGEX = re.compile(
    r"^https?://github\.com((?:/[a-z0-9-]+){2})(?:/tree/([a-z0-9-]+)((?:/[a-z0-9-]+)*))?/?$",
    flags=re.IGNORECASE,
)


async def get_git_raw_link(repo_url: str):
    """Получить raw ссылку на репозиторий"""
    match = GIT_REGEX.search(repo_url)
    if not match:
        return False

    repo_path = match.group(1)
    branch = match.group(2)
    path = match.group(3)

    r = await utils.run_sync(requests.get, f"https://api.github.com/repos{repo_path}")
    if r.status_code != 200:
        return False

    branch = branch or r.json()["default_branch"]

    return f"https://raw.githubusercontent.com{repo_path}/{branch}{path or ''}/"


@loader.module(name="Loader", author="sh1tn3t | shashachkaaa")
class LoaderMod(loader.Module):
    """Загрузчик модулей"""

    async def loadmod_cmd(self, app: Client, message: types.Message):
        """Загрузить модуль по файлу. Использование: <реплай на файл>"""
        reply = message.reply_to_message
        file = (
            message
            if message.document
            else reply
            if reply and reply.document
            else None
        )

        if not file:
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Необходим ответ на файл</b>")

        temp_file = tempfile.NamedTemporaryFile("w")
        await file.download(temp_file.name)

        try:
            with open(temp_file.name, "r", encoding="utf-8") as file:
                module_source = file.read()
        except UnicodeDecodeError:
            temp_file.close()
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Неверная кодировка файла</b>")

        module_name = await self.all_modules.load_module(module_source)
        if module_name is True:
            return await utils.answer(
                message, "<emoji id=5206607081334906820>✔️</emoji> <b>Зависимости установлены. Требуется перезагрузка</b>")

        if not module_name:
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Не удалось загрузить модуль. Подробности смотри в логах</b>")

        temp_file.close()
        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Модуль \"<code>{module_name}</code>\" загружен</b>")

    async def unloadmod_cmd(self, app: Client, message: types.Message, args: str):
        """Выгрузить модуль. Использование: unloadmod <название модуля>"""
        module_name, text = utils.get_module_name(message)
        
        if module_name.lower() in ["loader", "help", "tester", "updater", "information", "executor", "settings", "terminal"]:
        	return await utils.answer(message, f"<emoji id=5210952531676504517>❌</emoji> <code>{module_name}</code> <b>является системным модулем, его выгрузить невозможно!</b>")
        
        self.all_modules.unload_module(module_name)

        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Модуль \"<code>{module_name}</code>\" выгружен</b>\n\n{text}")

    async def ml_cmd(self, app: Client, message: types.Message, args: str):
        """Поделится модулем"""
    	
        if not args:
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Нет аргументов</b>")
        
        module_name, text = utils.get_module_name(message)
        
        try:
            await utils.answer(message, chat_id=message.chat.id, document=True, response=f'sh1t-ub/modules/{module_name}.py', caption = f'<emoji id=5433653135799228968>📁</emoji> <b>Файл</b> <code>{module_name}</code>\n\n<emoji id=5463408862499466706>😎</emoji> <code>.loadmod</code> <b>в ответ на это сообщение, чтобы установить модуль</b>\n\n{text}')
        except Exception as e:
            logging.error(e)
            await utils.answer(message, "<emoji id=5210952531676504517>❌</emoji> <b>Модуль не найден</b>")