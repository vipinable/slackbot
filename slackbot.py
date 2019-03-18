#!/usr/bin/env python
import os
import time
import re
from slackclient import SlackClient

# instantiate Slack client
sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# bot's user ID in Slack: value is assigned after the bot starts up
sbot_id = None

RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


if __name__ == "__main__":

  if sc.rtm_connect(with_team_state=False):
    # Read bot's user ID by calling Web API method `auth.test`
    sbot_id = sc.api_call("auth.test")["user_id"]
    print('User '+ sbot_id + ' bot connected and running!')
    mention = re.compile(MENTION_REGEX)
    while sc.server.connected is True:
      for event in sc.rtm_read():
        print event
        if 'type' in event and event['type'] == 'message':
          print event['text']
          if mention.match(event['text']):
            sc.rtm_send_message(event['channel'], 'Hi, How are you?')
          
      time.sleep(RTM_READ_DELAY)
  else:
    print 'Slack connection failed'
