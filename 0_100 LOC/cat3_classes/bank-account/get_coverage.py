import os
import subprocess

def process_subfolder(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)

    # Replace the below 'command' with the actual command you want to run on example.py
    #command = 'python example.py'
    # project_path = '.'                       # '.' or  '%cd%'
    # str1 = 'pynguin --project-path .'       # + './Desktop/btp_579'   ' --output-path ' + './Desktop/btp_579/pynguin-results'    ' --module-name example -v'
    # str2 = ' --output-path .'               # + './Desktop/btp_579/pynguin-results'
    # str3 = ' --module-name example -v'
    command1 = 'coverage run -m pytest test_example.py'
    command2 = 'coverage report -m'


    # Run the first command using subprocess
    try:
        subprocess.run(command1, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 1 in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # Run the second command using subprocess and redirect output to out.txt
    try:
        with open('out.txt', 'w') as output_file:
            subprocess.run(command2, shell=True, check=True, stdout=output_file)
    except subprocess.CalledProcessError as e:
        print(f"Command 2 in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # # Run the command using subprocess and wait for it to complete
    # try:
    #     subprocess.run(command, shell=True, check=True)  # Set timeout (seconds) as needed
    # except subprocess.TimeoutExpired:
    #     print(f"Command in {subfolder_path} took too long to execute.")


    os.chdir('..')

def main():
    main_folder = 'cat3_classes'

    # Get the full absolute path of the main folder
    main_folder = os.path.abspath(main_folder)

    # Get a list of all subfolders in the Main folder
    subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]

    for subfolder in subfolders:
        process_subfolder(subfolder)

    # # Get a list of all subfolders in the Main folder
    # subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]

    # for subfolder in subfolders:
    #     process_subfolder(subfolder)

if __name__ == "__main__":
    main()
