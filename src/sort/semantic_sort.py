from src.utils import ProcessData
from dotenv import load_dotenv
import spacy, json, os


class SemanticSort:
    load_dotenv()
    def __init__(self, request: str, data_path=os.getenv("FILEPATH")):
        self.__nlp = spacy.load('en_core_web_md')
        self.__request = ''.join([i for i in request if i.isalpha() or i == ' '])
        self.__data = ProcessData(data_path)


    def __fitness_score(self, target: str) -> float:
        sentence1 = self.__nlp(self.__request)
        sentence2 = self.__nlp(target)

        return sentence1.similarity(sentence2)


    def __find_focus_fitness(self, focus_vals: list, obj: dict):
        for key, topics in zip(obj, focus_vals):
            for topic in topics:
                obj[key] += self.__fitness_score(topic['name'])/len(topics)

    
    def __find_description_fitness(self, summary: list) -> dict:
        return {i['name']: self.__fitness_score(i['description'])
                for i in summary}

    
    def __json_preprocess(self, obj: dict) -> list:
        return [{"name" : key, "fitness": obj[key]} for key in obj]


    def sort_data(self, separator: int) -> dict:
        focus_vals = [i[0]['values'] for i in self.__data.parse_focus()[:separator]]
        result = self.__find_description_fitness(self.__data.parse_summary()[:separator])
        
        self.__find_focus_fitness(focus_vals, result)
        sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

        with open('result.json', 'w') as fp:
            json.dump(self.__json_preprocess(sorted_result), fp)

        return sorted_result