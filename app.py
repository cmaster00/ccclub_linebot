from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'X7Qq3dtLuLqxc2sZsET/NVR3rpcMI8iwIUIEgnNmqpqLH8n4n4Z9lbfHZgbvuG/FSo2JhnWjiW5m+QGb8Qo5VTCWvjlpi9qekQJyziJm4SYt13FDFgQo1qhGUQ9qHmh8Wy+cKfxp0Sv5h9PS3S59lQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2e0d562f63e18ddeab0cd06e772ea22f')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉，您說什麼?'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return

    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
