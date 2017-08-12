# -*- coding: utf-8 -*-

import twitter
import telegram
import json
import operator
import authconfig as cfg

bot = telegram.Bot(token=cfg.TELEGRAM_BOT_TOKEN)

api = twitter.Api(consumer_key=cfg.TWITTER_TOKEN['consumer_key'],
                  consumer_secret=cfg.TWITTER_TOKEN['consumer_secret'],
                  access_token_key=cfg.TWITTER_TOKEN['access_token_key'],
                  access_token_secret=cfg.TWITTER_TOKEN['access_token_secret'])

bot.send_message(chat_id=cfg.CHAT_ID, text='''程序已启动。''', parse_mode="HTML")

AQOURS = ['1393924040', '3692123006', '2598273120', '746579242431877121', '3801397033', '260986258', '4065828913', '3177547086', '3177540343', '391360956']
mp4 = [] # 定义一个列表来筛选最高质量的视频

def main():
    with open('output.log', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(follow=AQOURS):
            print u'检测到其他人转推或评论 Aqours 成员的更新。程序将忽略但写入 output.log 中'
            f.write(json.dumps(line)) # 输出一个 log 文件
            f.write('\n')

            if line.has_key('delete') == True: # 如果是删推操作
                bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>检测到删推操作。</b>', parse_mode="HTML")
                bot.send_message(chat_id=cfg.CHAT_ID, text=u'被删除的推特 ID 为：' + '<b>' + line['delete']['status']['id_str'] + '</b>', parse_mode="HTML")
                     
            if line.has_key('delete') == False: # 如果不是删推操作，则确认有推特内容更新。
                if line['user']['id_str'] in AQOURS:
                    print u'检测Aqours 成员的更新。'
                    bot.send_message(chat_id=cfg.CHAT_ID, text=u'嗨嗨嗨，醒一醒，'+ line['user']['name'] + u'推特更新了！', parse_mode="HTML")
 
                    if line.has_key('retweeted_status') == True: # 如果是转推
                        if line['is_quote_status'] == False: # 纯转推，需要转发媒体
                            bot.send_message(chat_id=cfg.CHAT_ID, text=u'从<b>' + line['retweeted_status']['user']['name'] + u'</b>转推了如下推文：\n' + line['retweeted_status']['text'], parse_mode="HTML")
                            if line['retweeted_status']['entities'].has_key('media') == True: # 如果转推的推文有媒体（Todo：获得媒体模块可以简化）
                                if line['extended_entities']['media'][0]['type'] == 'video': # 如果媒体是视频
                                    for m in range(0, len(line['extended_entities']['media'][0]['video_info']['variants'])):
                                        if line['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                                            mp4.append(line['extended_entities']['media'][0]['video_info']['variants'][m])
                                        else:
                                            pass
                                    print max(mp4, key=operator.itemgetter('bitrate'))['url']
                                    try:
                                        bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']))
                                        del mp4[:]
                                    except:
                                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'Failed to get content, this is possibly due to a timeout error. \n发生错误，有可能是由于网络错误。')
                                        del mp4[:]
                                if line['retweeted_status']['entities']['media'][0]['type'] == 'photo': # 如果媒体是图片
                                    for i in range(0, len(api.GetStatus(line['retweeted_status']['id_str']).media)):
                                        print api.GetStatus(line['id_str']).media[i].media_url
                                        bot.send_photo(chat_id=cfg.CHAT_ID, photo=api.GetStatus(line['retweeted_status']['id_str']).media[i].media_url)
                            else: # 如果没有媒体
                                pass
                    if line['is_quote_status'] == True: # 如果有转推评论，无需转发媒体
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'从<b>' + line['quoted_status']['user']['name'] + u'</b>转推并引用了如下推文：\n' + line['quoted_status']['text'], parse_mode="HTML")
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>转推评论为：</b>\n' + line['text'], parse_mode="HTML")
                    if line['in_reply_to_status_id'] != None:
                        print u'检测到有回复。'
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>' + line['user']['name'] + u'</b>' + u'回复了' + u'<b>' + api.GetUser(user_id=line['in_reply_to_user_id_str']).name + u'</b>', parse_mode="HTML")
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'<b>回复：</b>\n' + line['text'] + u'\n' + u'<b>回复的信息：</b>\n' + api.GetStatus(line['in_reply_to_status_id_str']).text, parse_mode="HTML") # 如果是回复
                    elif line['in_reply_to_status_id'] == None and line.has_key('retweeted_status') == False and line['is_quote_status'] == False: # 如果不是转推也不是回复也不是引用推特，则为原创推特，需要转发媒体。
                        bot.send_message(chat_id=cfg.CHAT_ID, text=u'''<b>以下为推特内容</b>\n''' + line['text'], parse_mode="HTML")
                        if line['entities'].has_key('media') == False: # 没有媒体（媒体获取模块在此开始）
                            pass
                        else: # 有媒体
                            if line['extended_entities']['media'][0]['type'] == 'video': # 媒体为视频
                                for m in range(0, len(line['extended_entities']['media'][0]['video_info']['variants'])):
                                    if line['extended_entities']['media'][0]['video_info']['variants'][m]['content_type'] == 'video/mp4':
                                        mp4.append(line['extended_entities']['media'][0]['video_info']['variants'][m])
                                    else:
                                        pass
                                print max(mp4, key=operator.itemgetter('bitrate'))['url']
                                try:
                                    bot.send_video(chat_id=cfg.CHAT_ID, video=str(max(mp4, key=operator.itemgetter('bitrate'))['url']))
                                    del mp4[:]
                                except:
                                    bot.send_message(chat_id=cfg.CHAT_ID, text=u'Failed to get content, this is possibly due to a timeout error. \n发生错误，有可能是由于网络错误。')
                                    del mp4[:]
                            if line['entities']['media'][0]['type'] == 'photo': # 媒体为图片
                                for i in range(0, len(api.GetStatus(line['id_str']).media)):
                                    print api.GetStatus(line['id_str']).media[i].media_url
                                    bot.send_photo(chat_id=cfg.CHAT_ID, photo=api.GetStatus(line['id_str']).media[i].media_url)

main()