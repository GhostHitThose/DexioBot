def run(chat_id, update, context):
	message = "Stopping Bot for Development"
	user_status = context.bot.get_chat_member(chat_id, update.message.from_user.id)['status']
	if user_status == "administrator" or user_status == "creator":
		updater.stop()
		context.bot.send_message(chat_id=chat_id, text=message)
		
