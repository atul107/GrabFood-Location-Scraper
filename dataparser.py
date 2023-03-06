import json

class JsonParser:
    # Saves the given data to a file in JSON format with indentation of 4 spaces.
    def save_data_to_file(self, data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)