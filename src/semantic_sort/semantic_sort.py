from src.utils import ProcessData
import spacy


class SemanticSort:
    def __init__(self, request: str, data_path='./data.json'):
        self.__nlp = spacy.load('en_core_web_md')
        self.__request = request
        self.__data = ProcessData(data_path)


    def __fitness_score(self, description: str) -> float:
        sentance1 = self.__nlp(self.__request)
        sentance2 = self.__nlp(description)

        return sentance1.similarity(sentance2)

    
    def sort_data(self, separator: int) -> list:
        sorted_data = list(sorted(self.__data.summary_data[:separator], 
                      key=lambda x: self.__fitness_score(x['description']), reverse=True))

        return [i['name'] for i in sorted_data]