from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi("LZKWVjdn0XvAbAf9nFgiq6HhYOkf5cr+BJJ2UfDUShVy3fXeHSD1OJ1k02PRdLe8fD8T+WY9xvJE2IoHuUxjXziJxN5CLKQjf0DXt5rq0ZqhlZEhsVFsgXZGjJWcwYoZnnhpOBFThTKTY0HtFWy92AdB04t89/1O/w1cDnyilFU=") #填入Channel access token
# Channel Secret
handler = WebhookHandler("fcdc3dd7104440616c1f0a98bf47edbc") #填入Channel secret

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
    if get_message == "地點":
        message = LocationSendMessage(
        title = "高雄",
        address = "高雄",
        latitude = 22.747736,
        longitude = 120.421516)   
    else:
        message = TextSendMessage(text=event.message.text)#回復訊息設定

    line_bot_api.reply_message(event.reply_token, message)#回復訊息

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
