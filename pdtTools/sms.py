from twilio.rest import TwilioRestClient
import phonenumbers as pn

# Find these values at https://twilio.com/user/account
account_sid = "AC704c52f848ac4a38e1c79c261fb5be1a"
auth_token = "df21f1a9fdc7e380b9e121c702dfb954"
client = TwilioRestClient(account_sid, auth_token)


def sms(phone, message):
    '''Send a text message to the given phone number (pn object).'''

    phone = pn.format_number(phone, pn.PhoneNumberFormat.INTERNATIONAL)
    print('Sending message to %s' % phone)
    print('"%s"' % message)
    
    return client.messages.create(to=phone, from_="+16198318787", body=message)
