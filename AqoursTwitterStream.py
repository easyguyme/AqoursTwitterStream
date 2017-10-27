# -*- coding: utf-8 -*-

import twitter
import telegram
import json
import operator
import authconfig as cfg
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import sys # Line 9-12 make sure that the output is encoded in UTF-8

reload(sys)
sys.setdefaultencoding('utf-8')

bot = telegram.Bot(token=cfg.TELEGRAM_BOT_TOKEN)

api = twitter.Api(consumer_key=cfg.TWITTER_TOKEN['consumer_key'],
                  consumer_secret=cfg.TWITTER_TOKEN['consumer_secret'],
                  access_token_key=cfg.TWITTER_TOKEN['access_token_key'],
                  access_token_secret=cfg.TWITTER_TOKEN['access_token_secret'])

bot.send_message(chat_id=cfg.CHAT_ID, text='''Script has been restarted.''')

AQOURS = ['1393924040', '3692123006', '2598273120', '746579242431877121', '3801397033', '260986258', '4065828913', '3177547086', '3177540343', '391360956', '347849994']
mp4 = []

def getMediaForPost(line, r):
    if line['entities'].has_key('media') == True:
        if line['extended_entities']['media'][0]['type'] == 'photo': # Media type: photo
            print u'媒体是图片'
            for i in range(0, len(line['extended_entities']['media'])):
                print line['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['extended_entities']['media'][i]['media_url_https'], caption='推文图片', reply_to_message_id=r['message_id'])
        if line['extended_entities']['media'][0]['type'] == 'video': # Media type: video
            print u'媒体是视频'
            for m in range(0, len(line['extended_entities']['media'][0]['video_info']['variants'])):
                if line['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
            print max(mp4, key=operator.itemgetter('bitrate'))['url']
            bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频')
            del mp4[:]
    else:
        pass

def getMediaForRepling(line, r):
    if line['entities'].has_key('media') == True:
        if line['entities']['media'][0]['type'] == 'photo': # Media type: photo
            print u'回复媒体是图片'
            for i in range(0, len(line['extended_entities']['media'])):
                print line['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['extended_entities']['media'][i]['media_url_https'], caption='回复附带图片', reply_to_message_id=r['message_id'])
        else:
            pass
    else:
        pass

def getMediaForLongTweet(line, r):
    if line['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo': # photo
        print u'媒体是图片'
        for i in range(0, len(line['extended_tweet']['extended_entities']['media'])): 
            print line['extended_tweet']['extended_entities']['media'][i]['media_url_https']
            bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['extended_tweet']['extended_entities']['media'][i]['media_url_https'], caption='推文图片', reply_to_message_id=r['message_id'])
    if line['extended_tweet']['extended_entities']['media'][0]['type'] == 'video': # video
        print u'媒体是视频'
        for m in range(0, len(line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
                if line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
        print max(mp4, key=operator.itemgetter('bitrate'))['url']
        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频', reply_to_message_id=r['message_id'])
        del mp4[:]

def getMediaForRetweet(line, r):
    if line['retweeted_status']['entities'].has_key('media') == True: 
        if line['retweeted_status']['extended_entities']['media'][0]['type'] == 'video': 
            print u'媒体是视频'
            for m in range(0, len(line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'])):
                if line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
            print max(mp4, key=operator.itemgetter('bitrate'))['url']
            bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='原推文视频', reply_to_message_id=r['message_id'])
            del mp4[:]
        if line['retweeted_status']['extended_entities']['media'][0]['type'] == 'photo': 
            print u'媒体是图片'
            for i in range(0, len(line['retweeted_status']['extended_entities']['media'])):
                print line['retweeted_status']['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['retweeted_status']['extended_entities']['media'][i]['media_url_https'], caption='原推文图片', reply_to_message_id=r['message_id'])
    else:
        pass

def getMediaForRetweetLongTweet(line, r):
    if line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo':
        print u'媒体是图片'
        for i in range(0, len(line['retweeted_status']['extended_tweet']['extended_entities']['media'])): 
            print line['retweeted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https']
            bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['retweeted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https'], caption='原推文图片', reply_to_message_id=r['message_id'])
    if line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'video':
        print u'媒体是视频'
        for m in range(0, len(line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
            if line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                mp4.append(line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
            else:
                pass
        print max(mp4, key=operator.itemgetter('bitrate'))['url']
        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='原推文视频', reply_to_message_id=r['message_id'])
        del mp4[:]

def getMediaForQuotedTweet(line, r):
    if line['quoted_status']['entities'].has_key('media') == True:
        print u'检测到媒体'
        if line['quoted_status']['extended_entities']['media'][0]['type'] == 'photo': # 转发图片
            print u'媒体是图片'
            for i in range(0, len(line['quoted_status']['extended_entities']['media'])):
                print line['quoted_status']['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['quoted_status']['extended_entities']['media'][i]['media_url_https'], caption='原推文图片', reply_to_message_id=r['message_id'])
        if line['quoted_status']['extended_entities']['media'][0]['type'] == 'video': # 转发视频
            print u'媒体是视频'
            for m in range(0, len(line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'])):
                if line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
            print max(mp4, key=operator.itemgetter('bitrate'))['url']
            bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='原推文视频', reply_to_message_id=r['message_id'])
            del mp4[:]
    else:
        pass

def getMediaForQuotedLongTweet(line, r):
    if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo': 
        print u'媒体是图片'
        for i in range(0, len(line['quoted_status']['extended_tweet']['extended_entities']['media'])): 
            print line['quoted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https']
            bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['quoted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https'], caption='推文图片', reply_to_message_id=r['message_id'])
    if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'video': 
        print u'媒体是视频'
        for m in range(0, len(line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
            if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                mp4.append(line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
            else:
                pass
        print max(mp4, key=operator.itemgetter('bitrate'))['url']
        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频', reply_to_message_id=r['message_id'])
        del mp4[:]

def main():
    with open('output.log', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(follow=AQOURS):

            if line.has_key('delete') == True: # If deleting a tweet
                bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>检测到删推操作</b>', parse_mode="HTML")
                bot.send_message(chat_id=cfg.CHAT_ID, text=u'被删除的推特 ID 为：' + '<b>' + line['delete']['status']['id_str'] + '</b>', parse_mode="HTML")
                     
            if line.has_key('delete') == False: # Id not deleting a tweet, an update can be confirmed 
                if line['user']['id_str'] in AQOURS:
                    print u'检测到了 Aqours 成员的更新。'
                    f.write(json.dumps(line)) # log output
                    f.write('\n')
                    bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>嗨嗨嗨，醒一醒，</b><a href="https://twitter.com/{0}">{1}</a><b>推特更新了！</b>'.format(line['user']['screen_name'], line['user']['name']), parse_mode="HTML", disable_web_page_preview=True)

                    twitterUrl = 'https://twitter.com/{0}/status/{1}'.format(line['user']['screen_name'], line['id_str'])
                    button_list = [
                                [InlineKeyboardButton(u"原推文", url=twitterUrl)]
                                ]
                    reply_markup = InlineKeyboardMarkup(button_list)

                    if line['is_quote_status'] == True: 
                        print u'检测到了 Aqours 成员的转推评论。'
                        if line['quoted_status']['truncated'] == False: # 如果转推推文是短推特
                            print u'转推推文是短推文'
                            r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推并引用了如下推文：</b>\n{2}'.format(line['quoted_status']['user']['screen_name'], line['quoted_status']['user']['name'], line['quoted_status']['text']), parse_mode="HTML", disable_web_page_preview=True)
                            getMediaForQuotedTweet(line, r)
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>转推评论为：</b>\n' + line['text'], parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)
                        if line['quoted_status']['truncated'] == True: # 如果转推推文是长推特
                            print u'转推推文是长推特'
                            r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推并引用了如下推文：</b>\n{2}'.format(line['quoted_status']['user']['screen_name'], line['quoted_status']['user']['name'], line['quoted_status']['extended_tweet']['full_text']), parse_mode="HTML", disable_web_page_preview=True)
                            getMediaForQuotedLongTweet(line, r)
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>转推评论为：</b>\n' + line['text'], parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)

                    if line.has_key('retweeted_status') == True and line['is_quote_status'] == False: 
                        print u'检测到了 Aqours 成员的纯转推。'
                        if line['retweeted_status']['truncated'] == False: # 如果纯转推推文是短推特
                            r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推了如下推文：</b>\n{2}'.format(line['retweeted_status']['user']['screen_name'], line['retweeted_status']['user']['name'], line['retweeted_status']['text']), parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)
                            getMediaForRetweet(line, r)
                        if line['retweeted_status']['truncated'] == True: # 如果纯转推推文是长推特，则一定有媒体
                            r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>从</b><a href="https://twitter.com/{0}">{1}</a><b>转推了如下推文：</b>\n{2}'.format(line['retweeted_status']['user']['screen_name'], line['retweeted_status']['user']['name'], line['retweeted_status']['extended_tweet']['full_text']), parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)
                            getMediaForRetweetLongTweet(line, r)

                    if line['in_reply_to_status_id'] != None:
                        print u'检测到有回复。' 
                        r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<a href="https://twitter.com/{0}">{1}</a><b>回复了</b><a href="https://twitter.com/{2}">{3}</a>'.format(line['user']['screen_name'], line['user']['name'], api.GetUser(user_id=line['in_reply_to_user_id_str']).screen_name, api.GetUser(user_id=line['in_reply_to_user_id_str']).name), parse_mode="HTML", disable_web_page_preview=True)
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>回复：</b>\n{0}\n<b>回复的信息：</b>\n{1}'.format(line['text'], api.GetStatus(line['in_reply_to_status_id_str']).text), parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)
                        getMediaForRepling(line, r)

                    if line['truncated'] == True: 
                        print u'检测到长推文。'
                        r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>以下为推特内容</b>\n' + line['extended_tweet']['full_text'], parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)
                        getMediaForLongTweet(line, r)

                    elif line['in_reply_to_status_id'] == None and line.has_key('retweeted_status') == False and line['is_quote_status'] == False and line['truncated'] == False: # 如果不满足以上任何条件，则为原创推特，需要转发媒体。
                        print u'检测到原创更新。'
                        r = bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>以下为推特内容</b>\n' + line['text'], parse_mode="HTML", disable_web_page_preview=True, reply_markup=reply_markup)
                        getMediaForPost(line, r)

while True:
    try:
        main()
    except:
        bot.send_message(chat_id=cfg.CHAT_ID, text=u'程序可能出现网络错误，正在重启。')
        continue