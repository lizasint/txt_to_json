from executor_class import Executor
from parser_class import Parser
from serializer_class import Serializer


class Converter:
    def __init__(self, parser: Parser, executor: Executor, serializer: Serializer, input_filename: str,
                 output_filename: str):
        self.parser = parser
        self.executor = executor
        self.serializer = serializer
        self.input_filename = input_filename
        self.output_filename = output_filename

    def convert(self):
        """Performs the conversion process from the input file to the output file"""
        dictionary = self.parser.parse(self, self.input_filename)
        dictionary_processed = self.executor.execute(dictionary)
        self.serializer.serialize(dictionary_processed, self.output_filename)
