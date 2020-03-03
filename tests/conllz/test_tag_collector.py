from tokenizer_tools.conllz.tag_collector import tag_collector, collect_tag_to_file, \
entity_collector,collect_entity_to_file,label_collector,extra_attr_collector,collect_extra_attr_to_file,\
collect_label_to_file

def test_tag_collector():
    # TODO what is the structure of this inputfiles?
    s = tag_collector(['corpus.txt'])
    print(s)

def test_collect_tag_to_file():
    collect_tag_to_file(['corpus3.txt'], 'corpus4.txt')

def test_entity_collector():
    s = entity_collector(['corpus3.txt'])
    print(s)

def test_collect_entity_to_file():
    entity_collector(['corpus3.txt'])

def test_label_collector():
    s = label_collector(['corpus3.txt'])

def test_extra_attr_collector():
    extra_attr_collector(['corpus3.txt'])

def test_collect_extra_attr_to_file():
    collect_extra_attr_to_file(['corpus3.txt'], 'corpus4.txt')

def test_collect_label_to_file():
    collect_label_to_file(['corpus3.txt'], 'corpus4.txt')
