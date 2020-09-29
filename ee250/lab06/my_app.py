#This is App
import json
import requests

def get_text():
    params = {
    }
    #response = requests.get("http://api.open-notify.org/iss-pass.json?lat=45.0&lon=-122.3&alt=20&n=5&callback=",params)
    response = requests.get("http://api.open-notify.org/astros.json?callback")
    if response.status_code == 200:
        data = response.json()
        #print(response.text)
        #print(type(response.text))
        #print(json.dumps(data, sort_keys = True, indent = 4))
        return response.text
    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None
def get_text_init():
    text = get_text()
    output = '{}'.format(text)
    print(text)
    return output
GTLL_APP = {
    'name': 'Get Text',
    'init': get_text_init
}
if __name__ == '__main__':
    get_text_init()

