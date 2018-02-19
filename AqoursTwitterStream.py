import telegram
import json
import operator
import twitter
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TELEGRAM_BOT_TOKEN = '538987372:AAFvqLnqUR6xRLgmMwqh2NN6JOY0zaKGHaU'  # 在引号中粘贴你的 Telegram 机器人 token / Paste your Telegram bot Token in the quotation marks.
TWITTER_TOKEN = {  # 在引号中粘贴你的 Twitter 应用程序授权码 / Paste your Twitter tokens in the quotation marks
    'consumer_key': 'OXxYD5wm8eVcutLrvJy94zbeD',
    'consumer_secret': '5KlgiHnZjPkwAxP3mbNw32TFLdZuaghrdUwXo10Gvc024rWZEu',
    'access_token_key': '391360956-Ah73hyt6pXIeYjQV1J4tF8mJKQDVjH8GiKeB7OVU',
    'access_token_secret': 'XJxosBOUdQVMqsEZSwKBVaZEDIfeE19lGGMnJ0jA4v0tq'}
CHAT_ID = '158754719'  # 在引号中粘贴你的 chat_id 或频道名称 / Paste your chat_id or channel name in the quotation marks.

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

api = twitter.Api(consumer_key=TWITTER_TOKEN['consumer_key'],
                  consumer_secret=TWITTER_TOKEN['consumer_secret'],
                  access_token_key=TWITTER_TOKEN['access_token_key'],
                  access_token_secret=TWITTER_TOKEN['access_token_secret'])

bot.send_message(chat_id=CHAT_ID, text='''Script has been restarted.''')

AQOURS = ['1393924040', '3692123006', '2598273120', '746579242431877121', '3801397033', '260986258', '4065828913',
          '3177547086', '3177540343', '391360956', '347849994']
mp4 = []


