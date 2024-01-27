import os
import subprocess
import shlex

# calculating branch coverage

def process_subfolder(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)

    # Replace the below 'command' with the actual commands you want to run
    # For example, 'coverage run -m pytest test_example.py'
    # And 'coverage report -m > out.txt' to redirect output to out.txt
    command1 = 'coverage run --branch -m pytest test_example.py'
    command2 = 'coverage report -m > branch_coverage.txt'

    # Properly quote the commands to handle spaces in the path
    # command1 = shlex.quote(command1)
    # command2 = shlex.quote(command2)

    # Run the first command using subprocess
    try:
        subprocess.run(command1, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 1 in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # Run the second command using subprocess and redirect output to out.txt
    try:
        # with open('out.txt', 'w') as output_file:
        subprocess.run(command2, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 2 in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # Return to the Main folder's parent directory
    os.chdir('..')

def main():
    main_folder = 'cat2_functions'

    # Get the full absolute path of the main folder
    main_folder = os.path.abspath(main_folder)

    # Get a list of all subfolders in the Main folder
    subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]
    print(subfolders)
    print()
    for subfolder in subfolders[:]:
        print(subfolder)
        process_subfolder(subfolder)

    # # Get a list of all subfolders in the Main folder
    # subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]

    # for subfolder in subfolders:
    #     process_subfolder(subfolder)
    
    
    
if __name__ == "__main__":
    main()