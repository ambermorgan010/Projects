'''
PURPOSE: Sending SMS text messages from Python to your cell phone using Twilio.

AUTHOR: Amber Morgan
'''

#import the Twilio library
import twilio.rest

# Global variables with information needed to send and receive messages.

# Your Twilio phone number
twilio_phone = '+13213011962'

# Your Account SID from twilio.com/console
account_sid = 'AC33c60f7f5e00bd6600175f7ac95ebd2b'

# Your Auth Token from twilio.com/console
auth_token = '084296a08f6dc397104d3f2d6913c6c2'

# Creates a client application that can be made to send and receive text messages
client = twilio.rest.Client(account_sid, auth_token)


def send_message(to_phone, text):
    """
    Sends a text message to the given cell phone number. The phone number must
    be formatted without any spaces, parentheses, or dashes and must contain
    the leading country code (+1 for the US).
    """
    client.messages.create(to=to_phone, from_=twilio_phone, body=text)


def main():
    """
    Send your cell phone a text message.
    """
    send_message('+14849554765', "Hello from Python!")


if __name__ == "__main__":
    main()
