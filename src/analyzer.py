import pandas as pd

class Analyzer():
    def __init__(self, filepath: str | None = None) -> None:
        self.df = pd.read_csv(filepath) if filepath != None else None
    