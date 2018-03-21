import logging

from telegram.ext import Updater

from configs import TOKEN
from commands.command_handler import (
    start_handler, invitecode_handler, joke_handler, joke_pic_handler)


# 注册updater
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# 设置log等级
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# 注册事件处理handler
dispatcher.add_handler(start_handler)
dispatcher.add_handler(invitecode_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(joke_pic_handler)

if __name__ == '__main__':
    # 开始轮询
    updater.start_polling()
