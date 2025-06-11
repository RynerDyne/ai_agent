import os


def get_files_info(working_directory, directory=None):
    dir_list = os.listdir(working_directory)
    cur_dir = working_directory
    if directory != None and directory != '.' and directory not in dir_list:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    elif directory != None and directory != '.' and directory in dir_list:
        cur_dir = os.path.join(cur_dir, directory)
        if os.path.isdir(cur_dir):
            dir_list = os.listdir(cur_dir)
        else:
            return f'Error: "{directory}" is not a directory'
    try:
        file_info_text = ''
        for dir in dir_list:
            dir_path = os.path.join(cur_dir, dir)
            file_size = os.path.getsize(dir_path)
            is_dir = os.path.isdir(dir_path)
            file_info = f"- {dir}: file_size={file_size} bytes, is_dir={is_dir}\n"
            file_info_text += file_info
        return file_info_text
    except Exception as e:
        return f"Error: {e}"
