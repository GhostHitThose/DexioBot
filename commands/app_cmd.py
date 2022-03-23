def run(chat_id, update, context):
	message = "App Coming Soon!"
	context.bot.send_message(chat_id=chat_id, text=message)
