import os

def get_files_info(working_directory, directory="."):
    try:
        # 1. Setup and Validate Paths
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

        # Security check: Ensure target is inside working directory
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # 2. Check if it's actually a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # 3. Gather Data
        items = os.listdir(target_dir)
        output_lines = []
        
        for item in items:
            item_path = os.path.join(target_dir, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            output_lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        # 4. Return as a single string
        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: {e}"