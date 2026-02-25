import os
from google.genai import types

def write_file(working_directory, file_path, content):

    try:
        # 1. Setup and Validate Paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # Security check: Ensure target is inside working directory
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # check if the file is not a directory
        if os.path.isdir(abs_file_path):
            print(f"abs_file_path: {abs_file_path}")
            return f'Error: Cannot write to "{file_path}" as it is a directory'


        # 2. Create parent directory if not exist
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        # 3. Write Data
        with open(abs_file_path, "w") as f:
            f.write(content)
        
        f.close()

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        

    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Create or Update file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents written in the file",
            )
        },
    ),
)