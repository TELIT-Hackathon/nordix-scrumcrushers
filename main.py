from src.semantic_sort import SemanticSort

if __name__ == '__main__':
    request = "Introduce your business and what you do there.\n\nI'm the founder and CEO of Riskwolf, a Zurich-based insurtech startup."

    ss = SemanticSort(request)
    print(ss.sort_data(5))