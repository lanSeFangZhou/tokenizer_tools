from tokenizer_tools.tagset.offset.span import Span
from tokenizer_tools.tagset.offset.span_set import SpanSet


def test_check_overlap():
    span_set = SpanSet()
    span_set.append(Span(1, 2, 'entity'))
    span_set.append(Span(2, 3, 'entity'))
    assert span_set.check_overlap() == True

    span_set = SpanSet()
    span_set.append(Span(1, 2, 'entity'))
    span_set.append(Span(4, 6, 'entity'))
    assert span_set.check_overlap() == True

    span_set = SpanSet()
    span_set.append(Span(1, 4, 'entity'))
    span_set.append(Span(2, 3, 'entity'))
    assert span_set.check_overlap() == False


def test_eq_():
    a = SpanSet()
    a.append(Span(1, 2, 'entity'))
    a.append(Span(2, 3, 'entity'))

    b = SpanSet()
    b.append(Span(1, 2, 'entity'))
    b.append(Span(2, 3, 'entity'))

    assert a == b

    c = SpanSet()  # empty SpanSet

    assert a != c

    d = SpanSet()  # same with `a` but different span order
    d.append(Span(2, 3, 'entity'))
    d.append(Span(1, 2, 'entity'))

    assert a == d

    e = SpanSet()  # same with `a` but different span order
    e.append(Span(0, 1, 'entity'))
    e.append(Span(1, 2, 'entity'))

    assert a != e
