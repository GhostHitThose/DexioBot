import time

LOCATION = './commands/database/mutes.txt'

def run(chat_id, update, context):
    file = open(LOCATION, "r")
    lines = file.readlines()

    #/time_check (user_id)
    try:
        user_id = context.args[0]
    except:
        context.bot.send_message(chat_id=chat_id, text='No user given.')
        return

    try:
        user = context.bot.get_chat_member(chat_id, user_id)['user']
    except:
        context.bot.send_message(chat_id=chat_id, text='User not found.')
        return

    cmd_runner_status = context.bot.get_chat_member(chat_id, update.message.from_user.id)['status']

    if cmd_runner_status == "administrator" or cmd_runner_status == "creator":
        for line in lines:
            userid, time_um = line.split(':')
            userid = int(userid)
            time_left = int(round(float(float(time_um) - float(time.time_ns()/1000000000))))
            if user.id == userid:
                user_status = context.bot.get_chat_member(chat_id, user.id)['status']
                if user_status == "administrator" or user_status == "creator":
                    context.bot.send_message(chat_id,text="The user provided is an administrator and can't be muted.")
                    return
                if int(round(float(time_um))) == -1:
                    context.bot.send_message(chat_id,text='User is muted forever.')
                    return
                if time_left < 0:
                    line_index = lines.index(line)
                    del lines[line_index]
                    new_file = open(LOCATION, "w+")

                    for new_line in lines:
                        new_file.write(new_line)

                    new_file.close()
                    context.bot.send_message(chat_id,text='User has been unmuted.')
                    return
                else:
                    days,hours,minutes,seconds=0,0,0,0
                    num = time_left
                    while num > 0:
                        if num >= 86400:
                            days += 1
                            num -= 86400
                        elif num >= 3600:
                            hours+=1
                            num-=3600
                        elif num >= 60:
                            minutes+=1
                            num-=60
                        elif num >= 1:
                            seconds+=1
                            num-=1
                        else:
                            print("Error")

                    context.bot.send_message(chat_id, text=f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds left on {user.name}'s mute.")
                    return
        context.bot.send_message(chat_id, text=f'{user.name} is not muted.')
    else:
        context.bot.send_message(chat_id,text='No permission.')
