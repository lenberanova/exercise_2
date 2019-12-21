import os

with open('temp_file.txt', 'w+') as file:
    file.write('yes!')

with open('temp_file.txt', 'r') as file:
    result = file.read()
    print(result)

with open('temp_file.txt', 'w') as file:
    file.write('yes!!')

with open('temp_file.txt', 'r') as file:
    result = file.read()
    print(result)

with open('temp_file.txt', 'a') as file:
    file.write('!')

with open('temp_file.txt', 'r') as file:
    result = file.read()
    print(result)

os.remove('temp_file.txt')
