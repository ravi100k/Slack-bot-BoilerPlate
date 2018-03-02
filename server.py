from flask import Flask, request, make_response
import os, json

from slackclient import SlackClient

# Your app's Slack bot user token
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]

"""
    SLACK_BOT_TOKEN = xoxp-xxxxxxxxx-xxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
    SLACK_VERIFICATION_TOKEN = xoxb-xxxxxxxxx-xxxxxxxxxxxxx
"""
# Slack client for Web API requests
slack_client = SlackClient(SLACK_VERIFICATION_TOKEN)

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)

# Post a message to a channel, asking users if they want to play a game
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to simple python slack bot stater kit......'

@app.route('/slack/events', methods=['POST'])
def events():
    slack_event = json.loads(request.data)
    print (slack_event)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":"application/json"})
    else:
        if 'bot_message' not in slack_event['event'] and 'user' in slack_event['event']:
            user_text = slack_event['event']['text']
            user_channel = slack_event['event']['channel']
            # User logic to send response to slack bot

            message_text = ':horse:'
            # User logic to send response to slack bot
            slack_client.api_call("chat.postMessage",channel=user_channel,text=message_text,as_user=False)
            return make_response("OK", 200, {"content_type":"application/json"})

        else:
            return make_response("OK", 200, {"X-Slack-No-Retry": 1})


if __name__ == "__main__":
    app.run(debug=True)
