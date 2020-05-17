from flask import Flask, url_for, render_template, redirect, request
from forms import TextForm

from vars import BaseKey, ApiKey, TableName, SecretKey, AccountSid, AuthToken
from sms import send
from db.get import get
from twilio.rest import Client


app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = SecretKey()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send-text', methods=['GET','POST'])
def send_text():
    form = TextForm()
    if request.method == 'POST' and form.validate_on_submit():
        message = form.message.data
        contacts = get(BaseKey(), TableName(), ApiKey())
        client = Client(AccountSid(), AuthToken())
        for contact in contacts:
            recipient = contact['fields']['phone_number']
            send(message, recipient, client)
        return render_template('sent.html', message=message)
    return render_template('text.html', form = form)
@app.route('/sent')
def sent():
    return render_template('sent.html')

if __name__ == "__main__":
    app.run(debug=True)