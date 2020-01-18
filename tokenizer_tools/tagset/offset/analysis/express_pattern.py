import collections
import copy
from typing import Tuple, Dict, Any

from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.document import Document


class ExpressPattern:
    def __init__(self, corpus: Corpus):
        self.corpus = corpus

    def compute(self) -> Dict[Tuple, Document]:
        pattern_mapping = collections.defaultdict(list)
        for doc in self.corpus:
            pattern = self.convert_to_pattern(doc)
            pattern_mapping[pattern].append(doc)

        return dict(pattern_mapping)

    @staticmethod
    def convert_to_pattern(doc: Document) -> Tuple[Any]:
        text = copy.deepcopy(doc.text)
        for span in doc.span_set:
            text[span.start: span.end] = ["<{}>".format(span.entity)] + (span.end - span.start - 1) * [None]

        return tuple(filter(lambda x: x is not None, text))
