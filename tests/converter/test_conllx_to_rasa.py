from tokenizer_tools.converter.conllx_to_rasa import conllx_to_rasa

def test_conllx_to_rasa():
    rs = conllx_to_rasa('1.txt', '2.txt')
    print(rs)
