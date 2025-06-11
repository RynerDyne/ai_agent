import os


def write_file(working_directory, file_path, content):
    dir_list = os.listdir(working_directory)
    file_dir_path = os.path.join(working_directory, file_path)
    end_file_path = file_path.split('/')
    non_file_path = os.path.join(working_directory,('/').join(end_file_path[:-1]))

    try:
        if end_file_path[0] not in dir_list:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(non_file_path):
            os.makedirs(file_dir_path)
        if os.path.isdir(file_dir_path):
            os.rmdir(file_dir_path)

        with open(file_dir_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
