from readjs import read
dataset = read()
count=1
for day in dataset:
    print("Day", count)
#    print(day)
    for planet in day:
 #       print(planet['moons'])
        if planet['moons']:
            print(planet['name'])
    count+=1
