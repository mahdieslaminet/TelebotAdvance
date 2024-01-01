import json
import requests

def exist(x, y):
    return x.count(y) - 1

def sendphoto(id, photo):
    api_token = "YOUR_API_TOKEN"  # Replace with your actual API token
    url = f"https://api.telegram.org/bot{api_token}/sendPhoto"
    data = {
        "chat_id": id,
        "photo": photo
    }
    response = requests.get(url, params=data)

def sender(id, message, keyboard):
    api_token = "YOUR_API_TOKEN"  # Replace with your actual API token
    url = f"https://api.telegram.org/bot{api_token}/sendmessage"
    data = {
        "chat_id": id,
        "text": message,
        "reply_markup": json.dumps({"inline_keyboard": keyboard})
    }
    response = requests.get(url, params=data)

data = input()

with open('exam.json', 'w') as file:
    file.write(data)

datacod = json.loads(data)

if "callback_query" in data:
    id = datacod["callback_query"]["from"]["id"]
    callback = datacod["callback_query"]["data"]
    photo_url = f"https://server.com/bots/img/{callback}.jpg"
    sendphoto(id, photo_url)
else:
    id = datacod["message"]["from"]["id"]
    message = datacod["message"]["text"]
    text = "با درود. جهت ثبت نام در کلاس های مورد نظر عدد مربوطه را انتخاب کنید"
    keyboard = [
        [
            {"text": "مشاهده دوره های آموزشی", "callback_data": '1'},
            {"text": "ثبت نام در دوره آموزشی", "callback_data": '2'}
        ],
        [
            {"text": "لغو ثبت نام", "callback_data": '3'},
            {"text": "لغو ثبت نام", "callback_data": '4'}
        ],
        [
            {"text": "ثبت نام تست آزمون", "callback_data": '5'},
            {"text": "ثبت نام کارگاه", "callback_data": '6'}
        ]
    ]
    sender(id, text, keyboard)
