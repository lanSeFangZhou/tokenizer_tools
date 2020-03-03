from tokenizer_tools.conllz.entity_vocabulary import entity_vocabulary

def test_entity_vovabulary():
    f = entity_vocabulary(['corpus.txt'])
    #TODO haven't deal with # sentence
    expect = {'11': ['11', 'c'],
             'a': ['1'],
             'a1': ['11'],
             'aaaa': ['#'],
             'b': ['2'],
             'b1': ['21'],
             'bbb': ['#'],
             'ccc': ['#'],
             'dddd': ['#'],
             'guojia': ['a']}
    assert f == expect
