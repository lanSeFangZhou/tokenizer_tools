from tokenizer_tools.tagset.BMES import BMESEncoderDecoder
from tokenizer_tools.evaluator.token.tag_level import TagEvaluator


def evaluate_by_files(test_file, gold_file):
    with open(test_file) as fd:
        test_line_list = fd.readlines()

    with open(gold_file) as fd:
        gold_line_list = fd.readlines()

    assert len(test_line_list) == len(gold_line_list)

    bmes_encoder_decoder = BMESEncoderDecoder()
    tag_evaluator = TagEvaluator()

    for i in range(len(gold_line_list)):
        test_line = test_line_list[i]
        gold_line = gold_line_list[i]

        test_word_list = test_line.strip().split()
        gold_word_list = gold_line.strip().split()

        test_tags = bmes_encoder_decoder.encode_word_list_as_string(test_word_list)
        gold_tags = bmes_encoder_decoder.encode_word_list_as_string(gold_word_list)

        tag_evaluator.process_one_paragraph(gold_tags, test_tags)

    precision, recall, f1 = tag_evaluator.get_score()

    return precision, recall, f1
