from twilio.rest import Client

account_sid = 'AC19b1cb9ea8ab5cefbde1421a98739e10'
auth_token = 'e88b6b8215eba5f6847bd78af0ec2202'


def sending_text(msg, number):
    client = Client(account_sid, auth_token)
    number = "+91" + number
    client.messages \
        .create(
            body=msg,
            from_='+13153295098',
            to=number
        )
    return ("Message Sent to " + number)