import requests

# OpenWeatherMap API: https://openweathermap.org/current

# TODO: Sign up for an API key
 # OpenWeatherMap API Key

DEFAULT_ZIP = 90089

def get_weather(zip_code):
    params = {
        'appid': OWM_API_KEY,
        # TODO: referencing the API documentation, add the missing parameters for zip code and units (Fahrenheit)
        'zip' : '90089',
        'units' : 'imperial',
    }

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params)

    if response.status_code == 200: # Status: OK
        data = response.json()
        #print(data)
        # TODO: Extract the temperature & humidity from data, and return as a tuple
        list = [(k, v) for k, v in data.items()]
        list = tuple(list)
        keys_to_extract = ["temp","humidity"]
        new_dict = list[3][1]
        #print(list[3][1])
        res = {key: new_dict[key] for key in new_dict.keys()
                               & {'temp', 'humidity'}}
        #print(res)
        return_tuple = (res.get('temp'),res.get('humidity'))
        #print(return_tuple)
        #a_subset = tuple({key: new_dict[key] for key in keys_to_extract})
        #This shows its a tuple
        #print(a_subset)
        #print(type(a_subset))
        return return_tuple

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0, 0.0

def weather_init():
    zip_code = DEFAULT_ZIP
    temp, hum = get_weather(zip_code)
    
    output = '{:.1f}F, {:>.0f}% humidity'.format(temp, hum)
    print('weather for {}: {}'.format(zip_code, output))

    return output


WEATHER_APP = {
    'name': 'Weather',
    'init': weather_init
}


if __name__ == '__main__':
    weather_init()

