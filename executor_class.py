class Executor:
    def execute(self, dictionary_of_values: dict) -> list:
        """Processes the input dictionary: splitting it into nested and non-nested lists,
        replacing values in non-nested lists, removing nesting from the lists."""
        nested_list_of_dicts, not_nested_list_of_dicts = self.split_by_nested(dictionary_of_values)
        dict_of_replaces_equals = self.replacing_equales_in_not_nested(not_nested_list_of_dicts)
        destroy_nesting_list = self.destroy_nesting(nested_list_of_dicts, dict_of_replaces_equals)
        return destroy_nesting_list

    @staticmethod
    def split_by_nested(dictionary_of_values: dict) -> tuple:
        """Splits the dictionary into nested and non-nested lists"""
        nested_list = []
        not_nested_list = []
        list_of_dictionary = [{key: value} for key, value in dictionary_of_values.items()]
        for item in list_of_dictionary:
            nested_list_bool = ['=' in value for value in list(item.values())[0]]
            if all(nested_list_bool):
                not_nested_list.append(item)
            else:
                nested_list.append(item)
        return nested_list, not_nested_list

    @staticmethod
    def value_from_list_to_dict(values_in_list: list) -> dict:
        """Converts a list of values into a dictionary"""
        dict_of_values = {}
        for value_from_list in values_in_list:
            if type(value_from_list) == str:
                key_in_list, value_in_list = value_from_list.split('=')
                dict_of_values[key_in_list] = value_in_list
            else:
                key_in_single_dict = list(value_from_list.keys())[0]
                dict_of_values[key_in_single_dict] = value_from_list[key_in_single_dict]
        return dict_of_values

    def replacing_equales_in_not_nested(self, not_nested_list: list) -> list:
        """Replaces values in non-nested dictionaries with corresponding key-value pairs"""
        for dct in not_nested_list:
            key_of_list = list(dct.keys())[0]
            value_in_list_in_dict = self.value_from_list_to_dict(dct[key_of_list])
            dct[key_of_list] = value_in_list_in_dict
        return not_nested_list

    @staticmethod
    def keys_extracting(not_nested_list: list) -> list:
        """Extracts keys from the non-nested list"""
        not_nested_keys = []
        for dct in not_nested_list:
            not_nested_keys.append(list(dct.keys())[0])
        return not_nested_keys

    @staticmethod
    def find_not_nested_dict_by_key(not_nested_list: list[dict], needed_key: str) -> dict | None:
        """Finds a non-nested dictionary by key"""
        for dct in not_nested_list:
            if list(dct.keys())[0] == needed_key:
                return dct

    def replace_nesting_in_value(self, value_in_list: list, not_nested_list: list, not_nested_keys: list) -> list:
        """Replaces nesting in value with a corresponding not-nested dictionary"""
        for single_value_index in range(len(value_in_list)):
            single_value = value_in_list[single_value_index]
            if single_value in not_nested_keys:
                value_in_list[single_value_index] = self.find_not_nested_dict_by_key(not_nested_list, single_value)
        return value_in_list

    def destroy_nesting(self, nested_list: list, not_nested_list: list) -> list:
        """Removes nesting from a list of dictionaries"""
        item_num = 0
        while len(nested_list) > 0:
            not_nested_keys = self.keys_extracting(not_nested_list)
            key_nested_list_dct = list(nested_list[item_num].keys())[0]
            all_nested_values_in_nested_list = all(
                [nested_values in not_nested_keys for nested_values in nested_list[item_num][key_nested_list_dct] if
                 '=' not in nested_values])
            if all_nested_values_in_nested_list:
                nested_list[item_num][key_nested_list_dct] = self.replace_nesting_in_value(
                    nested_list[item_num][key_nested_list_dct], not_nested_list, not_nested_keys)
                nested_list[item_num] = {
                    key_nested_list_dct: self.value_from_list_to_dict(nested_list[item_num][key_nested_list_dct])}
                not_nested_list.append(nested_list[item_num])
                nested_list.pop(item_num)
                item_num = 0
            elif item_num == len(nested_list) - 1:
                assert len(nested_list) != 1, 'Incorrect values!'
                item_num = 0
            else:
                item_num += 1
        return not_nested_list
