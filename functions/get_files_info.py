import os

def get_files_info(working_directory, directory="."):
    
    abs_path = os.path.abspath(working_directory)
    # print(f"abs_path: {abs_path}")
    target_dir = os.path.normpath(os.path.join(abs_path, directory))
    # print(f"target_dir: {target_dir}")
    validate_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
    # print(f"commonpath: {os.path.commonpath([abs_path, target_dir])}")
    
    

    target_dir_contents = os.listdir(target_dir)
    # print(f"Contents: {target_dir_contents}")
    consoled_directory = directory
    if directory == '.':
        consoled_directory = "current"
    print(f"Result for '{consoled_directory}' directory:")

    if not validate_target_dir:
        return print(f'\tError: Cannot list "{directory}" as it is outside the permitted working directory')
    
    
    if not os.path.isdir(target_dir):
        return print(f'\tError: "{target_dir}" is not a directory')

    for content in target_dir_contents:
        print(f"\t- {content}: file_size={os.path.getsize(target_dir + "/" + content)} bytes, is_dir={os.path.isdir(target_dir + "/" + content)}")
        # print(f"- {content.replace(".py", "")}: file_size={os.path.getsize("/Users/syk25/workspace/syk25/agent-python/calculator/tests.py")} bytes, is_dir={os.path.isdir("/Users/syk25/workspace/syk25/agent-python/calculator/tests.py")}")




