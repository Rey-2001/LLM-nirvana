import os
import subprocess
import shlex

def execute_commands_in_main_folder():
    # Get the path to the "main" folder (assuming get_coverage.py is in the same directory)
    main_folder = os.path.abspath(os.path.dirname('cat2_functions'))

    # Change the current working directory to the "main" folder
    os.chdir(main_folder)

    # Replace the below 'command1' and 'command2' with your desired commands
    command1 = 'coverage run -m pytest test_example.py'
    command2 = 'coverage report -m>line_coverage.txt'

    # Run the first command using subprocess
    try:
        subprocess.run(command1, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 1 returned a non-zero exit code: {e.returncode}")

    # Run the second command using subprocess and redirect output to out.txt
    try:
        subprocess.run(command2, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 2 returned a non-zero exit code: {e.returncode}")
    # try:
    #     with open('out.txt', 'w') as output_file:
    #         subprocess.run(command2, shell=True, check=True, stdout=output_file)
    # except subprocess.CalledProcessError as e:
    #     print(f"Command 2 returned a non-zero exit code: {e.returncode}")

if __name__ == "__main__":
    # Execute the commands in the "main" folder
    execute_commands_in_main_folder()
