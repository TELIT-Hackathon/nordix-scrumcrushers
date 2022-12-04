from src import MainSort


if __name__ == '__main__':
    request = "job for AI developers and for data scientists"

    ss = MainSort(request)
    print(ss.sort_data(20, 5))