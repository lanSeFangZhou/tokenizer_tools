class BaseEvaluator:
    def __init__(self, *args, **kwargs):
        self.wc_of_test = 0
        self.wc_of_gold = 0
        self.wc_of_correct = 0

    def process_one_batch(self, gold_data, test_data, *args, **kwargs):
        raise NotImplemented

    def get_score(self):
        # type: () -> Tuple(str, str, str)
        """

        :return: (precision, recall, f1)
        """

        print("WordCount from test result:", self.wc_of_test)
        print("WordCount from golden data:", self.wc_of_gold)
        print("WordCount of correct segs :", self.wc_of_correct)

        # 查全率
        # precision = self.wc_of_correct / float(self.wc_of_test)
        precision = self.wc_of_correct / float(self.wc_of_gold)
        # 查准率，召回率
        recall = self.wc_of_correct / float(self.wc_of_gold)

        f1 = (2 * precision * recall) / (precision + recall)

        metrics = {
            "RECALL": recall,
            "PRECISION": precision,
            "F1-MEASURE": f1
        }

        print("metrics = {}".format(metrics))

        return metrics
