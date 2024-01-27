import os
import subprocess
# to generate pynguin test cases for category 3

def process_subfolder(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)

    # Replace the below 'command' with the actual command you want to run on example.py
    #command = 'python example.py'
    project_path = '.'                       # '.' or  '%cd%'
    str1 = 'pynguin --project-path .'       # + './Desktop/btp_579'   ' --output-path ' + './Desktop/btp_579/pynguin-results'    ' --module-name example -v'
    str2 = ' --output-path .'               # + './Desktop/btp_579/pynguin-results'
    str3 = ' --module-name example -v'
    command = str1 + str2 + str3

    # Run the command using subprocess and wait for it to complete
    try:
        subprocess.run(command, shell=True, check=True)  # Set timeout (seconds) as needed
    except subprocess.TimeoutExpired:
        print(f"Command in {subfolder_path} took too long to execute.")


    os.chdir('..')

def main():
    main_folder = 'new_cat3' #'cat3'

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
