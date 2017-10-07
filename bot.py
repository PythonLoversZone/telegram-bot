import logging
import telegram
from telegram.ext import CommandHandler, Updater

#  导入第三方功能
from jokes import get_joke
from jokes import get_joke_images
from invitecode import get_invite_code
from image import parse_img_url

# 设置log等级
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


TOKEN = ''

HELPTEXT = '''
萌新bot,请大家多多关照！
以下是命令列表：
/start 获取所有命令
/invitecode 获取注册邀请码
/joke 来个段子
/joke_pic 来张搞笑图
/pic<空格>关键字 获取一张对应的图片 如（/pic 太阳）

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
def joke(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=get_joke())

# joke pic 命令部分
def joke_pic(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=get_joke_images())


def pic(bot, update):
    keyword = update.message.text.split(' ')[-1]
    print(keyword)
    if keyword == '/pic':
        bot.send_message(chat_id=update.message.chat_id,
                         text='蜜汁错误，注意格式喔')
    else:
        photo_url = parse_img_url(keyword)
        print(photo_url)
        bot.send_photo(chat_id=update.message.chat_id,
                       photo=photo_url)


# 注册事件处理handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

invitecode_handler = CommandHandler('invitecode', invitecde)
dispatcher.add_handler(invitecode_handler)

joke_handler = CommandHandler('joke', joke)
dispatcher.add_handler(joke_handler)

joke_pic_handler = CommandHandler('joke_pic', joke_pic)
dispatcher.add_handler(joke_pic_handler)

pic_handler = CommandHandler('pic', pic)
dispatcher.add_handler(pic_handler)

# 开始轮询
updater.start_polling()
