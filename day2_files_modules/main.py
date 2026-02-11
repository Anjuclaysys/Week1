from utils import file_reader, file_writer

file_writer("sample.txt", "Hello World\n")
content = file_reader("sample.txt")
print(content)
