import sys
sys.path.insert(1, 'C:/Users/g7liang/Documents/')

import os
import re
import slack

EXAMPLE_COMMAND = "do"  # sample command
MENTION_REGEX = "^<@([WU].+)>(.*)"  # RegEx for parsing command

slack_token = "xoxb-976204110500-964989095122-MEoTMwR8CQ1TkwG1J9F4aKoG"

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']

    # uncomment if you want to see metadata of all messages
    # print(data)

    if 'text' in data:  # some text is present, let's parse it
        msg_txt = data['text']

        # uncomment if you want to see text of all messages
        print(msg_txt)

        is_the_message_for_me, cmd = parse_message(msg_txt)

        if is_the_message_for_me:
            channel_id = data['channel']
            thread = data['ts']
            user = data['user']

            webclient = payload['web_client']
            webclient.chat_postMessage(
                channel=channel_id,
                text=msg_txt,
                thread=thread
            )


def parse_message(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the tuple [True, text of the command]
        If there is no direct mention, returns [False, None]
    """
    matches = re.search(MENTION_REGEX, message_text)
    if matches and matches.group(1) == my_user_id:
        return True, matches.group(2).strip()
    else:
        return False, None

def get_my_user_id(slack_api_token):
    """
    Get bot user id as per https://api.slack.com/methods/auth.test
    """
    return slack.WebClient(slack_token).auth_test()['user_id']


# get user id of the bot
my_user_id = get_my_user_id(slack_token)

# start the bot
rtmclient = slack.RTMClient(token=slack_token)
rtmclient.start()
