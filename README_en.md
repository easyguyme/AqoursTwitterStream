# AqoursTwitterStream

This Python script is for forwarding Twitter statuses in real time to a bot in Telegram - a messaging application. By default, this script forwards Aqours' members tweets and I call it AqoursTwitterStream because the initiative was from them. If you want to forward tweets from different, make changes to the `AQOURS` variable.

Following are the Twitter accounts of Aqours members (Japanese):

* [Anju Inami](https://twitter.com/anju_inami)
* [Rikako Aida](https://twitter.com/Rikako_Aida)
* [Nanaka Suwa](https://twitter.com/suwananaka)
* [Arisa Komiya](https://twitter.com/box_komiyaarisa)
* [Shuka Saito](https://twitter.com/Saito_Shuka)
* [Aika Kobayashi](https://twitter.com/Aikyan_)
* [Kanako Takatsuki](https://twitter.com/Kanako_tktk)
* [Aina Suzuki](https://twitter.com/aina_suzuki723)
* [Ai Furihata](https://twitter.com/furihata_ai)

Features are:

1. Forward the text of a tweet with its media.
2. Forward the text of a retweet with its media.
	1. If the retweet was quoted, then the quote is also forwarded.
3. Forward a reply, and the replied text. 

## How to?

You can deploy this script on a VPS, Google App Engine, or else. Before you start using it, you must have API keys from both Telegram ("bot token") and Twitter.

### VPS

Make sure you have installed git, then run the following command. 

```
git clone https://github.com/MagaFun/AqoursTwitterStream.git
cd AqoursTwitterStream/
```

Next, paste your tokens in the file: `AqoursTwitterStream.py`. If you need the bot to send messages to a channel, put the channel name in the `CHAT_ID` variable, or you could put your personal chat ID if you wish the bot send messages to you only.

You are all good to go now, run the command:

```
pip install python-twitter
pip install python-telegram-bot
python AqoursTwitterStream.py
```

If you received a message `Script has been restarted.`, the script has been started. 

Please be informed that the script will create a file in the folder named `output.log` for error logging purpose.

## Potential Problem

* The script cannot forward the video in a reply.
* Daisy-chained retweet may not work.