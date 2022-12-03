class SemanticAnalyzer:
    def __init__(self, request: str):
        self.__abc = "abcdefghijklmnopqrstuvwxyz "
        self.__request = self.__preprocess_text(request)
    

    def __preprocess_text(self, text: str) -> list:
        text = text.lower()
        text = ''.join([c for c in text if c in self.__abc])

        return text.split(' ')


    def fitness_score(self, description: str) -> int:
        tmp_description = self.__preprocess_text(description)
        return len(set(tmp_description) & set(self.__request))