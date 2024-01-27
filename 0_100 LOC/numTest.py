import os
import subprocess
import shlex
import re
import csv

def get_num_tc(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)
    print(subfolder_path)
    # Read the content of the text file
    with open('notc.txt', 'r') as file:
        content = file.read()

    # Regular expression pattern to match lines like '30:0: 'test_cipher_text_multiline_input' 1'
    pattern = r'\d+:\d+: .+ \d+'

    # Find all matches and count the number of lines
    matches = re.findall(pattern, content)
    num_matching_lines = len(matches)

    # print("Number of matching lines:", num_matching_lines)
    return num_matching_lines


def get_mccabe(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)
    with open('mccabe.txt', 'r') as file:
        content = file.read()
    print(content)
    # Regular expression pattern to match the third value in each line
    # pattern = r"'[^']+' (\d+)"
    # pattern = r': .+ (\d+)'
    pattern = r'\S+\s+\S+\s+(\d+)'

    # Find all matches and store the third values in a list
    values = [int(match.group(1)) for match in re.finditer(pattern, content)]
    print(values)
    return [max(values), sum(values), round(sum(values)/len(values), 2)]
    

def get_loc(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)
    ans = 0
    # Read the content of the text file
    with open('loc.txt', 'r') as file:
        content = file.read()

    # Regular expression pattern to match the SLOC line
    sloc_pattern = r'SLOC: (\d+)'

    # Search for the SLOC line and extract the value
    sloc_match = re.search(sloc_pattern, content)

    if sloc_match:
        sloc_value = sloc_match.group(1)
        ans = int(sloc_value)
        # print("SLOC:", sloc_value)
        
    return ans


def process_subfolder(subfolder_path):
    # Change the current working directory to the subfolder
    os.chdir(subfolder_path)

    # Replace the below 'command' with the actual commands you want to run
    # For example, 'coverage run -m pytest test_example.py'
    # And 'coverage report -m > out.txt' to redirect output to out.txt
    command1 = 'python -m mccabe --min 0 test_example.py > notc.txt'
    # command1 = 'radon raw .meta\example.py > loc.txt'
    #command2 = 'coverage report -m > branch.txt'

    # Properly quote the commands to handle spaces in the path
    # command1 = shlex.quote(command1)
    # command2 = shlex.quote(command2)

    # Run the first command using subprocess
    try:
        subprocess.run(command1, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 1 in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # Run the second command using subprocess and redirect output to out.txt
    # try:
    #     # with open('out.txt', 'w') as output_file:
    #     subprocess.run(command2, shell=True, check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Command 2 in {subfolder_path} returned a non-zero exit code: {e.returncode}")

    # Return to the Main folder's parent directory
    os.chdir('..')

def main():
    # main_folder = 'cat2_functions'
    # main_folder = 'cat1_scripts'
    main_folder = 'cat3_classes'

    # Get the full absolute path of the main folder
    main_folder = os.path.abspath(main_folder)

    # Get a list of all subfolders in the Main folder
    subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]
    print(subfolders)
    print()
    # list_sloc = []
    # list_mccabe = []
    list_ntc = []
    for subfolder in subfolders:
        # print(path)
        # process_subfolder(subfolder)
        # list_mccabe.append(get_mccabe(subfolder))
        # list_sloc.append(get_loc(subfolder))
        list_ntc.append(get_num_tc(subfolder))
        
    #MCCABE *****************************************************************************************************8
    # Path to the CSV file
    # os.chdir('..')
    # print(os.getcwd())
    # csv_file_path = "mccabe_out.csv"
    # print(list_mccabe)
    # # Write the list of lists to the CSV file
    # with open(csv_file_path, 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerows([[num[2]] for num in list_mccabe])
    #     # for row in list_mccabe:
    #     #     csv_writer.writerow(row)
            
    #SLOC*********************************************************************************************************
    # # Write the list of numbers to the CSV file
    # with open(csv_file_path, 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow(["Number"])  # Write header
    #     csv_writer.writerows([[num] for num in list_sloc])  # Write each number in a row
        
    # # Get a list of all subfolders in the Main folder
    # subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]

    # for subfolder in subfolders:
    #     process_subfolder(subfolder)
    # Path to the CSV file
    
    #NTC*********************************************************************************************************
    # Path to the CSV file
    os.chdir('..')
    print(os.getcwd())
    csv_file_path = "ntc_out.csv"
    print(list_ntc)
    # Write the list of numbers to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows([[num] for num in list_ntc])  # Write each number in a row
        

    
    
if __name__ == "__main__":
    main()
    
    
