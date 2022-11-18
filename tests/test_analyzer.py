from analyzer import Analyzer
import pandas as pd

def test_earliest_customer():
    analyzer = Analyzer("sample.csv")
    customer: pd.DataFrame = analyzer.get_earliest_customer()
    print(customer)
    assert customer["First Name"].values[0] == "Anselmo"