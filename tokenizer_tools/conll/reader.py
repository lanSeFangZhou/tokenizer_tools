def read_conll(conll_file):
    sentence_list = []
    with open(conll_file) as fd:
        content = fd.read()

        raw_sentence_list = content.split('\n\n')

        for raw_sentence in raw_sentence_list:
            sentence = []
            raw_line_list = raw_sentence.split('\n')
            for raw_line in raw_line_list:
                line = raw_line.strip()
                item = line.split()

                sentence.append(item)

            sentence_list.append(sentence)

    return sentence_list


if __name__ == "__main__":
    sentence = read_conll('test.conllu')
    print(sentence)
