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


text = "hello world"
file_writer("writer.txt", text)
