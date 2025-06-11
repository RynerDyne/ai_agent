import os


def get_file_content(working_directory, file_path):
    MAX_CHAR = 10000
    dir_list = os.listdir(working_directory)
    file_dir_path = os.path.join(working_directory, file_path)
    end_file_path = file_path.split('/')


    if end_file_path[0] not in dir_list:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_dir_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if len(end_file_path) > 1:
        new_dir = os.path.join(working_directory, end_file_path[0])
        print(new_dir)
        new_file_path = ("/").join(end_file_path[1:])
        print(new_file_path)
        return get_file_content(new_dir, new_file_path)
    
    try:
        with open(file_dir_path, 'r') as f:
            file_content_string = f.read()
            char_count = len(file_content_string.replace(" ", "").replace("\n", ''))
        if char_count > 10000:
            with open(file_dir_path, 'r') as f:
                file_content_string = f"{f.read(MAX_CHAR)}[...File \"{file_path}\" truncated at 10000 characters]"
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
