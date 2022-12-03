class SemanticAnalyzer:
    def __init__(self, description: str, request: str):
        self.__abc = "abcdefghijklmnopqrstuvwxyz"
        self.description = self.__preprocess_text(description)
        self.request = self.__preprocess_text(request)
    

    def __preprocess_text(self, text: str):
        text = text.lower()
        text = ''.join([c for c in text if c in self.__abc])

        return text.split('')
    

if __name__ == '__main__':
    description = 'Seven Peaks is a world-class technology company specializing in digital transformation for companies worldwide, delivering scalable software solutions and experience design, aimed at driving business impact.\nWe are based in Bangkok, Thailand, with a growing team of more than 200 industry professionals from over 25 different countries currently providing engineering-led services in native mobile app development, web technology, UX/UI design and more.\n \nSeven Peaks recently acquired Morphosis, one of the leading UX/UI design companies in Thailand which is now part of the Seven Peaks group.\nFor more information please visit https://sevenpeakssoftware.comRead more...'
    request = "Introduce your business and what you do there.\n\nI'm the founder and CEO of Riskwolf, a Zurich-based insurtech startup."
    
    sa = SemanticAnalyzer(description, request)
    print(description)