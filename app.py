from flask import Flask, url_for, render_template, redirect, request
from airtable import Airtable
from twilio.rest import Client

from vars import BaseKey, ApiKey, TableName, SecretKey, AccountSid, AuthToken
from sms import send
from forms import TextForm, ContactForm
from db.get import get_fields, get_all


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
        base_key = BaseKey()
        table_name = TableName()
        api_key = ApiKey()
        at = Airtable(base_key, table_name, api_key)
        fields = ["ccellarea", "ccellphone"]
        client = Client(AccountSid(), AuthToken()) 
        contacts = get_fields(at, fields)
        for contact in contacts:
            area = str(contact['fields']['ccellarea'])
            phone = str(contact['fields']['ccellphone'])
            area = area[:-2]
            phone = phone[:-2]
            recipient = '+1' + area + phone
            print(recipient)
            # send(message, recipient, client)
        return render_template('sent.html', message=message)
    return render_template('text.html', form = form)

@app.route('/sent')
def sent():
    return render_template('sent.html')

@app.route('/add-contact')
def add_contact():
    form = ContactForm()
    # if request.method == 'POST' and form.validate_on_submit():

    return render_template('add.html', form=form)

@app.route('/listen', methods=['GET', 'POST'])
def stop_listener():
    """
    Respond to incoming STOP message
    """
    resp = twiml.Response()
    

if __name__ == "__main__":
    app.run(debug=True)