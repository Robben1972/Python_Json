import json

# Function to read JSON data from a file
def read_json(file_path):
    """
    Reads JSON data from a file and returns it as a dictionary.
    
    Args:
        file_path (str): The path to the JSON file.
        
    Returns:
        dict: The JSON data as a dictionary.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write a dictionary to a JSON file
def write_json(file_path, data):
    """
    Writes a dictionary to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        data (dict): The dictionary to write to the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to update a JSON file with new data
def update_json(file_path, new_data):
    """
    Updates a JSON file with new data. It merges the new data with the existing data.
    
    Args:
        file_path (str): The path to the JSON file.
        new_data (dict): The new data to merge with the existing data.
    """
    # Read the existing data
    data = read_json(file_path)
    
    # Update the existing data with the new data
    data.update(new_data)
    
    # Write the updated data back to the file
    write_json(file_path, data)

# Example usage
if __name__ == "__main__":
    # Define a sample JSON file path
    json_file = 'sample_data.json'
    
    # Sample data to write to JSON
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    
    # Write the sample data to the JSON file
    write_json(json_file, sample_data)
    
    # Read the data from the JSON file
    data = read_json(json_file)
    print("Read JSON Data:", data)
    
    # Update the JSON file with new data
    new_data = {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    update_json(json_file, new_data)
    
    # Read the updated data from the JSON file
    updated_data = read_json(json_file)
    print("Updated JSON Data:", updated_data)
