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
    

def file_writer(file_path, text):
    """
    write a content to a text file
    """
    try:
        with open(file_path, "w") as file:
            file.write(text)
            print("content add to file")
    except Exception as e:
        print(e)
        