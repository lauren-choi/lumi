from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

#credentials
account_sid = 'ACcdc4119af79d46419a3501fdb27ef4e9' # account account_sid
auth_token = 'f11f3f684ab5465f4c9458b4e859d37b'

client = Client(account_sid, auth_token)

@app.route('/sms', methods = ['POST'])
def send_sms():
    message = client.messages.create(
        to = request.form['To'],
        from_ = '+15108040184',
        body = request.form['Body'],
    )

    return message.sid

if __name__ == '__main__':
    app.run()
