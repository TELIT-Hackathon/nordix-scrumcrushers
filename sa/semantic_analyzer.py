class SemanticAnalyzer:
    def __init__(self, description: str, request: str):
        self.__abc = "abcdefghijklmnopqrstuvwxyz "
        self.__description = self.__preprocess_text(description)
        self.__request = self.__preprocess_text(request)
    

    def __preprocess_text(self, text: str) -> list:
        text = text.lower()
        text = ''.join([c for c in text if c in self.__abc])

        return text.split(' ')
    

    def fitness_score(self) -> int:
        return len(set(self.__description) & set(self.__request))