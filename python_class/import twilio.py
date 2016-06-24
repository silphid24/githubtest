from twilio.rest import TwilioRestClient

account_sid = "ACc7874066e5084cfb791b329e00b35771" # Your Account SID from www.twilio.com/console
auth_token  = "77298de3ccc61812bc91c6a8c5fa3d3f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="second",
    to="+12404892440",    # Replace with your phone number
    from_="+12404892440") # Replace with your Twilio number

print(message.sid)