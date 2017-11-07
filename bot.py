import logging
import telegram
from telegram.ext import CommandHandler, Updater

#  导入第三方功能
from spider import get_joke
from spider import get_boring_images
from spider import get_meizi_images
# 导入获取邀请码模块
from invitecode import get_invite_code


# 设置log等级
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


TOKEN = ''

HELPTEXT = '''
萌新bot,请大家多多关照！

以下是命令列表：
/start 获取所有命令
/invitecode 获取注册邀请码
/duanzi 来个段子
/funpic 无聊图
/meizitu 来张妹纸图

更多功能正在开发中....
'''

# 注册updater
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


# start命令 部分
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=HELPTEXT)

# invitecde 命令部分
def invitecde(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=get_invite_code())

# joke 命令部分
def get_duanzi(bot, update):
    print('123')
    bot.send_message(chat_id=update.message.chat_id,
                     text=get_joke())

# joke pic 命令部分
def get_boringpic(bot, update):
    url = get_boring_images()
    if url[-3:] == 'gif':
        bot.send_document(chat_id=update.message.chat_id,
                          document=url)
    else:
        bot.send_photo(chat_id=update.message.chat_id, photo=url)


# 煎蛋网妹纸图部分
def get_meizitu(bot, update):
    url = get_meizi_images()
    if url[-3:] == 'gif':
        bot.send_document(chat_id=update.message.chat_id,
                          document=url)
    else:
        bot.send_photo(chat_id=update.message.chat_id, photo=url)


# 注册事件处理handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

invitecode_handler = CommandHandler('invitecode', invitecde)
dispatcher.add_handler(invitecode_handler)

joke_handler = CommandHandler('duanzi', get_duanzi)
dispatcher.add_handler(joke_handler)

joke_pic_handler = CommandHandler('funpic', get_boringpic)
dispatcher.add_handler(joke_pic_handler)

meizitu_handler = CommandHandler('meizitu', get_meizitu)
dispatcher.add_handler(meizitu_handler)

# 开始轮询
updater.start_polling()
