import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

    try:
        # 1. Setup and Validate Paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # 1-1. Security check: Ensure target is inside working directory
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 1-2. Check if the file_path points to a file
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # 1-3. Check if the file is a python file
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'


        # 2. Use subprocess to run the file
        
        # 2-1. Create command token list
        command = ["python", abs_file_path]
        
        # 2-2. Add additional args to command token list
        if args:
            command.extend(args)

        # 2-3. run subprocess
        completed_subprocess = subprocess.run(
            args=command, 
            text=True, 
            timeout=30, 
            capture_output=True, 
            cwd=abs_working_dir
            )

        # 3. Return Result of subprocess
        if completed_subprocess.stdout:
            return f"STDOUT: {completed_subprocess.stdout}"
        
        if completed_subprocess.stderr:
            return f"STDERR: {completed_subprocess.stderr}"
        
        if completed_subprocess.returncode:
            return f"Process exited with code {completed_subprocess.returncode}"
        
        return f"No output produced"
    


    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "args"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of arguments input through CLI",
                items= types.Schema(
                    type=types.Type.STRING,
                    description="Argument given through CLI",
                )
            ),
        },
    ),
)