from enum import Enum

GLOBAL_CORPUS_COMPARE_WAY = None


def consider_text_only_document_compare_function(self, other):
    return self.text == other.text


def consider_text_only_document_hash_function(self):
    return hash(frozenset(self.text))


def consider_text_entity_compare_function(self, other):
    return self.text == other.text and self.span_set == other.span_set


def corpus_set_compare_way(compare_way):
    # set global corpus compare way
    global GLOBAL_CORPUS_COMPARE_WAY

    GLOBAL_CORPUS_COMPARE_WAY = compare_way


def corpus_get_compare_way():
    # get global corpus compare way
    return GLOBAL_CORPUS_COMPARE_WAY


def consider_text_entity_hash_function(self):
    return hash((frozenset(self.text), self.span_set))


class DocumentCompareContext:
    def __init__(self, current_context):
        self.current_context = current_context
        self.privious_context = None

    def __enter__(self):
        # save current compare way
        self.privious_context = corpus_get_compare_way()

        # set up new compare way
        corpus_set_compare_way(self.current_context)

    def __exit__(self, exception_type, exception_value, traceback):
        # restore the old compare way
        corpus_set_compare_way(self.privious_context)

        if exception_value is not None:  # an exception has occurred
            return False  # reraise the exception


class DocumentCompareWays(Enum):
    TEXT_ONLY = {
        "eq": consider_text_only_document_compare_function,
        "hash": consider_text_only_document_hash_function,
    }
    TEXT_ENTITY_ONLY = {
        "eq": consider_text_only_document_compare_function,
        "hash": consider_text_entity_hash_function,
    }
    TEXT_ENTITY_INTENT_ONLY = 3
    TEXT_ENTITY_INTENT_DOMAIN = 4
    ALL = 5
