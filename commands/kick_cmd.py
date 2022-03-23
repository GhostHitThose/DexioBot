def run(chat_id, update, context):
	# checks if cmd runner is admin/creator
	if context.bot.get_chat_member(chat_id, update.message.from_user.id)['status'] == "administrator" or context.bot.get_chat_member(chat_id, update.message.from_user.id)['status'] == "creator":
		#checks if real arguments were provided
		if len(context.args) > 0:
			try:
				#checks if the chat_id provided is an admin/creator
				if context.bot.get_chat_member(chat_id, context.args[0])['status'] == "administrator" or context.bot.get_chat_member(chat_id, context.args[0])['status'] == "creator":
					context.bot.send_message(chat_id=chat_id, text="They have administrator permissions.")
				else:
					#kicks them if runner is admin/creator and user_id provided is < admin/creator
					try:
						update.message.chat.kick_member(context.args[0])
					except:
						context.bot.send_message(chat_id=chat_id, text="Bot doesn't have administrator permissions.")
			except:
				context.bot.send_message(chat_id=chat_id, text="Invalid chat_id.")
		else:
			context.bot.send_message(chat_id=chat_id, text="No arguments provided.")
	else:
		context.bot.send_message(chat_id=chat_id, text="No permissions to run command.")
# end command
