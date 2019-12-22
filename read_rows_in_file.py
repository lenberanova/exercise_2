with open('text_file_to_read.txt', 'r') as file:
    line = 1
    content = file.readline()
    while content:
        print('Line {}: {}'.format(line, content.strip()))
        content = file.readline()
        line += 1