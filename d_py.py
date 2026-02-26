print('Hello Julia')
my_dict={'a':1,'b':2,'c':3}
print(my_dict['a'])

# перебір ключів
for key in my_dict:
    print(key)

print('--------------------------')
# перебір лише значень
for value in my_dict.values():
    print(value)
print('--------------------------')
# перебір пар ключ-значення
for key, value in my_dict.items():
    print(f"Ключ: {key}, значення: {value}")
print(my_dict.items())
print('-----------or--------------') # аналог
for i in my_dict:
    print(f"Ключ: {i}, значення: {my_dict[i]}")