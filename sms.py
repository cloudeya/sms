from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe310669548bba5b66dc36a6728182db2"
# Your Auth Token from twilio.com/console
auth_token  = "8f45538c37996948bb24f6de43fe4707"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886912785049", 
    from_="+17246053695",
    body="Hello昀!以後用這來通知虛擬貨幣漲幅喔!")

print(message.sid)
