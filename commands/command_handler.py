from telegram.ext import CommandHandler

from utils.spider import get_joke, get_joke_images
from utils.invitecode import get_invite_code

HELPTEXT = '''
萌新bot,请大家多多关照！

以下是命令列表：
/start 获取所有命令
/invitecode 获取注册邀请码
/duanzi 来个段子
/funpic 无聊图
更多功能正在开发中....
'''


def start(bot, update):
    '''
    打印欢迎信息
    '''
    bot.send_message(chat_id=update.message.chat_id,
                     text=HELPTEXT)


def invitecde(bot, update):
    '''
    发送邀请码
    '''
    bot.send_message(chat_id=update.message.chat_id,
                     text=get_invite_code())


def get_duanzi(bot, update):
    '''
    发送糗事百科段子
    '''
    bot.send_message(chat_id=update.message.chat_id,
                     text=get_joke())


def get_fun_pic(bot, update):
    '''
    发送搞笑图
    '''
    url = get_joke_images()
    if url[-3:] == 'gif':
        bot.send_document(chat_id=update.message.chat_id,
                          document=url)
    else:
        bot.send_photo(chat_id=update.message.chat_id, photo=url)


start_handler = CommandHandler('start', start)
joke_pic_handler = CommandHandler('funpic', get_fun_pic)
invitecode_handler = CommandHandler('invitecode', invitecde)
joke_handler = CommandHandler('duanzi', get_duanzi)
