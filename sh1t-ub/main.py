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

from pyrogram.methods.utilities.idle import idle
from . import auth, database, loader


async def main():
    """Основной цикл юзербота"""
    me, app = await auth.Auth().authorize()
    await app.initialize()

    db = database.db
    db.init_cloud(app, me)

    modules = loader.ModulesManager(app, db, me)
    await modules.load(app)

    if (restart := db.get("sh1t-ub.loader", "restart")):
            try:
            	text = "✅ Перезагрузка прошла успешно!" if restart["type"] == "restart" else "✅ Обновление прошло успешно!"
            	id = restart["msg"].split(":")
            	await app.edit_message_text(id[0], id[1], text)
            except:
            	pass
            
            db.pop("sh1t-ub.loader", "restart")

    prefix = db.get("sh1t-ub.loader", "prefixes", ["."])[0]
    bot_info = await modules.bot_manager.bot.me()

    logging.info(f"Стартовал для [ID: {modules.me.id}] успешно, введи {prefix}help в чате для получения списка команд")
    logging.info(f"Твой бот: @{bot_info.username} [ID: {bot_info.id}]")

    await idle()

    logging.info("Завершение работы...")
    return True
