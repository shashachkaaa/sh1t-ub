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

from pyrogram import Client, types
from .. import loader, utils


@loader.module(name="Settings", author="sh1tn3t | shashachkaaa")
class SettingsMod(loader.Module):
    """Настройки бота"""

    async def setprefix_cmd(self, app: Client, message: types.Message, args: str):
        """Изменить префикс, можно несколько штук разделённые пробелом. Использование: setprefix <префикс> [префикс, ...]"""
        if not (args := args.split()):
            return await utils.answer(
                message, "<emoji id=5436113877181941026>❓</emoji> <b>На какой префикс нужно изменить?</b>")

        self.db.set("sh1t-ub.loader", "prefixes", list(set(args)))
        prefixes = ", ".join(f"<code>{prefix}</code>" for prefix in args)
        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Префикс был изменен на</b> «{prefixes}»")

    async def addalias_cmd(self, app: Client, message: types.Message, args: str):
        """Добавить алиас. Использование: addalias <новый алиас> <команда>"""
        if not (args := args.lower().split(maxsplit=1)):
            return await utils.answer(
                message, "<emoji id=5436113877181941026>❓</emoji> <b>Какой алиас нужно добавить?</b>")

        if len(args) != 2:
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Неверно указаны аргументы."
                         "<emoji id=5206607081334906820>✔️</emoji> <b>Пример:</b> <code>addalias</code> (новый алиас) (команда)"
            )

        aliases = self.all_modules.aliases
        if args[0] in aliases:
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Такой алиас уже существует</b>")

        if not self.all_modules.command_handlers.get(args[1]):
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Такой команды нет</b>")

        aliases[args[0]] = args[1]
        self.db.set("sh1t-ub.loader", "aliases", aliases)

        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Алиас</b> «<code>{args[0]}</code>» <b>для команды</b> «<code>{args[1]}</code>» <b>был добавлен</b>")

    async def delalias_cmd(self, app: Client, message: types.Message, args: str):
        """Удалить алиас. Использование: delalias <алиас>"""
        if not (args := args.lower()):
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Какой алиас нужно удалить?</b>")

        aliases = self.all_modules.aliases
        if args not in aliases:
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Такого алиаса нет</b>")

        del aliases[args]
        self.db.set("sh1t-ub.loader", "aliases", aliases)

        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Алиас</b> «<code>{args}</code>» <b>был удален</b>")

    async def aliases_cmd(self, app: Client, message: types.Message):
        """Показать все алиасы"""
        aliases = self.all_modules.aliases
        if not aliases:
            return await utils.answer(
                message, "<emoji id=5463044060862244442>🤷‍♂</emoji> <b>Алиасы отсутствуют</b>")

        return await utils.answer(
            message, "<emoji id=5956561916573782596>📄</emoji> <b>Список всех алиасов:</b>\n" + "\n".join(
                f"<emoji id=4972281662894244560>🛑</emoji> <code>{alias}</code> ➜ <code>{command}</code>"
                for alias, command in aliases.items()
            )
        )

    async def hidemod_cmd(self, app: Client, message: types.Message, args: str):
        """Скрыть модуль. Использование: hidemod <название модуля>"""
        if not args:
            return await utils.answer(
                message, "<emoji id=5436113877181941026>❓</emoji> <b>Какой модуль нужно скрыть?</b>"
            )

        module_name = args.lower()
        hide_mods = self.db.get("help", "hide_mods", [])
        
        all_modules = [module.name.lower() for module in self.all_modules.modules]
        
        module_name, text = utils.find_closest_module_name(module_name, all_modules)
        
        if module_name in hide_mods:
            return await utils.answer(
                message, f"<emoji id=5210952531676504517>❌</emoji> <b>Модуль</b> «<code>{module_name}</code>» <b>уже скрыт</b>\n\n{text}"
            )

        hide_mods.append(module_name)
        self.db.set("help", "hide_mods", hide_mods)

        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Модуль</b> «<code>{module_name}</code>» <b>скрыт</b>\n\n{text}"
        )

    async def showmod_cmd(self, app: Client, message: types.Message, args: str):
        """Показать скрытый модуль. Использование: showmod <название модуля>"""
        if not args:
            return await utils.answer(
                message, "<emoji id=5436113877181941026>❓</emoji> <b>Какой модуль нужно показать?</b>"
            )

        module_name = args.lower()
        hide_mods = self.db.get("help", "hide_mods", [])
        
        all_modules = [module.name.lower() for module in self.all_modules.modules]
        
        module_name, text = utils.find_closest_module_name(module_name, all_modules)
        
        if module_name not in hide_mods:
            return await utils.answer(
                message, f"<emoji id=5210952531676504517>❌</emoji> <b>Модуль</b> «<code>{module_name}</code>» <b>не скрыт</b>\n\n{text}"
            )

        hide_mods.remove(module_name)
        self.db.set("help", "hide_mods", hide_mods)

        return await utils.answer(
            message, f"<emoji id=5206607081334906820>✔️</emoji> <b>Модуль</b> «<code>{module_name}</code>» <b>теперь виден</b>\n\n{text}"
        )

    async def hiddenmods_cmd(self, app: Client, message: types.Message):
        """Показать список скрытых модулей. Использование: hiddenmods"""
        hide_mods = self.db.get("help", "hide_mods", [])
        
        if not hide_mods:
            return await utils.answer(
                message, "<emoji id=5463044060862244442>🤷‍♂</emoji> <b>Скрытых модулей нет</b>"
            )

        return await utils.answer(
            message, "<emoji id=5956561916573782596>📄</emoji> <b>Список скрытых модулей:</b>\n" + "\n".join(
                f"<emoji id=4972281662894244560>🛑</emoji> <code>{module}</code>"
                for module in hide_mods
            )
        )