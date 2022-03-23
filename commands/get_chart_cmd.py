def run(chat_id, update, context):
	message = "Chart at\n📈Poocoin:\nhttps://poocoin.app/tokens/0x29b1e39a529d3b3cacea55989594f71813e998bb/\n📈Bogged:\nhttps://charts.bogged.finance/?token=0x29b1E39A529d3B3cacEA55989594F71813e998Bb"
	context.bot.send_message(chat_id=chat_id, text=message)
