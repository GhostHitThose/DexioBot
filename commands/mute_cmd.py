import time
import traceback

LOCATION = './commands/database/mutes.txt'


def run(chat_id, update, context):
    file = open(LOCATION, 'r')
    lines = file.readlines()

    # command example: /mute (user) (time length)
    user_status = context.bot.get_chat_member(chat_id, update.message.from_user.id)['status']
    try:
        mute_user = context.args[0]
    except:
        context.bot.send_message(chat_id=chat_id, text="No user given.")
        return

    try:
        mute_user = context.bot.get_chat_member(chat_id, mute_user)
        mute_user_status = mute_user['status']
    except:
        context.bot.send_message(chat_id=chat_id, text="User not found.")
        return

    try:
        time_muted_for = get_time_unmuted(context.args[1])
    except:
        time_muted_for = -1

    if mute_user_status == "administrator" or mute_user_status == "creator":
        context.bot.send_message(chat_id=chat_id, text='The user you are attempting to mute is an administrator.')
        return

    if user_status == "administrator" or user_status == "creator":
        if isMuted(mute_user['user'], context, update, chat_id):
            pass
        else:
            # Mute.txt format:    user:time_muted
            update_file = open(LOCATION, 'a')
            update_file.write(str(mute_user['user']['id']))
            update_file.write(":" + str(time_muted_for) + '\n')

    else:
        context.bot.send_message(chat_id=chat_id, text='No permission.')

def isMuted(user, context, update, chat_id):
    file = open(LOCATION, 'r')
    lines = file.readlines()
    for line in lines:
        user_id, time_um = line.split(':')
        user_id = int(user_id)
        user_status = context.bot.get_chat_member(chat_id, update.message.from_user.id)['status']
        if user_status == "administrator" or user_status == "creator":
            line_index = lines.index(line)
            del lines[line_index]

            new_file = open(LOCATION, "w+")

            for new_line in lines:
                new_file.write(new_line)

            new_file.close()
            return False
        time_um = float(time_um[:-1])
        if user.id == user_id:
            if time_um == -1:
                return True
            elif (time.time_ns()/1000000000)-float(time_um) < 0:
                return True
            else:
                line_index = lines.index(line)
                del lines[line_index]

                new_file = open(LOCATION, "w+")

                for new_line in lines:
                    new_file.write(new_line)

                new_file.close()
                return False
        else:
            pass

    return False

def delete_message(chat_id, update, context):
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)

def get_time_unmuted(time_muted):
    now = time.time_ns()/1000000000
    return now + int(time_muted)
