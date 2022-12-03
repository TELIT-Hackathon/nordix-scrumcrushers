import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')


def synonym_extractor(phrase: str) -> set:
    return {l.name() for syn in nltk.corpus.wordnet.synsets(phrase) for l in syn.lemmas()}


print(synonym_extractor("Collection"))
