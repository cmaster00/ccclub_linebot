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
import requests
import json
from bs4 import BeautifulSoup

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

def cashback():
    url = 'https://rich01.com/best-only-cashback-credit-cards/'
    r = requests.get(url, verify=False)

    if r.status_code == requests.codes.ok:

        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', style="border-collapse: collapse; width: 100%; height: 970px;")

        trs = table.find_all('tr')
        for tr in trs[1:6]:
            tds = tr.find_all('td')
            for td in tds[0]:
                card_name = td.text
                print(card_name)
            for td in tds[1]:
                card_fdback = td.text
                print(card_fdback)

        question = soup.find('div', id="sp-eap-accordion-section-18093").find('script',
                                                                              type="application/ld+json").get_text()
        questiontojson = json.loads(question, strict=False)
        qa_info = questiontojson['mainEntity']
        for qa in qa_info:
            print(qa['name'])
            print(qa['acceptedAnswer']['text'])
    else:
        print("Can't get the website")


def credit_cashback():
    url_2 = 'https://rich01.com/e-commerce-credit-card/'
    r = requests.get(url_2, verify=False)

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find()
        tables = soup.find_all('table')
        for table in tables[4:7]:
            trs = table.find_all('tr')
            for tr in trs[2:len(trs) - 1]:
                tds = tr.find_all('td')
                for td in tds[0]:
                    print(td.text)
                for td in tds[1]:
                    print(td.text)
    else:
        print("Can't get the website")


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
        cashback()
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
