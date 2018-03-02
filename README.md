# pythOnBoarding Bot

After you've cloned this repository locally, you'll want to create a virtual
environment to keep the dependencies for this project isolated from any other
project you may be working on.

If you're using `virtualenv` run the following commands from the root of your
project directory:

```bash
virtualenv env
```

Then activate your new virtual environment:

```bash
source env/bin/activate
```

After that, you can install all the Python packages this project will need with
this command:

```bash
pip install -r requirements.txt
```

###### Server Requirements

Slack will be delivering events to your app's server so your server needs to be able to receive incoming HTTPS traffic from Slack.

If you are running this project locally, you'll need to set up tunnels for Slack to connect to your endpoints. [Ngrok](https://ngrok.com/) is an easy to use tunneling tool that supports HTTPS, which is required by Slack.

You'll likely want to test events coming to your server without going through the actions on your Slack team.  [Postman](https://www.getpostman.com/) is a useful tool you can use to recreate requests sent from Slack to your server. This is especially helpful for events like user join, where the workflow to recreate the event requires quite a bit of set up.

## Let's get started :tada:
* **[Section 1: Build This Bot]
* [First home route to display your home page]
* [Second slack/events to handle the request comming from slack server]
* [Event Sucribe is im.message](for further development you can add more event and api calls to handle differnts request.)

## Further Reading and Getting Help

### Documentation

##### Slack Documentation
* [Getting started with Slack apps](https://api.slack.com/slack-apps)  
* [Slack Events API documentation](https://api.slack.com/events)  
* [Slack Web API documentation](https://api.slack.com/web)

##### Documentation for Tools
* [virtualenv](https://virtualenv.pypa.io/en/latest/userguide/)
* [flask](http://flask.pocoo.org/)
* [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/)
* [ngrok](https://ngrok.com/docs)
* [postman](https://www.getpostman.com/docs/)

### Where to Find Help

Wondering what to do if you can't get this dang tutorial to work for you?
The Slack Developer community is an awesome place to get help when you're confused
or stuck. We have an excellent 'search first' culture and Slack is committed to
improving our tutorials and documentation based on your feedback. If you've
checked the [Slack API documentation](https://api.slack.com/), reached the end
of your google patience and found [StackOverflow](http://stackoverflow.com/questions/tagged/slack-api)
to be unhelpful, try asking for help in the [Dev4Slack](http://dev4slack.xoxco.com/)
Slack team.
