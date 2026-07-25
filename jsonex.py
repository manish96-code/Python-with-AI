import json

person = '''{
    "name": "Manish Kumar",
    "age": 25,
    "address": {
        "street": "123 abc street",
        "city": "Purnea",
        "state": "Bihar",
        "pin": "854301"
    }
}'''

person_dict = json.loads(person)
print(type(person_dict))
print(person_dict)
print(person_dict["name"])