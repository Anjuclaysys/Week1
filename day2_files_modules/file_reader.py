def file_reader(file_path):
    """
    Reads content from a file
    :param path: file path 
    """
    try:
        with open(file_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found")
        return None

text = file_reader('example.txt')
print(text)
