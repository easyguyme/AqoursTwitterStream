> Note: I don't know what the heck is in Twitter's mind but apparently they are making a lot of changes to the APIs. The upcoming change could render this script useless. I probably won't make any further adaptations to the new APIs. 

# 推特实时转发 Telegram (CN) Scroll down for EN_US or EN_GB

本 Python 脚本可以实现将推特实时转发到 Telegram 机器人的功能。因为这个程序由 Aqours 启发，所以程序默认转发 Aqours 成员的推特更新。如果需要转发其他人的推特更新，请修改 `AQOURS` 变量。Aqours 成员推特分别为（日语）：

* [伊波杏樹](https://twitter.com/anju_inami)
* [逢田梨香子](https://twitter.com/Rikako_Aida)
* [諏訪ななか](https://twitter.com/suwananaka)
* [小宮有紗](https://twitter.com/box_komiyaarisa)
* [斉藤朱夏](https://twitter.com/Saito_Shuka)
* [小林愛香](https://twitter.com/Aikyan_)
* [高槻かなこ](https://twitter.com/Kanako_tktk)
* [鈴木愛奈](https://twitter.com/aina_suzuki723)
* [降幡愛](https://twitter.com/furihata_ai)

可以实现的功能有：

1. 转发文字推文以及附带的媒体
2. 转发转发的推文以及附带的媒体，如果媒体存在的话。
	1. 如果是引用推文的话，转发引用推文及其附带的媒体并转发引用文字。
3. 转发回复和原回复的媒体

## 怎样使用

您可以将本脚本部署到 VPS 或 Google App Engine 等平台。在使用之前您需要申请一个 Telegram 机器人以及 Twitter 应用程序。

### VPS

请先确保您的 VPS 安装了 Git 以及 Python，然后运行以下命令：

```
git clone https://github.com/MagaFun/AqoursTwitterStream.git
cd AqoursTwitterStream/
```

然后进入 `AqoursTwitterStream` 目录，在 `AqoursTwitterStream.py` 内粘贴自己的 Token，粘贴完毕后保存。

之后，您可以设定机器人向一个频道发送信息。若您想要让您刚才创建的机器人给您发送私人信息提醒推特更新的话，您需要编辑 `CHAT_ID`，您的 `CHAT_ID` 可以通过另一个机器人 [get_id_bot](https://telegram.me/get_id_bot) 来获取。

然后，直接运行如下命令：

```
pip install python-twitter
pip install python-telegram-bot
python AqoursTwitterStream.py
```

如果机器人给您发送信息`Script has been restarted.`，说明脚本启动成功。

脚本将在目录里创建 `output.log` 来记录一些日志，请您知悉。

## 问题

* 暂时无法转发回复的推文的视频
* 多层转发可能不会工作

# AqoursTwitterStream (EN_US / EN_GB)

This Python script is for forwarding Twitter statuses in real time to a bot in Telegram - a messaging application. By default, this script forwards Aqours' members tweets and I call it AqoursTwitterStream because the initiative was from them. If you want to forward tweets from different people, make changes to the `AQOURS` variable.

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
