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

import io
import logging
import time

from datetime import datetime
from pyrogram import Client, types

from .. import loader, utils, logger


@loader.module(name="Tester", author="sh1tn3t")
class TesterMod(loader.Module):
    """Тест чего-то"""

    async def ping_cmd(self, app: Client, message: types.Message, args: str):
        """Пингует"""
        a = time.time()
        m = await utils.answer(message, f"<emoji id=5463408862499466706>😎</emoji>")
        if m:
        	b = time.time()
        	return await utils.answer(message, f'<emoji id=5463408862499466706>😎</emoji> Пинг: <b>{round((b - a) * 1000, 3)}</b> ms)

    async def logs_cmd(self, app: Client, message: types.Message, args: str):
        """Отправляет логи. Использование: logs <уровень>"""
        lvl = 40  # ERROR

        if args and not (lvl := logger.get_valid_level(args)):
            return await utils.answer(
                message, "❌ Неверный уровень логов")

        handler = logging.getLogger().handlers[0]
        logs = ("\n".join(handler.dumps(lvl))).encode("utf-8")
        if not logs:
            return await utils.answer(
                message, f"❕ Нет логов на уровне {lvl} ({logging.getLevelName(lvl)})")

        logs = io.BytesIO(logs)
        logs.name = "sh1t-ub.log"

        await message.delete()
        return await utils.answer(
            message, logs, doc=True, quote=False,
            caption=f"📤 Sh1t-UB Логи с {lvl} ({logging.getLevelName(lvl)}) уровнем"
        )
