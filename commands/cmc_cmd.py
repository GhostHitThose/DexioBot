def run(chat_id, update, context):
	message = "https://coinmarketcap.com/currencies/dexioprotocol/"
	context.bot.send_message(chat_id=chat_id, text=message)
