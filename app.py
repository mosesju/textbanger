from flask import Flask, url_for, render_template, redirect, request
from airtable import Airtable
from twilio.rest import Client

from vars import BaseKey, ApiKey, TestContacts, Messages, SecretKey, AccountSid, AuthToken
from sms import send
from forms import TextForm, ContactForm
from db.get import get_fields, get_all
from db.insert import insert
import datetime


app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = SecretKey()

@app.route('/')
def home():
    title = "Banger Text"
    return render_template('home.html', title=title)

@app.route('/send-text', methods=['GET','POST'])
def send_text():
    form = TextForm()
    title = "Send Text"
    if request.method == 'POST' and form.validate_on_submit():
        message = form.message.data
        at = Airtable(BaseKey(), TestContacts(), ApiKey())
        fields = ["ccellarea", "ccellphone"]
        client = Client(AccountSid(), AuthToken()) 
        contacts = get_fields(at, fields)
        for contact in contacts:
            area = str(contact['fields']['ccellarea'])
            phone = str(contact['fields']['ccellphone'])
            recipient = '+1' + area + phone
            send(message, recipient, client)
        at_messages = Airtable(BaseKey(), Messages(), ApiKey())
        sent_date = datetime.datetime.now()
        sent = {
            'message': message,
            'sent_date': str(sent_date)
        }
        insert(at_messages, sent)
        return render_template('sent.html',title=title, message=message)
    return render_template('text.html', form = form, title = title)

@app.route('/sent')
def sent():
    title = "Sent Text"
    return render_template('sent.html', title = title, message=message)

# This needs to add a record to airtable
@app.route('/add-contact', methods = ['GET', 'POST'])
def add_contact():
    form = ContactForm()
    title = "Add Contact"
    if request.method == 'POST' and form.validate_on_submit():
        bday = str(form.dbday.data)
        print(bday)
        record = {
            'clastname':form.clastname.data,
            'cfirstname':form.cfirstname.data,
            'caddress1':form.caddress1.data,
            'caddress2':form.caddress2.data,
            'ccity':form.ccity.data,
            'cstate':form.cstate.data,
            'czip':form.czip.data,
            'dbday': bday,
            'cemail':form.cemail.data,
            'ccellarea':form.ccellarea.data,
            'ccellphone':form.ccellphone.data
        }
        at = Airtable(BaseKey(), TestContacts(), ApiKey())
        insert(at, record)
        return render_template('added.html', title=title, record=record)
    return render_template('add.html', form=form, title = title)

@app.route('/listen', methods=['GET', 'POST'])
def stop_listener():
    """
    Respond to incoming STOP message
    """
    resp = twiml.Response()
    

if __name__ == "__main__":
    app.run(debug=True)