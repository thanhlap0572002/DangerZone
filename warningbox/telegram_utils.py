import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "5943834188:AAFWeEX-O1TuzqgN068i8l6qxX7hQ11eJUs"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="5755763712", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiểm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")

# def send_telegram(photo_path="loan.jpg"):
#     try:
#         my_token = "5995405241:AAFn7cwPOhlrNiuAJESs8Sg78j3Yg3-DrRU"
#         bot = telegram.Bot(token=my_token)
#         bot.sendPhoto(chat_id="5755763712", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
#     except Exception as ex:
#         print("Can not send message telegram ", ex)
#
#     print("Send sucess")