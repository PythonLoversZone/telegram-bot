from telegram.ext import MessageHandler
from telegram.ext.filters import Filters


def ehco_all(bot, update):
    '''
    打印所有传进来的文本信息
    '''
    print(update.message.text)


def unknown_command(bot, update):
    '''
    当遇到不认识的命令时，返回错误信息
    '''
    bot.send_message(chat_id=update.message.chat_id,
                     text="抱歉，我不知道这命令是啥子！！")


ehco_handler = MessageHandler(Filters.text, ehco_all)
unknown_handler = MessageHandler(Filters.command, unknown_command)
