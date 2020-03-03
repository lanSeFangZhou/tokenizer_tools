from tokenizer_tools.conllz.iterator_reader import read_conllx_iterator,\
    read_conllx_from_string,iterator_reader,conllx_iterator_reader,read_conllz_iterator

# iterator single file
def test_read_conllz_iterator():
    for i in read_conllz_iterator('corpus.txt'):
        print(i)

# iterator file list
def test_iterator_reader():
    for i in iterator_reader(['corpus.txt']):
        print(i)

# TODO  this style text is not expected   count
def test_read_conllx_iterator():
    for i in read_conllx_iterator('corpus1.txt'):
        print(i)

#TODO
def test_conllx_iterator_reader():
    for i in conllx_iterator_reader(['corpus1.txt']):
        print(i)