class getMedia:

    @staticmethod
    def tweet(tweettype, line, r):
        if tweettype == 'short':
            if 'media' in line['entities'] == True:
                if line['extended_entities']['media'][0]['type'] == 'photo':  # Media type: photo
                    print('媒体是图片')
                for i in range(0, len(line['extended_entities']['media'])):
                    print(line['extended_entities']['media'][i]['media_url_https'])
                    bot.send_photo(chat_id=CHAT_ID, photo=line['extended_entities']['media'][i][
                                                              'media_url_https'] + '?format=jpg&name=orig',
                                   caption='推文图片', reply_to_message_id=r['message_id'])
                if line['extended_entities']['media'][0]['type'] == 'video':  # Media type: video
                    print('媒体是视频')
                    for m in range(0, len(line['extended_entities']['media'][0]['video_info']['variants'])):
                        if line['extended_entities']['media'][0]['video_info']['variants'][m][
                            'content_type'] == 'video/mp4':
                            mp4.append(line['extended_entities']['media'][0]['video_info']['variants'][m])
                        else:
                            pass
                print(max(mp4, key=operator.itemgetter('bitrate'))['url'])
                bot.send_video(chat_id=CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']),
                               caption='推文视频', reply_to_message_id=r['message_id'])
                del mp4[:]
            else:
                pass
        if tweettype == 'long':
            if 'extended_entities' in line['extended_tweet']:
                if line['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo':  # photo
                    print('媒体是图片')
                    for i in range(0, len(line['extended_tweet']['extended_entities']['media'])):
                        print(line['extended_tweet']['extended_entities']['media'][i]['media_url_https'])
                        bot.send_photo(chat_id=CHAT_ID,
                                       photo=line['extended_tweet']['extended_entities']['media'][i][
                                                 'media_url_https'] + '?format=jpg&name=orig', caption='推文图片',
                                       reply_to_message_id=r['message_id'])
                if line['extended_tweet']['extended_entities']['media'][0]['type'] == 'video':  # video
                    print('媒体是视频')
                    for m in range(0, len(
                            line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
                        if line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m][
                            'content_type'] == 'video/mp4':
                            mp4.append(
                                line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
                        else:
                            pass
                    print(max(mp4, key=operator.itemgetter('bitrate'))['url'])
                    bot.send_video(chat_id=CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']),
                                   caption='推文视频', reply_to_message_id=r['message_id'])
                    del mp4[:]
            else:
                pass

    @staticmethod
    def retweet(line, r):
        if 'media' in line['retweeted_status']['entities']:
            if line['retweeted_status']['extended_entities']['media'][0]['type'] == 'video':
                print('媒体是视频')
                for m in range(0, len(
                        line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'])):
                    if line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'][m][
                        'content_type'] == 'video/mp4':
                        mp4.append(
                            line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'][m])
                    else:
                        pass
                print(max(mp4, key=operator.itemgetter('bitrate'))['url'])
                bot.send_video(chat_id=CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']),
                               caption='原推文视频', reply_to_message_id=r['message_id'])
                del mp4[:]
            if line['retweeted_status']['extended_entities']['media'][0]['type'] == 'photo':
                print('媒体是图片')
                for i in range(0, len(line['retweeted_status']['extended_entities']['media'])):
                    print(line['retweeted_status']['extended_entities']['media'][i]['media_url_https'])
                    bot.send_photo(chat_id=CHAT_ID, photo=line['retweeted_status']['extended_entities']['media'][i][
                                                              'media_url_https'] + '?format=jpg&name=orig',
                                   caption='原推文图片', reply_to_message_id=r['message_id'])
        else:
            pass

    @staticmethod
    def quote(tweettype, line, r):
        if tweettype == 'short':
            if 'media' in line['quoted_status']['entities']:
                print('检测到媒体')
                if line['quoted_status']['extended_entities']['media'][0]['type'] == 'photo':  # 转发图片
                    print('媒体是图片')
                    for i in range(0, len(line['quoted_status']['extended_entities']['media'])):
                        print(line['quoted_status']['extended_entities']['media'][i]['media_url_https'])
                        bot.send_photo(chat_id=CHAT_ID,
                                       photo=line['quoted_status']['extended_entities']['media'][i][
                                                 'media_url_https'] + '?format=jpg&name=orig', caption='原推文图片',
                                       reply_to_message_id=r['message_id'])
                if line['quoted_status']['extended_entities']['media'][0]['type'] == 'video':  # 转发视频
                    print('媒体是视频')
                    for m in range(0, len(
                            line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'])):
                        if line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'][m][
                            'content_type'] == 'video/mp4':
                            mp4.append(
                                line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'][m])
                        else:
                            pass
                    print(max(mp4, key=operator.itemgetter('bitrate'))['url'])
                    bot.send_video(chat_id=CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']),
                                   caption='原推文视频', reply_to_message_id=r['message_id'])
                    del mp4[:]
            else:
                pass
        if tweettype == 'long':
            if 'extended_entities' in line['quoted_status']['extended_tweet']:
                if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo':
                    print('媒体是图片')
                    for i in range(0, len(line['quoted_status']['extended_tweet']['extended_entities']['media'])):
                        print(
                            line['quoted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https'])
                        bot.send_photo(chat_id=CHAT_ID,
                                       photo=line['quoted_status']['extended_tweet']['extended_entities']['media'][i][
                                                 'media_url_https'] + '?format=jpg&name=orig', caption='推文图片',
                                       reply_to_message_id=r['message_id'])
                if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'video':
                    print('媒体是视频')
                    for m in range(0, len(
                            line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info'][
                                'variants'])):
                        if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                            mp4.append(
                                line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info'][
                                    'variants'][m])
                        else:
                            pass
                    print(max(mp4, key=operator.itemgetter('bitrate'))['url'])
                    bot.send_video(chat_id=CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']),
                                   caption='推文视频', reply_to_message_id=r['message_id'])
                    del mp4[:]
            else:
                pass

    @staticmethod
    def reply(line, r):
        if 'media' in line['entities']:
            if line['entities']['media'][0]['type'] == 'photo':  # Media type: photo
                print('回复媒体是图片')
                for i in range(0, len(line['extended_entities']['media'])):
                    print(line['extended_entities']['media'][i]['media_url_https'])
                    bot.send_photo(chat_id=CHAT_ID, photo=line['extended_entities']['media'][i][
                                                              'media_url_https'] + '?format=jpg&name=orig',
                                   caption='回复附带图片', reply_to_message_id=r['message_id'])
            else:
                pass
        else:
            pass


def main():
    with open('output.log', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(follow=AQOURS):

            if 'delete' in line:  # If deleting a tweet
                bot.send_message(chat_id=CHAT_ID, text='<b>检测到删推操作</b>', parse_mode="HTML")
                bot.send_message(chat_id=CHAT_ID,
                                 text='被删除的推特 ID 为：' + '<b>' + line['delete']['status']['id_str'] + '</b>',
                                 parse_mode="HTML")

            if 'delete' not in line:  # If not deleting a tweet, an update can be confirmed
                if line['user']['id_str'] in AQOURS:
                    print('检测到了 Aqours 成员的更新。')
                    f.write(json.dumps(line))  # log output
                    f.write('\n')
                    bot.send_message(chat_id=CHAT_ID,
                                     text='<b>嗨嗨嗨，醒一醒，</b><a href="https://twitter.com/{0}">{1}</a><b>推特更新了！</b>'.format(
                                         line['user']['screen_name'], line['user']['name']),
                                     parse_mode="HTML",
                                     disable_web_page_preview=True
                                     )

                    twitterUrl = 'https://twitter.com/{0}/status/{1}'.format(line['user']['screen_name'],
                                                                             line['id_str'])
                    button_list = [
                        [InlineKeyboardButton("原推文", url=twitterUrl)]
                    ]
                    reply_markup = InlineKeyboardMarkup(button_list)

                    if line['is_quote_status']:
                        print('检测到了 Aqours 成员的转推评论。')
                        if not line['quoted_status']['truncated']:  # 如果转推推文是短推特
                            print('转推推文是短推文')
                            r = bot.send_message(chat_id=CHAT_ID,
                                                 text='<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推并引用了如下推文：</b>\n{2}'.format(
                                                     line['quoted_status']['user']['screen_name'],
                                                     line['quoted_status']['user']['name'],
                                                     line['quoted_status']['text']),
                                                 parse_mode="HTML",
                                                 disable_web_page_preview=True)
                            getMedia.quote(line=line, r=r)
                            bot.send_message(chat_id=CHAT_ID, text='<b>转推评论为：</b>\n' + line['text'],
                                             parse_mode="HTML", disable_web_page_preview=True,
                                             reply_markup=reply_markup)
                        if line['quoted_status']['truncated']:  # 如果转推推文是长推特
                            print('转推推文是长推特')
                            r = bot.send_message(chat_id=CHAT_ID,
                                                 text='<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推并引用了如下推文：</b>\n{2}'.format(
                                                     line['quoted_status']['user']['screen_name'],
                                                     line['quoted_status']['user']['name'],
                                                     line['quoted_status']['extended_tweet']['full_text']),
                                                 parse_mode="HTML",
                                                 disable_web_page_preview=True)
                            getMedia.quote(line=line, r=r)
                            bot.send_message(chat_id=CHAT_ID, text='<b>转推评论为：</b>\n' + line['text'],
                                             parse_mode="HTML", disable_web_page_preview=True,
                                             reply_markup=reply_markup)

                    if 'retweeted_status' in line and not line['is_quote_status']:
                        print('检测到了 Aqours 成员的纯转推。')
                        if not line['retweeted_status']['truncated']:  # 如果纯转推推文是短推特
                            r = bot.send_message(chat_id=CHAT_ID,
                                                 text='<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推了如下推文：</b>\n{2}'.format(
                                                     line['retweeted_status']['user']['screen_name'],
                                                     line['retweeted_status']['user']['name'],
                                                     line['retweeted_status']['text']),
                                                 parse_mode="HTML",
                                                 disable_web_page_preview=True,
                                                 reply_markup=reply_markup)
                            getMedia.retweet(line=line, r=r)
                        if line['retweeted_status']['truncated'] == True:  # 如果纯转推推文是长推特，则一定有媒体
                            r = bot.send_message(chat_id=CHAT_ID,
                                                 text='<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推了如下推文：</b>\n{2}'.format(
                                                     line['retweeted_status']['user']['screen_name'],
                                                     line['retweeted_status']['user']['name'],
                                                     line['retweeted_status']['extended_tweet']['full_text']),
                                                 parse_mode="HTML",
                                                 disable_web_page_preview=True,
                                                 reply_markup=reply_markup)
                            getMedia.retweet(line=line, r=r)

                    if line['in_reply_to_status_id'] != None:
                        print('检测到有回复。')
                        r = bot.send_message(chat_id=CHAT_ID,
                                             text='<a href="https://twitter.com/{0}">{1}</a><b>回复了</b><a href="https://twitter.com/{2}">{3}</a>'.format(
                                                 line['user']['screen_name'], line['user']['name'],
                                                 api.GetUser(user_id=line['in_reply_to_user_id_str']).screen_name,
                                                 api.GetUser(user_id=line['in_reply_to_user_id_str']).name),
                                             parse_mode="HTML",
                                             disable_web_page_preview=True)
                        bot.send_message(chat_id=CHAT_ID,
                                         text='<b>回复：</b>\n{0}\n<b>回复的信息：</b>\n{1}'.format(line['text'], api.GetStatus(
                                             line['in_reply_to_status_id_str']).text), parse_mode="HTML",
                                         disable_web_page_preview=True, reply_markup=reply_markup)
                        getMedia.reply(r=r)

                    if line['truncated']:
                        print('检测到长推文。')
                        r = bot.send_message(chat_id=CHAT_ID,
                                             text='<b>以下为推特内容</b>\n' + line['extended_tweet']['full_text'],
                                             parse_mode="HTML",
                                             disable_web_page_preview=True,
                                             reply_markup=reply_markup)
                        getMedia.tweet(tweettype='long', line=line, r=r)

                    else:  # 如果不满足以上任何条件，则为原创推特，需要转发媒体。
                        print('检测到原创更新。')
                        r = bot.send_message(chat_id=CHAT_ID,
                                             text='<b>以下为推特内容</b>\n' + line['text'],
                                             parse_mode="HTML",
                                             disable_web_page_preview=True,
                                             reply_markup=reply_markup)
                        getMedia.tweet(tweettype='short', line=line, r=r)


main()
