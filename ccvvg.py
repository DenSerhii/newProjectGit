users = {
    "admin1": "admin",
    "user1": "user",
    "manager1": "manager",
    "admin2": "admin"
}

for key, value in users.items():
    if value =='admin':
        print(f'{key} is {value}')
