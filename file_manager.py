import json
import os

class FileManager:

    @staticmethod
    def load_data(filename):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, filename)

        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as file:
            try:
                return json.load(file)
            except:
                return []

    @staticmethod
    def save_data(filename, data):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, filename)

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)