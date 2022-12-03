from src.utils import ProcessData
from src.find_synonyms import synonym_extractor
from random import choice
import spacy, random


class SemanticSort:
    def __init__(self, request: str, data_path='./data.json'):
        self.__nlp = spacy.load('en_core_web_md')
        self.__requests = ''.join([i for i in request if i.isalpha() or i == ' '])
        self.__data = ProcessData(data_path)


    def __fitness_score(self, description: str) -> float:
        sentance1 = self.__nlp(self.__requests)
        sentance2 = self.__nlp(description)

        return sentance1.similarity(sentance2)

    
    def sort_data(self, separator: int) -> list:
        # descriptions = [i['description'] for i in self.__data.summary_data[:separator]]

        # return list(sorted(descriptions, 
        #               key=lambda x: self.__fitness_score(x), reverse=True))
        return {i['name']: self.__fitness_score(i['description']) for i in self.__data.summary_data[:separator]}