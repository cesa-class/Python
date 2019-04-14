from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler)
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import model


def start(bot, update, args):
    print(update)

    bot.send_message(chat_id=update.message.chat_id, text='Amin pool nadade!')
    if args:
        print(args)
        target = args[0]
        model.make_connection(int(update.message.chat_id), int(target))
        bot.send_message(chat_id=update.message.chat_id, text='connected to {}'.format(target))


def link(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,
                     text='t.me/pnfarabibot?start={}'.format(chat_id))

def echo(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text
    target = model.get_target(chat_id)
    model.save_messages(chat_id, target, message)

    reply = InlineKeyboardButton(text='Reply', callback_data='--reply--')
    markup = InlineKeyboardMarkup([[reply]])

    bot.send_message(chat_id=target, text=message, reply_markup=markup)
    bot.send_message(chat_id=chat_id, text='Sent!')


def callback(bot, update):
    if update.callback_query.data == '--reply--':
        from_id = update.callback_query.from_user.id
        message = update.callback_query.message.text
        model.reply_command(from_id, message)
        bot.sendMessage(from_id, "پیام های بعدی به فرستنده پیام انتخاب شده ارسال می شوند!")



if __name__ == '__main__':
    model.make_database()

    TOKEN = '<TOKEN>'
    REQ = {'proxy_url': 'socks5h://127.0.0.1:9050'}
    updater = Updater(token=TOKEN, request_kwargs=REQ)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start, pass_args=True)
    dispatcher.add_handler(start_handler)

    link_handler = CommandHandler('link', link)
    dispatcher.add_handler(link_handler)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    callback_handler = CallbackQueryHandler(callback)
    dispatcher.add_handler(callback_handler)

    updater.start_polling()
    updater.idle()