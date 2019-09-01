from twilio.rest import Client
#----------------------------------------------------------------------
def send_sms(msg, to):
    """"""
    sid = "AC056203e0175b224658eebe90ae61e206"
    auth_token = "e10778887be3e074991467d5e5ccf67c"
    twilio_number = "+12563872746"
    client = Client(sid, auth_token)
    message = client.messages.create(body=msg,
                                     from_=twilio_number,
                                     to=to,
                                     )
if __name__ == "__main__":
    msg = "Hello from Bukan Coder!"
    to = "+12562429413"
    send_sms(msg, to)
