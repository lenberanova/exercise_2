from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    the_file = open(file_name, mode)
    yield the_file
    the_file.close()

def multiple_generator(x):
    for i in range(1, 11):
        result = x * i
        yield result

for i in multiple_generator(1):
    with open_file('file_1.txt', 'a') as file_a:
            file_a.write(str(i))

    with open_file('file_1.txt', 'r') as file_r:
        content = file_r.read()
        print(content)

