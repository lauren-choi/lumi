from twilio.rest import Client

account_sid = 'ACcdc4119af79d46419a3501fdb27ef4e9'
auth_token = 'f11f3f684ab5465f4c9458b4e859d37b'
client = Client(account_sid, auth_token)

def send_sms(mood):
#ideally there would be infinite number of quotes that we'd get from the web
    happyquotes = ["Being happy NEVER goes out of style - Lily Pulitzer", "When you love what you have, you have everything you need", "You are gold, baby. Solid gold."]
    mehquotes = ["Difficult roads often lead to beautiful destinations", "Great things never came from comfort zones. It's okay to feel lost.", "You won't find happiness if you keep looking in the smae place you lost it."]
    sadquotes = ["Don't wait until you reach your goal to be proud of yourself. Be proud of every step you take.", "Keep your head up, keep your heart strong.", "Trust me, the best has yet to come."]

    if mood != 1 or mood != 2 or mood != 3:
         return;

    if mood == 1:
        happyiterator = iter(happyquotes)

        message = client.messages \
            .create(
                 body = next(happyiterator),
                 from_='+15108040184',
                 to='+16096477951'
             )
        print(message.sid)

    #if user presses meh button
    if mood == 2:
        mehiterator = iter(mehquotes)

        message = client.messages \
            .create(
                 body = next(mehiterator),
                 from_='+15108040184',
                 to='+16096477951'
             )
        print(message.sid)

    #if user presses not okay button
    if mood == 3:
        saditerator = iter(sadquotes)

        message = client.messages \
            .create(
                 body = next(saditerator),
                 from_='+15108040184',
                 to='+16096477951'
             )
        print(message.sid)


if __name__ == '__main__':
    send_sms(3)


#if user presses happy button
# if mood == 1:
#     for i in happyquotes:
#         message = client.messages \
#             .create(
#                  body = i,
#                  from_='+15108040184',
#                  to='+16096477951'
#              )



        #body = next(sadquotes)

# message = client.messages \
#     .create(
#          body = body,
#          from_='+15108040184',
#          to='+16096477951'
#      )

# print(message.sid)

# def send_sms():
#     message = client.messages.create(
#         to = request.form['To'],

#
# #credentials
# account_sid = 'ACcdc4119af79d46419a3501fdb27ef4e9' # account account_sid
# auth_token = 'f11f3f684ab5465f4c9458b4e859d37b'
#
# client = Client(account_sid, auth_token)
#

# def send_sms():
#     message = client.messages.create(
#         to = request.form['To'],
#         from_ = '+15108040184',
#         body = request.form['Body'],
#     )
#
#     return message.sid
#
# if __name__ == '__main__':
#     app.run()
