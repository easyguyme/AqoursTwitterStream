# -*- coding: utf-8 -*-

import twitter
import telegram
import json
import operator
import authconfig as cfg
import sys # 8-11 行是保证系统使用 UTF-8 编码做输出检查，不需要的话可以注释掉。

reload(sys)
sys.setdefaultencoding('utf-8')

bot = telegram.Bot(token=cfg.TELEGRAM_BOT_TOKEN)

api = twitter.Api(consumer_key=cfg.TWITTER_TOKEN['consumer_key'],
                  consumer_secret=cfg.TWITTER_TOKEN['consumer_secret'],
                  access_token_key=cfg.TWITTER_TOKEN['access_token_key'],
                  access_token_secret=cfg.TWITTER_TOKEN['access_token_secret'])

bot.send_message(chat_id=cfg.CHAT_ID, text='''程序已重启。''')

AQOURS = ['1393924040', '3692123006', '2598273120', '746579242431877121', '3801397033', '260986258', '4065828913', '3177547086', '3177540343', '391360956', '347849994']
mp4 = [] # 定义一个列表来筛选最高质量的视频

def getMediaForPost(line):
    if line['entities'].has_key('media') == True: # 没有媒体（媒体获取模块在此开始）
        if line['entities']['media'][0]['type'] == 'photo': # 媒体为图片
            print u'媒体是图片'
            for i in range(0, len(line['extended_entities']['media'])):
                print line['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['extended_entities']['media'][i]['media_url_https'], caption='推文图片')
        elif line['extended_entities']['media'][0]['type'] == 'video': # 媒体为视频
            print u'媒体是视频'
            for m in range(0, len(line['extended_entities']['media'][0]['video_info']['variants'])):
                if line['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
            print max(mp4, key=operator.itemgetter('bitrate'))['url']
            bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频')
            del mp4[:]
    else: # 有媒体
        pass

def getMediaForRepling(line):
    if line['entities'].has_key('media') == True:
        if line['entities']['media'][0]['type'] == 'photo': # 媒体为图片
            print u'回复媒体是图片'
            for i in range(0, len(line['extended_entities']['media'])):
                print line['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['extended_entities']['media'][i]['media_url_https'], caption='回复附带图片')
        else:
            pass
    else:
        pass

def getMediaForLongTweet(line):
    if line['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo': # 转发图片
        print u'媒体是图片'
        for i in range(0, len(line['extended_tweet']['extended_entities']['media'])): 
            print line['extended_tweet']['extended_entities']['media'][i]['media_url_https']
            bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['extended_tweet']['extended_entities']['media'][i]['media_url_https'], caption='推文图片')
    elif line['extended_tweet']['extended_entities']['media'][0]['type'] == 'video': # 转发视频
        print u'媒体是视频'
        for m in range(0, len(line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
                if line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
        print max(mp4, key=operator.itemgetter('bitrate'))['url']
        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频')
        del mp4[:]

def getMediaForRetweet(line):
    if line['retweeted_status']['entities'].has_key('media') == True: # 如果转推的推文有媒体（Todo：获得媒体模块可以简化）
        if line['retweeted_status']['extended_entities']['media'][0]['type'] == 'video': # 如果媒体是视频
            print u'媒体是视频'
            for m in range(0, len(line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'])):
                if line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['retweeted_status']['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
            print max(mp4, key=operator.itemgetter('bitrate'))['url']
            bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='原推文视频')
            del mp4[:]
    
        elif line['retweeted_status']['entities']['media'][0]['type'] == 'photo': # 如果媒体是图片
            print u'媒体是图片'
            for i in range(0, len(line['retweeted_status']['extended_entities']['media'])):
                print line['retweeted_status']['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['retweeted_status']['extended_entities']['media'][i]['media_url_https'], caption='原推文图片')
    else: # 如果没有媒体
        pass

def getMediaForRetweetLongTweet(line):
    if line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo': # 转发图片
        print u'媒体是图片'
        for i in range(0, len(line['retweeted_status']['extended_tweet']['extended_entities']['media'])): 
            print line['retweeted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https']
            bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['retweeted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https'], caption='原推文媒体')
    if line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'video': # 转发视频
        print u'媒体是视频'
        for m in range(0, len(line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
            if line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                mp4.append(line['retweeted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
            else:
                pass
        print max(mp4, key=operator.itemgetter('bitrate'))['url']
        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='原推文媒体')
        del mp4[:]

def getMediaForQuotedTweet(line):
    if line['quoted_status']['entities'].has_key('media') == True: # 检查原推文是否有媒体，短推特不一定有媒体
        print u'检测到媒体'
        if line['quoted_status']['extended_entities']['media'][0]['type'] == 'photo':
            print u'媒体是图片'
            for i in range(0, len(line['quoted_status']['extended_entities']['media'])):
                print line['quoted_status']['extended_entities']['media'][i]['media_url_https']
                bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['quoted_status']['extended_entities']['media'][i]['media_url_https'], caption='原推特图片')# 转发图片
        elif line['quoted_status']['extended_entities']['media'][0]['type'] == 'video': # 转发视频
            print u'媒体是视频'
            for m in range(0, len(line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'])):
                if line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                    mp4.append(line['quoted_status']['extended_entities']['media'][0]['video_info']['variants'][m])
                else:
                    pass
            print max(mp4, key=operator.itemgetter('bitrate'))['url']
            bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频')
            del mp4[:]
    else:
        pass

def getMediaForQuotedLongTweet(line):
    if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'photo': # 转发图片
        print u'媒体是图片'
        for i in range(0, len(line['quoted_status']['extended_tweet']['extended_entities']['media'])): 
            print line['quoted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https']
            bot.send_photo(chat_id=cfg.CHAT_ID, photo=line['quoted_status']['extended_tweet']['extended_entities']['media'][i]['media_url_https'], caption='推文图片')
    elif line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['type'] == 'video': # 转发视频
        print u'媒体是视频'
        for m in range(0, len(line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'])):
            if line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                mp4.append(line['quoted_status']['extended_tweet']['extended_entities']['media'][0]['video_info']['variants'][m])
            else:
                pass
        print max(mp4, key=operator.itemgetter('bitrate'))['url']
        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']), caption='推文视频')
        del mp4[:]

def main():
    with open('output.log', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(follow=AQOURS):

            if line.has_key('delete') == True: # 如果是删推操作
                bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>检测到删推操作。</b>', parse_mode="HTML")
                bot.send_message(chat_id=cfg.CHAT_ID, text=u'被删除的推特 ID 为：' + '<b>' + line['delete']['status']['id_str'] + '</b>', parse_mode="HTML")
                     
            if line.has_key('delete') == False: # 如果不是删推操作，则确认有推特内容更新。
                if line['user']['id_str'] in AQOURS:
                    print u'检测到了 Aqours 成员的更新。'
                    f.write(json.dumps(line)) # 输出一个 log 文件
                    f.write('\n')
                    bot.send_message(chat_id=cfg.CHAT_ID, text=u'''嗨嗨嗨，醒一醒，<a href="https://twitter.com/{0}">{1}</a>推特更新了！'''.format(line['user']['screen_name'], line['user']['name']), parse_mode="HTML", disable_web_page_preview=True)

                    if line['is_quote_status'] == True: # 如果有转推评论，转发原推特媒体
                        print u'检测到了 Aqours 成员的转推评论。'
                        if line['quoted_status']['truncated'] == False: # 如果转推推文是短推特
                            print u'转推推文是短推文'
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'从<a href="https://twitter.com/{0}">{1}</a>转推并引用了如下推文：\n{2}'.format(line['quoted_status']['user']['screen_name'], line['quoted_status']['user']['name'], line['quoted_status']['text']), parse_mode="HTML", disable_web_page_preview=True)
                            getMediaForQuotedTweet(line)
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>转推评论为：</b>\n' + line['text'], parse_mode="HTML", disable_web_page_preview=True)
                        if line['quoted_status']['truncated'] == True: # 如果转推推文是长推特
                            print u'转推推文是长推特'
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'从<a href="https://twitter.com/{0}">{1}</a>转推并引用了如下推文：\n{2}'.format(line['quoted_status']['user']['screen_name'], line['quoted_status']['user']['name'], line['quoted_status']['extended_tweet']['full_text']), parse_mode="HTML", disable_web_page_preview=True)
                            getMediaForQuotedLongTweet(line)
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>转推评论为：</b>\n' + line['text'], parse_mode="HTML", disable_web_page_preview=True)

                    if line.has_key('retweeted_status') == True and line['is_quote_status'] == False: # 如果是纯转推，转发媒体
                        print u'检测到了 Aqours 成员的纯转推。'
                        if line['retweeted_status']['truncated'] == False: # 如果纯转推推文是短推特
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'从<a href="https://twitter.com/{0}">{1}</a>转推了如下推文：\n{2}'.format(line['retweeted_status']['user']['screen_name'], line['retweeted_status']['user']['name'], line['retweeted_status']['text']), parse_mode="HTML", disable_web_page_preview=True)
                            getMediaForRetweet(line)
                        if line['retweeted_status']['truncated'] == True: # 如果纯转推推文是长推特，则一定有媒体
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'从<a href="https://twitter.com/{0}">{1}</a>转推了如下推文：\n{2}'.format(line['retweeted_status']['user']['screen_name'], line['retweeted_status']['user']['name'], line['retweeted_status']['extended_tweet']['full_text']), parse_mode="HTML", disable_web_page_preview=True)
                            getMediaForRetweetLongTweet(line)

                    if line['in_reply_to_status_id'] != None: # 如果是回复，暂时不转发媒体
                        print u'检测到有回复。' 
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'<a href="https://twitter.com/{0}">{1}</a>回复了<a href="https://twitter.com/{2}">{3}</a>'.format(line['user']['screen_name'], line['user']['name'], api.GetUser(user_id=line['in_reply_to_user_id_str']).screen_name, api.GetUser(user_id=line['in_reply_to_user_id_str']).name), parse_mode="HTML", disable_web_page_preview=True)
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>回复：</b>\n{0}\n<b>回复的信息：</b>\n{1}'.format(line['text'], api.GetStatus(line['in_reply_to_status_id_str']).text), parse_mode="HTML", disable_web_page_preview=True)
                        getMediaForRepling()

                    if line['truncated'] == True: # 检测到长推文，长推文一定会有媒体，则转发。
                        print u'检测到长推文。'
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'''<b>以下为推特内容</b>\n''' + line['extended_tweet']['full_text'], parse_mode="HTML", disable_web_page_preview=True)
                        getMediaForLongTweet(line)

                    elif line['in_reply_to_status_id'] == None and line.has_key('retweeted_status') == False and line['is_quote_status'] == False and line['truncated'] == False: # 如果不是转推也不是回复也不是引用推特，则为原创推特，需要转发媒体。
                        print u'检测到原创更新。'
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'''<b>以下为推特内容</b>\n''' + line['text'], parse_mode="HTML", disable_web_page_preview=True)
                        getMediaForPost(line) 
while True:
    try:
        main()
    except:
        bot.send_message(chat_id=cfg.CHAT_ID, text=u'''程序可能出现网络错误，正在重启。''')
        continue