# JSON Functions
This repository contains Python code for basic JSON file operations. The code provides functionality to read, write, and update JSON files.

Functions:

read_json(file_path):

Description: This function reads JSON data from a file and returns it as a Python dictionary.
Parameters:
file_path (str): The path to the JSON file.
Returns:
A dictionary containing the JSON data.
write_json(file_path, data):

Description: This function writes a Python dictionary to a JSON file.
Parameters:
file_path (str): The path to the JSON file.
data (dict): The dictionary to write to the JSON file.
update_json(file_path, new_data):

Description: This function updates an existing JSON file by merging new data with the current data in the file.
Parameters:
file_path (str): The path to the JSON file.
new_data (dict): The new data to merge with the existing data.
