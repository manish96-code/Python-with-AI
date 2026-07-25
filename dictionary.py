student = {
    "name": "Manish",
    "age": 25,
    "city": "Purnea"
}
print(student["name"])     # Manish
print(student["age"])     # 25
print(student["city"])     # Purnea
print(student)     # {'name': 'Manish', 'age': 25, 'city': 'Purnea'}
print(type(student))     # dict

student["age"] = 26
student["country"] = "India"
print(student)   # {'name': 'Manish', 'age': 26, 'city': 'Purnea', 'country': 'India'}

del student["city"]
print(student)   # {'name': 'Manish', 'age': 26, 'country': 'India'}



person = {
    "person1": {
        "first_name": "Manish",
        "last_name": "Kumar",
        "roll": 101,
        "age": 25,
        "address": {
            "city": "Purnea",
            "state": "Bihar",
            "pin": 854301
        },
        "course": ["Python", "Data Science", "Machine Learning"]
    },
    "person2": {
        "first_name": "Rupesh",
        "last_name": "Sharma",
        "roll": 102,
        "age": 24,
        "address": {
            "city": "Patna",
            "state": "Bihar",
            "pin": 800001
        },
        "course": ["Java", "Web Development", "Cloud Computing"]
    },
    "person3": {
        "first_name": "Shivam",
        "last_name": "Verma",
        "roll": 103,
        "age": 23,
        "address": {
            "city": "Mumbai",
            "state": "Maharashtra",
            "pin": 400001
        },
        "course": ["C++", "Operating Systems", "Database Management"]
    }
}
print(person["person1"]["first_name"])     # Manish
print(person["person2"]["address"]["city"])     # Patna
print(person["person3"]["address"]["pin"])     # 400001
print(person["person1"]["course"])     # ['Python', 'Data Science', 'Machine Learning']
print(person["person2"]["course"][0])     # Java
print(person["person2"]["course"][2])     # Cloud Computing
print(person)
print(type(person))   # dict

# empty dictionary
empty_dict = {}
print(empty_dict)     # {}

