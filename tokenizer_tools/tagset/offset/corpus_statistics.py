import collections
import typing
from collections import Counter
from typing import Dict, Tuple, Optional

if typing.TYPE_CHECKING:
    from tokenizer_tools.tagset.offset.corpus import Corpus


class CorpusStatistics:
    def __init__(
        self,
        domain: Optional[Counter] = None,
        function: Optional[Counter] = None,
        sub_function: Optional[Counter] = None,
        intent: Optional[Counter] = None,
        entity_types: Optional[Dict[str, Counter]] = None,
        entity_values: Optional[Dict[Tuple, Counter]] = None,
    ):
        self.domain: Optional[Counter] = domain
        self.function: Optional[Counter] = function
        self.sub_function: Optional[Counter] = sub_function
        self.intent: Optional[Counter] = intent
        self.entity_types: Optional[Dict[str, Counter]] = entity_types
        self.entity_values: Optional[Dict[Tuple, Counter]] = entity_values

    @classmethod
    def create_from_corpus(cls, corpus: "Corpus") -> "CorpusStatistics":
        domain = cls._collect_domain(corpus)
        function = cls._collect_function(corpus)
        sub_function = cls._collect_sub_function(corpus)
        intent = cls._collect_intent(corpus)
        entity_types = cls._collect_entity_types(corpus)
        entity_values = cls._collect_entity_values(corpus)

        return cls(domain, function, sub_function, intent, entity_types, entity_values)

    @classmethod
    def _collect_domain(cls, corpus: "Corpus") -> Counter:
        domain_list = [doc.domain for doc in corpus]
        return Counter(domain_list)

    @classmethod
    def _collect_function(cls, corpus: "Corpus") -> Counter:
        function_list = [doc.function for doc in corpus]
        return Counter(function_list)

    @classmethod
    def _collect_sub_function(cls, corpus: "Corpus") -> Counter:
        sub_function_list = [doc.sub_function for doc in corpus]
        return Counter(sub_function_list)

    @classmethod
    def _collect_intent(cls, corpus: "Corpus") -> Counter:
        intent_list = [doc.intent for doc in corpus]
        return Counter(intent_list)

    @classmethod
    def _collect_entity_types(cls, corpus: "Corpus") -> Dict[str, Counter]:
        """
        collect statistic info about entity type: each type have what kinds of values
        """
        entities_mapping = collections.defaultdict(list)
        for doc in corpus:
            for span in doc.entities:
                entities_mapping[span.entity].append(tuple(span.value))
        return {k: Counter(v) for k, v in entities_mapping.items()}

    @classmethod
    def _collect_entity_values(cls, corpus: "Corpus") -> Dict[Tuple, Counter]:
        """
        collect statistic info about entity value: each value have what kinds of types
        """
        value_mapping = collections.defaultdict(list)
        for doc in corpus:
            for span in doc.entities:
                value_mapping[tuple(span.value)].append(span.entity)
        return {k: Counter(v) for k, v in value_mapping.items()}

    def __eq__(self, other: "CorpusStatistics"):
        if not isinstance(other, CorpusStatistics):
            return False
        return (
            (self.domain == other.domain)
            and (self.function == other.function)
            and (self.sub_function == other.sub_function)
            and (self.intent == other.intent)
            and (self.entity_values == other.entity_values)
            and (self.entity_types == other.entity_types)
        )
