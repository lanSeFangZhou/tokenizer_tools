import copy

from tokenizer_tools.tagset.offset.sequence import Sequence


class Document(Sequence):
    @property
    def intent(self):
        return self.extra_attr.get("intent")

    @intent.setter
    def intent(self, intent):
        self.extra_attr["intent"] = intent

    @property
    def function(self):
        return self.extra_attr.get("function")

    @function.setter
    def function(self, function):
        self.extra_attr["function"] = function

    @property
    def sub_function(self):
        return self.extra_attr.get("sub_function")

    @sub_function.setter
    def sub_function(self, sub_function):
        self.extra_attr["sub_function"] = sub_function

    @property
    def domain(self):
        return self.extra_attr.get("domain")

    @domain.setter
    def domain(self, domain):
        self.extra_attr["domain"] = domain

    @property
    def entities(self):
        return self.span_set

    @entities.setter
    def entities(self, entities):
        self.span_set = entities

    def convert_to_md(self) -> str:
        text_list = copy.deepcopy(self.text)

        for span in self.entities:
            text_list[span.start] = "[" + text_list[span.start]
            text_list[span.end - 1] = text_list[span.end - 1] + "]({})".format(
                span.entity
            )

        return " ".join(text_list)

    def __str__(self):
        return "<D: {domain}, F: {function}, S: {sub_function}, I: {intent}>    {body}".format(
            domain=self.domain,
            function=self.function,
            sub_function=self.sub_function,
            intent=self.intent,
            body=self.convert_to_md(),
        )

    def compare_entities(self, other):
        return self.text == other.text and self.span_set == other.span_set