work_hours = {
    "Іван": 38,
    "Марія": 42,
    "Олег": 35,
    "Софія": 40,
"Юлія ": 44,
"Остап": 15,
"Артем": 33,
"Аделія":17
}

hard_worker_hours = 0
hard_worker_name = ""
for name, hours in work_hours.items():
    if hours > hard_worker_hours:
        hard_worker_hours = hours
        hard_worker_name = name
print(f'the most hardworking person is {hard_worker_name}, work hours: {hard_worker_hours}')