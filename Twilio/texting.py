'''
PURPOSE: Send and receive SMS text messages from Python using Twilio.

AUTHOR: Amber Morgan
'''

# Import libraries needed for sending and receiving SMS text messages
import http.server
import urllib.parse
import twilio.rest

# Global variables with information needed to send and receive messages.

# Your Twilio phone number (not personal cell phone number)
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
    # Do not modify this function
    client.messages.create(to=to_phone, from_=twilio_phone, body=text)


def receive_message(from_number, message_text):
    """
    This function is called whenever our program receives a text message. The
    cell phone number that sent the message is in `from_number` and is formatted
    like '+12345678901'. The text message they sent is in `message_text`.
    """
    formatted = format_phone_number(from_number)
    print("Text message received from {}: {}".format(formatted, message_text))
    definition = find_acronym_definition(message_text)
    if definition == ("", ""):
        send_message(from_number, "The text message doesn't have any acronyms I know")
    else:
        send_message(from_number, "{} means {}".format(definition[0], definition[1]))


def format_phone_number(from_number):
    """
    Formats the given phone number to a more reader-friendly version.
    """
    formatted_phone_number = "({}) {}-{}".format(from_number[2:5], from_number[5:8], from_number[8:12])
    return formatted_phone_number


def find_acronym_definition(message_text):
    """
    Returns the acronym and its associated definition.
    """
    if 'lol' in message_text.lower():
        return "lol", "laughing out loud"
    elif 'ttyl' in message_text.lower():
        return "ttyl", "talk to you later"
    elif 'jk' in message_text.lower():
        return "jk", "just kidding"
    elif 'hru' in message_text.lower():
        return "hru", "how are you"
    elif 'eta' in message_text.lower():
        return "eta", "estimated time of arrival"
    else:
        return "", ""


######## The rest of the code handles the receipt of text messages ########
#### IMPORTANT! Do not modify below here! ####

class SMSReceiver(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            qs = urllib.parse.parse_qs(self.path[self.path.index('?') + 1:])
            receive_message(qs['From'][0], qs['Body'][0])
        except Exception:
            import sys, traceback
            print("Error while processing received text message:", file=sys.stderr)
            traceback.print_exc()
        self.send_response(204)  # always send empty response to Twilio

    def log_message(self, _format, *args):  # makes HTTPServer quiet
        return


def main():
    server_address = ('', 5000)
    with http.server.HTTPServer(server_address, SMSReceiver) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
