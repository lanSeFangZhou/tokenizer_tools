class TagEvaluator:
    def __init__(self):
        self.wc_of_test = 0
        self.wc_of_gold = 0
        self.wc_of_correct = 0

    def process_one_paragraph(self, gold_tag_list, test_tag_list):
        assert len(gold_tag_list) == len(test_tag_list)

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

    def get_f1(self):
        print("WordCount from test result:", self.wc_of_test)
        print("WordCount from golden data:", self.wc_of_gold)
        print("WordCount of correct segs :", self.wc_of_correct)

        # 查全率
        P = self.wc_of_correct / float(self.wc_of_test)
        # 查准率，召回率
        R = self.wc_of_correct / float(self.wc_of_gold)

        f1 = (2 * P * R) / (P + R)

        print("P = %f, R = %f, F-score = %f" % (P, R, f1))
        return P, R, f1


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

    _, _, f1 = tag_evaluator.get_f1()
    print(f1)
