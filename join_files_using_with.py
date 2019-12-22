with open('file_new.txt', 'w+') as file:

    with open('file1.txt', 'r') as file1:
        file1_content = file1.read()

    file.write(file1_content)

    with open('file2.txt', 'r') as file2:
        file2_content = file2.read()

    file.write(file2_content)

with open('file_new.txt', 'r') as file:
    result_content = file.read()
    print(result_content)
