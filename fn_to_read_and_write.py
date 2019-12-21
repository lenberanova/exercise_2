
def file_reader(file_name):
    file = open(file_name, 'r')
    #devides the rows to the list
    #result = file.read().split('\n')
    result = file.read()
    print(result)
    file.close()

def file_writer(file_name):
    file = open(file_name, 'w')
    file.write('ano')
    file.close()


job_read = file_reader('text_file_to_read.txt')

job_write = file_writer('text_file_to_write.txt')
