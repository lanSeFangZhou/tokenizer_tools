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
