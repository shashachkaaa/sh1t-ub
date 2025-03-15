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
from .. import loader, utils, __version__


from bs4 import BeautifulSoup

def sanitize_html(text: str) -> str:
    """Очищает HTML-текст, закрывая незакрытые теги."""
    return BeautifulSoup(text, "html.parser").prettify()

@loader.module(name="Help", author="sh1tn3t")
class HelpMod(loader.Module):
    """Помощь по командам юзербота"""

    async def help_cmd(self, app: Client, message: types.Message, args: str):
        """Список всех модулей"""
        if not args:
            text = ""
            for module in self.all_modules.modules:
                commands = inline = ""

                commands += " <b>|</b> ".join(
                    f"<code>{command}</code>" for command in module.command_handlers
                )

                if module.inline_handlers:
                    if commands:
                        inline += " <b>|| 🎹</b>: "
                    else:
                        inline += "<b>🎹</b>: "

                inline += " <b>|</b> ".join(
                    f"<code>{inline_command}</code>" for inline_command in module.inline_handlers
                )

                text += f"\n<b>📦 {module.name}</b>: " + commands + inline

            return await utils.answer(
                message, f"<b>🛠 Всего модулей: {len(self.all_modules.modules)}</b>\n"
                        f"{text}"
            )

        if not (module := self.all_modules.get_module(args)):
            return await utils.answer(
                message, "<emoji id=5210952531676504517>❌</emoji> <b>Такого модуля нет</b>")

        prefix = self.db.get("sh1t-ub.loader", "prefixes", ["."])[0]
        bot_username = (await self.bot.me()).username

        command_descriptions = "\n".join(
            f"👉 <code>{prefix + command}</code>\n"
            f"    ╰ {sanitize_html(module.command_handlers[command].__doc__ or 'Нет описания для команды')}"
            for command in module.command_handlers
        )
        inline_descriptions = "\n".join(
            f"👉 <code>@{bot_username + ' ' + command}</code>\n"
            f"    ╰ {sanitize_html(module.inline_handlers[command].__doc__ or 'Нет описания для команды')}"
            for command in module.inline_handlers
        )

        header = (
            f"<b>🖥 Модуль:</b> <code>{module.name}</code>\n" + (
                f"<b>👨🏿‍💻 Автор:</b> <code>{sanitize_html(module.author)}</code>\n" if module.author else ""
            ) + (
                f"<b>🔢 Версия:</b> <code>{sanitize_html(module.version)}</code>\n" if module.version else ""
            ) + (
                f"\n<b>📄 Описание:</b>\n"
                f"    ╰ {sanitize_html(module.__doc__ or 'Нет описания для модуля')}\n\n"
            )
        )

        return await utils.answer(
            message, header + command_descriptions + "\n" + inline_descriptions
        )