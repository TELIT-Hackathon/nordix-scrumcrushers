from src.semantic_sort import SemanticAnalyzer

if __name__ == '__main__':
    request = "Introduce your business and what you do there.\n\nI'm the founder and CEO of Riskwolf, a Zurich-based insurtech startup."

    a = [{
            'name': 'abcd',
            'description': 'Seven Peaks is a world-class technology company specializing in digital transformation for companies worldwide, delivering scalable software solutions and experience design, aimed at driving business impact.\nWe are based in Bangkok, Thailand, with a growing team of more than 200 industry professionals from over 25 different countries currently providing engineering-led services in native mobile app development, web technology, UX/UI design and more.\n \nSeven Peaks recently acquired Morphosis, one of the leading UX/UI design companies in Thailand which is now part of the Seven Peaks group.\nFor more information please visit https://sevenpeakssoftware.comRead more...'
        },
        {
            'name': 'fdsifjws',
            'description': "Introduce your business and what you do there.\n\nI'm the"
        }]

    sa = SemanticAnalyzer(request)
    print(sorted(a, key=lambda x: sa.fitness_score(x['description']), reverse=True))