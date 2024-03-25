import os

def clear_downloads():
    # Get the path to the user's Downloads directory
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    # Change the current working directory to Downloads
    os.chdir(downloads_dir)

    # Check the operating system
    if os.name == 'nt':  # Windows
        # Command to delete files in the Downloads directory recursively
        del_files_command = "del /S /Q *.*"

        # Command to remove directories in the Downloads directory recursively
        del_dirs_command = "for /D %p in (*) do rmdir /s /q %p"

        # Execute commands
        os.system(del_files_command)
        os.system(del_dirs_command)
    else:  # Unix/Linux
        # Command to delete files and directories in the Downloads directory recursively
        del_files_dirs_command = "rm -rf *"

        # Execute command
        os.system(del_files_dirs_command)

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
