import os
from google.genai import types


def write_file(working_directory, file_path, content): 
    try:
        working_dir_abspath = os.path.abspath(working_directory)
        file_path_abspath = os.path.normpath(os.path.join(working_dir_abspath, file_path))


        if os.path.commonpath([working_dir_abspath, file_path_abspath]) != working_dir_abspath:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path_abspath):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(file_path_abspath), exist_ok=True)
        with open(file_path_abspath, "w") as f:
            f.write(content)
        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        print(f'Error: writing to file: {e}')


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a specified file within the working directory (overwriting if the file exists)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)

