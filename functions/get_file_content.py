import os
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abspath = os.path.abspath(working_directory)
        file_path_abspath = os.path.normpath(os.path.join(working_dir_abspath, file_path))


        if os.path.commonpath([working_dir_abspath, file_path_abspath]) != working_dir_abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abspath):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(file_path_abspath, "r") as f:
            file_content_string = f.read(10000)

            if f.read(1):
                file_content_string += (f'[...File "{file_path}" truncated at 10000 characters]')
        return file_content_string


    except Exception as e:
        print(f'Error: {e}')


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {10000} characters) of a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)






