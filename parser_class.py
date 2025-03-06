class Parser:
    @staticmethod
    def parse(self, filename: str) -> dict:
        """Pasres file by filename and returns dictionary"""
        input_file = open(filename)
        dictionary_of_values = {}
        lines = input_file.readlines()
        for line in lines:
            key, values = line.split(':')
            values_split = list(map(str.strip, values.split(',')))
            dictionary_of_values[key.strip()] = values_split
        input_file.close()
        return dictionary_of_values
