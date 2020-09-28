import requests
import socket
import json

# Reddit API: https://github.com/reddit-archive/reddit/wiki/API

def qotd_init():
    headers = {
        # Reddit's API rules require a unique User-Agent. For this lab, please leave this as is
        'User-Agent': 'usc.ee250.lab8.' + socket.gethostname()
    }

    params = {
    }

    response = requests.get('http://www.reddit.com/r/quotes/random.json',
                            params=params, headers=headers)

   if response.status_code == 200: # Status: OK
        data = response.json()
        # TODO: Extract the quote from the data. Use pretty printing to help you decipher the json
        quote = 'This is supposed to be quote'
        print(type(data))
        #print(data)
        hello = data[0]
        print(type(hello))
        #key_list = list(hello)
        #values = hello.values()
        #values_list = list(values)
        #print("this")
        #print(values_list)
        #print(json.dumps(values_list, sort_keys = True, indent = 4))
        #print(key_list[1])
        res = {key: hello[key] for key in hello.keys() 
                               & {'data'}}
        print(type(res))
        print(json.dumps(res, sort_keys = True, indent = 4))
        search = res["data"]
        print(type(search))
        #print(json.dumps(search, sort_keys = True, indent = 4))
        new_search = search["children"]
        for super_search in new_search:
            print(super_search)
        print(json.dumps(super_search, sort_keys = True, indent = 4))
        print(type(new_search))
        deeper_search = super_search["data"]
        print(" ")
        print(" ")
        print(json.dumps(deeper_search, sort_keys = True, indent = 4))
        #print(new_search)
        last_search = deeper_search["url"]
        quote_search = deeper_search["title"]
        print(quote_search)
        print(last_search)
        quote = quote_search
        #final_search = requests.get(last_search, params = params,headers = headers)
        #final_search = requests.get(last_search)
        #print(final_search)
        #print(final_search.headers['content-type'])
        print(quote)
        return quote

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None

QOTD_APP = {
    'name': 'Quote of the Day',
    'init': qotd_init
}


if __name__ == '__main__':
    qotd_init()



