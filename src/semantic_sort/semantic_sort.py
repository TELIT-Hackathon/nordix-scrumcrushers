from src.utils import ProcessData
import spacy, json


class SemanticSort:
    def __init__(self, request: str, data_path='./data.json'):
        self.__nlp = spacy.load('en_core_web_md')
        self.__request = ''.join([i for i in request if i.isalpha() or i == ' '])
        self.__data = ProcessData(data_path)


    def __fitness_score(self, item: str) -> float:
        sentence1 = self.__nlp(self.__request)
        sentence2 = self.__nlp(item)

        return sentence1.similarity(sentence2)

    
    def sort_data(self, separator: int) -> dict:
        summary = self.__data.parse_summary()[:separator]
        focus_vals = [i[0]['values'] for i in self.__data.parse_focus()[:separator]]
        result = {i['name']: self.__fitness_score(i['description'])
                for i in summary}
            
        for key, topics in zip(result, focus_vals):
            for topic in topics:
                result[key] += self.__fitness_score(topic['name'])/len(topics)

        sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

        with open('result.json', 'w') as fp:
            json.dump(sorted_result, fp)

        return sorted_result