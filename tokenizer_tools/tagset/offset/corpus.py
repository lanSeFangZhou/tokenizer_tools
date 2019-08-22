from tokenizer_tools.conllz.writer import write_conllx
from tokenizer_tools.converter.offset_to_sentence import offset_to_sentence


class Corpus(list):
    def write_to_file(self, output_file):
        sentence_list = [offset_to_sentence(offset) for offset in self]

        with open(output_file, 'wt') as fd:
            write_conllx(sentence_list, fd)
