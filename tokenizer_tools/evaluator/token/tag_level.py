class TagEvaluator:
    def __init__(self):
        self.wc_of_test = 0
        self.wc_of_gold = 0
        self.wc_of_correct = 0

    def process_one_paragraph(self, gold_tag_list, test_tag_list, check_corpus_aligned=False):
        # type: (List[str], List[str]) -> None

        gold_tag_list_len = len(gold_tag_list)
        test_tag_list_len = len(test_tag_list)

        if check_corpus_aligned:
            assert gold_tag_list_len == test_tag_list_len
        else:
            # using gold_tag_list as gold,
            # if test_tag_list is shorter, then padding None as tag
            # if test_tag_list is logger, just ignore the rest
            if test_tag_list_len < gold_tag_list_len:
                test_tag_list.extend(
                    [None] * (gold_tag_list_len - test_tag_list_len)
                )
            if test_tag_list_len > gold_tag_list_len:
                test_tag_list = test_tag_list_len[:gold_tag_list_len + 1]

        tag_len = len(gold_tag_list)
        flag = True
        for i in range(tag_len):
            gold_tag = gold_tag_list[i]
            test_tag = test_tag_list[i]

            if test_tag != gold_tag:
                flag = False

            if test_tag in ('E', 'S'):
                self.wc_of_test += 1
                if flag:
                    self.wc_of_correct += 1
                flag = True

            if gold_tag in ('E', 'S'):
                self.wc_of_gold += 1

    def get_score(self):
        # type: () -> Tuple(str, str, str)
        """

        :return: (precision, recall, f1)
        """

        print("WordCount from test result:", self.wc_of_test)
        print("WordCount from golden data:", self.wc_of_gold)
        print("WordCount of correct segs :", self.wc_of_correct)

        # 查全率
        precision = self.wc_of_correct / float(self.wc_of_test)
        # 查准率，召回率
        recall = self.wc_of_correct / float(self.wc_of_gold)

        f1 = (2 * precision * recall) / (precision + recall)

        print("P = %f, R = %f, F-score = %f" % (precision, recall, f1))
        return precision, recall, f1


if __name__ == "__main__":
    tag_evaluator = TagEvaluator()
    tag_evaluator.process_one_paragraph(
        'BMEBE',
        'BESBE'
    )
    tag_evaluator.process_one_paragraph(
        'BMEBE',
        'BESBE'
    )

    _, _, f1 = tag_evaluator.get_score()
    print(f1)
