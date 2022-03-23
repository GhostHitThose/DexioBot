from tracker import get_crypto_prices

def run(chat_id, update, context):
    crypto_data = get_crypto_prices()
    percent_change = crypto_data['data']['DEXI']['quote']['USD']['percent_change_24h']
    percent_change7 = crypto_data['data']['DEXI']['quote']['USD']['percent_change_7d']
    # last_updated = crypto_data['data']['DEXI']['quote']['USD']['last_updated']
    # last_updated_final = last_updated[5:10]+last_updated[4]+last_updated[:4]
    price = f"{float(crypto_data['data']['DEXI']['quote']['USD']['price']):,.8f}"
    coin_symbol = crypto_data['data']['DEXI']['symbol']
    message = f"{coin_symbol}\n"

    message += f"Price: ${price}\n"
    message += f"Percent Change 24hr: {percent_change:,.2f}" + chr(37) + "\n"
    message += f"Percent Change 7d: {percent_change7:,.2f}" + chr(37)  + "\n"
    # message += f"Last updated: {last_updated_final}"

    context.bot.send_message(chat_id=chat_id, text=message)
    