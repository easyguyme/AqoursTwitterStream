# Aqours 推特实时转发 Telegram

本 Python 脚本可以实现将 Aqours 成员推特实时转发到 Telegram 机器人的功能。Aqours 成员推特分别为（日语）：

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
	2. 如果是引用推文的话，转发引用推文及其附带的媒体并转发引用文字。
3. 转发回复

## 怎样使用

您可以将本脚本部署到 VPS 或 Google App Engine 等平台。在使用之前您需要申请一个 Telegram 机器人以及 Twitter 应用程序。您同样也可以直接在 Telegram 上关注频道 [Aqours 推特 / 新闻快速报](https://t.me/AqoursTwitter)。

### VPS

请先确保您的 VPS 安装了 Git 以及 Python 2.6，然后运行以下命令：

`git clone https://github.com/MagaFun/AqoursTwitterStream.git
`

然后进入目录，在 `authconfig.py` 内粘贴自己的 Token，粘贴完毕后保存。

之后，若您想要让您刚才创建的机器人给您发送私人信息提醒 Aqours 成员推特更新的话，您需要编辑 `CHAT_ID`，您的 `CHAT_ID` 可以通过另一个机器人 [get_id_bot](https://telegram.me/get_id_bot) 来获取。

之后直接运行如下命令：

`python AqoursTwitterStream.py`

如果机器人给您发送信息`程序已启动。`，说明脚本启动成功。

脚本将在目录里创建 `output.log` 来记录一些日志，请您知悉。

## 问题

* 暂时无法转发回复的推文的视频
* 多层转发可能不会工作