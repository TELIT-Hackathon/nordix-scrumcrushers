from src.semantic_sort import SemanticSort
from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    request = "job for AI developers and for data scientists"

    ss = SemanticSort(request)
    print(ss.sort_data(20))