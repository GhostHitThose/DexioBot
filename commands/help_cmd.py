def run(chat_id, update, context):
    message = "List of Commands:\n /track - Displays live pricing information\n /cmc - Displays CoinMarketCap Site\n /chart - Displays Chart Links\n /contract - Displays Contract \n /website - Displays Website Link\n /wallet - Shows Information about the Wallet\n /info - Provides information about Dexi"
    context.bot.send_message(chat_id=chat_id, text=message)
