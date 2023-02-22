from flask import Flask, request, abort
from datetime import timedelta
import time
import json

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

from app_login import *
from app_home import *
from app_customer import *
from app_service import *
from app_form import *

app = Flask(__name__)

app.secret_key = "1234"
app.permanent_session_lifetime = timedelta(minutes=60)

app.register_blueprint(app_login)
app.register_blueprint(app_home)
app.register_blueprint(app_customer)
app.register_blueprint(app_service)
app.register_blueprint(app_form)

YOUR_CHANNEL_ACCESS_TOKEN = 'AXdY/HAZvVGIrYFP9eufs9e/IBLa5Br1Dj+tLbzM9p/6Qxb/hYLouMo5EaE/uahRNimxpzaccdBvaDLeQwynJX9ltPo8Vdk0LVMrWIbX9x/oUQy9vi8jHLb+wmXCY/s/GbTU3XVSktTFj0TMRUx+bgdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '44e593c9eddb75ea144a690943e86c6e'

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print("*"*80)

    try:
        msg_in = event.message.text
        line_id = event.source
        print('msg_in =', msg_in)
        print('line_id =', line_id)
    except:
        pass

    str_time = str(time.time())

    # connect db
    con = sqlite3.connect("db/db.db")
    cur = con.cursor()

    # fn register line
    if msg_in == "register":
        sql = 'insert into tb_tag_register_line (line_id, time) values ("{}", "{}")'.format(line_id, str_time)
        print(sql)
        curs = cur.execute(sql)
        con.commit()
        msg_out = "please insert code id"

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg_out))  

    print("*"*80)

    #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))  

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)