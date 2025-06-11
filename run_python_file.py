import os
from subprocess import run


def run_python_file(working_directory, file_path):
    try:
        full_dir = os.path.join(working_directory, file_path)

#        assert os.path.isdir(working_directory)
#        assert os.path.isfile(full_dir)

        dir_list = os.listdir(working_directory)
        file_path_list = file_path.split('/')

        if len(file_path_list) > 1 and file_path_list[0] not in dir_list:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_dir):
            return f'Error: File "{file_path}" not found.'
        if file_path[-3:] != '.py':
            return f'Error: "{file_path}" is not a Python file.'

        execute = run(["python3", file_path], timeout=30, capture_output=True, cwd=working_directory)

        exe_output = []
        stdout = execute.stdout
        stderr = execute.stderr

        if stderr or stdout:
            if stdout:
                exe_output.append(f"STDOUT: {stdout}")
            if stderr:
                exe_output.append(f"STDERR: {stderr}")
        else:
            exe_output.append("No output produces.")

        if execute.returncode != 0:
            exe_output.append(f"Process exited with code {execute.returncode}")

        return ('\n').join(exe_output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
