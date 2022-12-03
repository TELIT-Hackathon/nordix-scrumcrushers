from src.utils import ProcessData
from src.find_synonyms import synonym_extractor
import spacy, json


class SemanticSort:
    def __init__(self, request: str, data_path='./data.json'):
        self.__nlp = spacy.load('en_core_web_md')
        self.__requests = ''.join([i for i in request if i.isalpha() or i == ' '])
        self.__data = ProcessData(data_path)


    def __fitness_score(self, description: str) -> float:
        sentence1 = self.__nlp(self.__requests)
        sentence2 = self.__nlp(description)

        return sentence1.similarity(sentence2)

    
    def sort_data(self, separator: int) -> list:
        # descriptions = [i['description'] for i in self.__data.summary_data[:separator]]

        # return list(sorted(descriptions, 
        #               key=lambda x: self.__fitness_score(x), reverse=True))
        
        result = {i['name']: self.__fitness_score(i['description'])
                for i in self.__data.summary_data[:separator]}

        with open('result.json', 'w') as fp:
            json.dump(result, fp)

        return result
        