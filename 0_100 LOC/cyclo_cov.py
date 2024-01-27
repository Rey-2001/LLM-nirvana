import os
import subprocess
import shlex

# calculating mccabe cyclometric complexity (CC)

def process_subfolder(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)

    # Replace the below 'command' with the actual commands you want to run
    command = 'python3.9 -m mccabe --min 0 test_example.py'

    # Properly quote the commands to handle spaces in the path
    # command1 = shlex.quote(command1)
    # command2 = shlex.quote(command2)

    # Run the second command using subprocess and redirect output to out.txt
    try:
        with open('notc.txt', 'w') as output_file:
            subprocess.run(command, shell=True, check=True, stdout=output_file)
    except subprocess.CalledProcessError as e:
        print(f"Command in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # Return to the Main folder's parent directory
    os.chdir('..')

def main():
    main_folder = 'cat1_scripts'  # 'cat2_functions' #'cat3_classes' 

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