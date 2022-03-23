import os
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from commands import *
import requests

#command alias
command_name = "track"
command_quit = "quit"
command_cmc = "cmc"
command_website = "website"
command_contract = "contract"
command_get_chart = "chart"
command_kick = "kick"
command_help = "support"
command_wallet = "wallet"
command_app = "app"
command_mute = "mute"
command_mute_time_check = "timecheck"

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

# change to = read_token() if you want to read token from file
telegram_bot_token = read_token()
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

#functions for each command


def track(update, context):
    chat_id = update.effective_chat.id
    track_cmd.run(chat_id, update, context)

def quit(update, context):
    chat_id = update.effective_chat.id
    quit_cmd.run(chat_id, update, context)

def cmc(update, context):
    chat_id = update.effective_chat.id
    cmc_cmd.run(chat_id, update, context)

def website(update, context):
    chat_id = update.effective_chat.id
    website_cmd.run(chat_id,update,context)

def contract(update, context):
    chat_id = update.effective_chat.id
    contract_cmd.run(chat_id, update, context)

def get_chart(update, context):
    chat_id = update.effective_chat.id
    get_chart_cmd.run(chat_id, update, context)

def kick(update, context):
    chat_id = update.effective_chat.id
    kick_cmd.run(chat_id, update, context)

def mute(update, context):
    chat_id = update.effective_chat.id
    mute_cmd.run(chat_id, update, context)

def help(update, context):
    chat_id = update.effective_chat.id
    help_cmd.run(chat_id, update, context)

def wallet(update, context):
    chat_id = update.effective_chat.id
    wallet_cmd.run(chat_id, update, context)

def app(update, context):
    chat_id = update.effective_chat.id
    app_cmd.run(chat_id, update, context)

def time_check(update, context):
    chat_id = update.effective_chat.id
    time_check_cmd.run(chat_id, update, context)

# end of functions for commands

def test(update, context):
    chat_id = update.effective_chat.id
    if mute_cmd.isMuted(update.message.from_user, context, update, chat_id):
        mute_cmd.delete_message(chat_id, update, context)
    else:
        pass



#commandhandler calling comamnds
dispatcher.add_handler(CommandHandler(command_name, track))
dispatcher.add_handler(CommandHandler(command_quit, quit))
dispatcher.add_handler(CommandHandler(command_cmc, cmc))
dispatcher.add_handler(CommandHandler(command_website, website))
dispatcher.add_handler(CommandHandler(command_contract, contract))
dispatcher.add_handler(CommandHandler(command_get_chart, get_chart))
dispatcher.add_handler(CommandHandler(command_help, help))
dispatcher.add_handler(CommandHandler(command_wallet, wallet))
dispatcher.add_handler(CommandHandler(command_app, app))
dispatcher.add_handler(CommandHandler(command_kick, kick))
dispatcher.add_handler(CommandHandler(command_mute, mute))
dispatcher.add_handler(CommandHandler(command_mute_time_check, time_check))
#messagehandler
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), test))

updater.start_polling()
updater.idle()
