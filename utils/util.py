import json


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

    def __parse_focus(self) -> list:
        return [el["focus"] for el in self.data]

    def __parse_portfolio(self) -> list:
        return [el["portfolio"] for el in self.data]

    def __parse_reviews(self) -> list:
        return [el["reviews"] for el in self.data]

    def __parse_summary(self) -> list:
        return [el["summary"] for el in self.data]

    def __parse_scores_and_description(self) -> dict:
        return {el["name"]: (el["rating"], el["description"])
                for el in self.summary_data}
