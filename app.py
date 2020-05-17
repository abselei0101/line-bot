from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
import os

# Channel Access Token
line_bot_api = LineBotApi(os.environ["token"]) #填入Channel access tokenfrom flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
import os

# Channel Access Token
line_bot_api = LineBotApi(os.environ["token"]) #填入Channel access token
# Channel Secret
handler = WebhookHandler(os.environ["secret"]) #填入Channel secret

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text
    if get_message =="圖片":
        message =ImageSendMessage(
        original_content_url = "https://autos.yahoo.com.tw/p/r/w880/car-trim/March2019/bfc5dfd3d0692287ac9946be100e5eeb.jpeg",
        preview_image_url = "https://autos.yahoo.com.tw/p/r/w880/car-trim/March2019/bfc5dfd3d0692287ac9946be100e5eeb.jpeg"
        )
    elif get_message == "地點":
        message = LocationSendMessage(
        title = "高雄",
        address = "高雄",
        latitude = 22.747736,
        longitude = 120.421516)
    elif get_message == "貼圖":
        message = StickerSendMessage(
            package_id= "1",
            sticker_id="1"
        )
    elif get_message == "按鈕":
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                title='Menu',
                text='Please select',
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    ),
                    URITemplateAction(
                        label='uri',
                        uri='http://example.com/'
                    )
                ]
            )
        )
    elif get_message == "選擇按鈕":
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Are you sure?',
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='data'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    )
                ]
            )
        )
    elif get_message == "選擇按鈕":
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.smartm.com.tw/data/Images/ec/24/a5/4d/f6ff18b13a9728bea09279d.jpg',
                        title='this is menu1',
                        text='description1',
                        actions=[
                            PostbackTemplateAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='message1',
                                text='message text1'
                            ),
                            URITemplateAction(
                                label='uri1',
                                uri='https://www.smartm.com.tw/article/31363834cea3'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://is1-ssl.mzstatic.com/image/thumb/Video111/v4/9d/8e/34/9d8e34e2-2327-3840-c184-bf4a125c5d37/pr_source.lsr/268x0w.png',
                        title='this is menu2',
                        text='description2',
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='uri2',
                                uri='https://itunes.apple.com/tw/movie/%E5%B0%8F%E5%B0%8F%E5%85%B5/id991371510'
                            )
                        ]
                    )
                ]
            )
        )
    elif get_message == "imagecarouseltemplate":
        message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                        action=PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='data'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                        action=MessageTemplateAction(
                            label='Message',
                            text='Message text2',
                        )
                    )
                    ,
                    ImageCarouselColumn(
                        image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                        action=URITemplateAction(
                            label='uri',
                            uri='http://example.com/'
                        )
                    )

                ]
            )
        )
    else:
        message = TextSendMessage(text=event.message.text)#回復訊息設定

    line_bot_api.reply_message(event.reply_token, message)#回復訊息

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
# Channel Secret
handler = WebhookHandler(os.environ["secret"]) #填入Channel secret

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text
    if get_message =="圖片":
        message =ImageSendMessage(
        original_content_url = "https://autos.yahoo.com.tw/p/r/w880/car-trim/March2019/bfc5dfd3d0692287ac9946be100e5eeb.jpeg",
        preview_image_url = "https://autos.yahoo.com.tw/p/r/w880/car-trim/March2019/bfc5dfd3d0692287ac9946be100e5eeb.jpeg"
        )
    elif get_message == "地點":
        message = LocationSendMessage(
        title = "高雄",
        address = "高雄",
        latitude = 22.747736,
        longitude = 120.421516)
    elif get_message == "貼圖":
        message = StickerSendMessage(
            package_id= "1",
            sticker_id="1"
        )
    elif get_message == "按鈕":
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                title='Menu',
                text='Please select',
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    ),
                    URITemplateAction(
                        label='uri',
                        uri='http://example.com/'
                    )
                ]
            )
        )
    elif get_message == "confirmtemplate":
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Are you sure?',
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='data'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    )
                ]
            )
        )
    elif get_message == "carouseltemplate":
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.smartm.com.tw/data/Images/ec/24/a5/4d/f6ff18b13a9728bea09279d.jpg',
                        title='this is menu1',
                        text='description1',
                        actions=[
                            PostbackTemplateAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='message1',
                                text='message text1'
                            ),
                            URITemplateAction(
                                label='uri1',
                                uri='https://www.smartm.com.tw/article/31363834cea3'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://is1-ssl.mzstatic.com/image/thumb/Video111/v4/9d/8e/34/9d8e34e2-2327-3840-c184-bf4a125c5d37/pr_source.lsr/268x0w.png',
                        title='this is menu2',
                        text='description2',
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='uri2',
                                uri='https://itunes.apple.com/tw/movie/%E5%B0%8F%E5%B0%8F%E5%85%B5/id991371510'
                            )
                        ]
                    )
                ]
            )
        )
    elif get_message == "imagecarouseltemplate":
        message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                        action=PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='data'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                        action=MessageTemplateAction(
                            label='Message',
                            text='Message text2',
                        )
                    )
                    ,
                    ImageCarouselColumn(
                        image_url='https://img.hypesphere.com/2015-10-22-174039-60.jpg',
                        action=URITemplateAction(
                            label='uri',
                            uri='http://example.com/'
                        )
                    )

                ]
            )
        )
    else:
        message = TextSendMessage(text=event.message.text)#回復訊息設定

    line_bot_api.reply_message(event.reply_token, message)#回復訊息

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
