from converter_class import Converter
from executor_class import Executor
from parser_class import Parser
from serializer_class import Serializer


def main():
    parser_txt = Parser()
    executor = Executor()
    serializer_json = Serializer()
    converter_txt_to_json = Converter(input_filename='probe.txt', output_filename='output_json.json', parser=parser_txt,
                                      executor=executor, serializer=serializer_json)
    converter_txt_to_json.convert()


main()
