from tokenizer_tools.tagset.NER.base_tagset import BaseTagSet


class BILUOEncoderDecoder(BaseTagSet):
    def generate_tag(self, prefix):
        if self.tag_name == 'O':
            # O tag is very special, it always return O
            return "O"

        return "{}-{}".format(prefix, self.tag_name)

    def encode(self, sequence):
        len_of_sequence = len(sequence)

        if len_of_sequence == 1:
            return [self.generate_tag('U')]

        elif len_of_sequence == 2:
            return [self.generate_tag('B'), self.generate_tag('L')]

        else:
            return [self.generate_tag('B')] + [self.generate_tag('I')] * (len_of_sequence - 2) + [self.generate_tag('L')]

    def decode(self, sequence):
        pass
