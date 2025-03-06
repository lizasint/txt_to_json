import json


class Serializer:
    @staticmethod
    def serialize(processed_dictionary: list, output_filename: str) -> None:
        """Serializes a list of dictionaries into a JSON file"""
        json_file = json.dumps(processed_dictionary, indent=4)
        file_out = open(output_filename, 'w')
        file_out.write(json_file)
        file_out.close()
