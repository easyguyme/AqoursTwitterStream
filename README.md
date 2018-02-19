# 推特实时转发 Telegram

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