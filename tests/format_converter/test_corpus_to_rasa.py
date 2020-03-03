from tokenizer_tools.format_converter.corpus_to_rasa_json import CorpusToRasaJson
from tokenizer_tools.tagset.offset.corpus import Corpus

#TODO
def test_convert_to_json(datadir):
    corpus = Corpus.read_from_file( "output.conllx")
    ex = CorpusToRasaJson(corpus)
    rs = CorpusToRasaJson.convert_to_json(ex)
    print(rs)

def test_convert_to_file():
    pass
