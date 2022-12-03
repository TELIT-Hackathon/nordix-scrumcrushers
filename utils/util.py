import pandas as pd


class ProcessData:

    def __init__(self, filepath="../data.json"):
        self.__filepath = filepath
        self.data = self.__open()
        self.focus_data = self.__parse_focus()
        self.portfolio_data = self.__parse_portfolio()

    def __open(self) -> pd.DataFrame:
        return pd.read_json(self.__filepath)

    def __parse_focus(self) -> pd.Series:
        return self.data.get("focus")

    def __parse_portfolio(self) -> pd.Series:
        return self.data.get("portfolio")
