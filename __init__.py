

try:
    print("Initializing the Python Package for Natural Language Processing")
    import PorterStemmer
    import Preprocess
    import NaiveBayes
    from ModelEval import ModelEvalution

    import_error = None

except Exception as ex:
    import_error = ex

def test_import_nlp():
    assert import_error is None
