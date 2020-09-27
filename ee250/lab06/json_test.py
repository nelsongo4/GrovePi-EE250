import json

# json library: https://docs.python.org/3.5/library/json.html

person = {
    'name': 'Tommy Trojan',
    'email': 'tommy@usc.edu',
    'phone': '213-740-2311',
    'nicknames': [
        'Tommy T',
        'Spirit of Troy',
    ],
}

print(type(person))
print(person)

person_json = json.dumps(person)
print(person_json)

# TODO: What type is person_json?
print(type(person_json))
#person_json is of type string as noted by print and type function
#person variable is a dictionary type 
# TODO: Pretty printing
print(json.dumps(person, sort_keys = True, indent = 2))
