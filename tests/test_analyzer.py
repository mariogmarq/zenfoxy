from analyzer import Analyzer
import pandas as pd

def test_earliest_customer():
    analyzer = Analyzer("sample.csv")
    customer: pd.DataFrame = analyzer.get_earliest_customer()
    assert customer["First Name"].values[0] == "Anselmo"

def test_latest_customer():
    analyzer = Analyzer("sample.csv")
    customer: pd.DataFrame = analyzer.get_latest_customer()
    assert customer["First Name"].values[0] == "Bjorn"

def test_list_customers():
    analyzer = Analyzer("sample.csv")
    list = analyzer.get_customer_list()
    
    for i in range(1, len(list)):
        assert list[i-1] < list[i]