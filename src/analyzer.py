import pandas as pd


class Analyzer():
    def __init__(self, data: str | pd.DataFrame) -> None:
        self.df = data
        if isinstance(data, str):
            self.df = pd.read_csv(data)

        self.preprocess_data()

    def preprocess_data(self):
        # Check that we have the necesary data
        required_columns = ["Street", "Zip",
                            "City", "Company", "Last Check-In Date"]
        for column in required_columns:
            if column not in self.df.columns:
                raise Exception("missing column {}".format(column))

        self.df["Last Check-In Date"] = pd.to_datetime(
            self.df["Last Check-In Date"], format="%d/%m/%Y")

        # Logs for missing columns
        size = len(self.df.index)

        for i in range(size):
            missing_data = self.df.loc[i].isna()
            if sum(missing_data) != 0:
                print("WARNING: Missing columns " +
                      ", ".join(self.df.columns[missing_data]) +
                      " at row {}".format(i))

    def get_earliest_customer(self):
        sorted = self.df.sort_values(by="Last Check-In Date", ascending=True)
        return sorted.head(n=1)

    def get_latest_customer(self):
        sorted = self.df.sort_values(by="Last Check-In Date", ascending=False)
        return sorted.head(n=1)

    def get_customer_list(self):
        full_names = (self.df["First Name"] + " " +
                      self.df["Last Name"]).sort_values().dropna().values
        return full_names

    def get_companies_list(self):
        companies = self.df["Company"].dropna().unique()
        companies.sort()
        return companies
