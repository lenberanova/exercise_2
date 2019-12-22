from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    the_file = open(file_name, mode)
    yield the_file
    the_file.close()


with open_file('file_2.txt', 'w') as file_w:

    file_w.write('yes!')

with open_file('file_2.txt', 'r') as file_r:
    content = file_r.read()
    print(content)

