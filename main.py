from src.semantic_sort import SemanticSort


if __name__ == '__main__':
    request = "Web Development companies"

    ss = SemanticSort(request)
    print(ss.sort_data(20))