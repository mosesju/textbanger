from vars import PhoneNumber

def send(body, recipient, client):
    """
    Sends an SMS via Twilio Programmable SMS

    Parameters
    ----------
    body: The message body
    table_name: recipient The person getting the text
    client: The twilio client

    Returns
    -------
    Nothing, but it sends the message out
    """
    message = client.messages.create(
        body=body,
        from_=PhoneNumber(),
        to=recipient
    )
    print(message.sid)