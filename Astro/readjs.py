import json as js
def read():
    with open('observations.json', 'r', encoding = "utf-8") as file:
        observations = js.load(file)
    return observations
#read()
#print(read())