def generate_line(file_name):
    with open(file_name, 'r') as file:
        line = 1
        content = file.readline()
        while content:
            yield content
            content = file.readline()
            line += 1

generator1 = generate_line('text_file_to_read.txt')

for i in generator1:
    print(i, end='')

#while True:
    #try:
        #print(generator1.__next__(), end='')
    #except:
        #break