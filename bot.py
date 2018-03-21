from telegram.ext import Updater

from configs import TOKEN
from handler.command_handler import (
    start_handler, invitecode_handler, joke_handler, joke_pic_handler)
from handler.message_handler import ehco_handler, unknown_handler

# 注册updater
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# 注册事件处理handler
dispatcher.add_handler(start_handler)
dispatcher.add_handler(invitecode_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(joke_pic_handler)
dispatcher.add_handler(ehco_handler)
dispatcher.add_handler(unknown_handler)


if __name__ == '__main__':
    # 开始轮询
    updater.start_polling()
    updater.idle()
