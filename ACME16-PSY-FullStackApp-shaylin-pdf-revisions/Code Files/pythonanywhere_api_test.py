import requests

username = 'WSUPsych'
token = 'b19849a8c15e16119580e813c9a1bdc2b9985e5b'
host = 'www.pythonanywhere.com'

# API endpoint for starting the console
CONSOLE_START_URL = f'https://{host}/api/v0/user/{username}/consoles/33319540/start/'

headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
response = requests.post(CONSOLE_START_URL, headers=headers)
if response.status_code == 200:
    print('Success')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
     