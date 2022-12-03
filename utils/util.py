import json
from pprint import pprint


class ProcessData:

    def __init__(self, filepath="../data.json"):
        self.__filepath: str = filepath
        self.data = self.__open()
        self.focus_data = self.__parse_focus()
        self.portfolio_data = self.__parse_portfolio()
        self.reviews_data = self.__parse_reviews()
        self.summary_data = self.__parse_summary()
        self.scores = self.__parse_scores_and_description()

    def __open(self) -> dict:
        try:
            with open(self.__filepath, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception as e:
            print(e)

    def __parse_focus(self) -> dict:
        return {idx: el["focus"] for idx, el in enumerate(self.data)}

    def __parse_portfolio(self) -> dict:
        return {idx: el["portfolio"] for idx, el in enumerate(self.data)}

    def __parse_reviews(self) -> dict:
        return {idx: el["reviews"] for idx, el in enumerate(self.data)}

    def __parse_summary(self) -> dict:
        return {idx: el["summary"] for idx, el in enumerate(self.data)}

    def __parse_scores_and_description(self) -> dict:
        return {el["name"]: (el["rating"], el["description"])
                for el in self.summary_data.values()}

