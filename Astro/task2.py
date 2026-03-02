from readjs import read
dataset = read()
max_temp = dataset[0][0]
for day in dataset:
   for planet in day:
       if planet['temp'] > max_temp['temp']:
           max_temp = planet
print(f'the hottest planet is {max_temp['name']}, the temperature is {max_temp["temp"]}')




# temperature = []
# max_temp = 0
# for day in dataset:
#    for planet in day:
#       temperature.append(planet['temp'])
#
#
# max_temp = max(temperature)
# for day in dataset:
#    for planet in day:
#       if planet['temp'] == max_temp:
#           print(f'the hottest planet is {planet['name']}, the temperature is {planet["temp"]}')