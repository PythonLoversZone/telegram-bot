import base64
import requests
USERNAME = 'xxx'
PORT = 1111
URL = 'https://xxx/api/get/invitecode/'
TOKEN = base64.b64encode(
    bytes('{}+{}'.format(USERNAME, PORT), 'utf8')).decode()


def get_invite_code():
    r = requests.post(URL, data={'token': TOKEN})
    return r.json().get('msg')
