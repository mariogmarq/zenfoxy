import pandas as pd



class Analyzer():
    def __init__(self, filepath: str | None = None) -> None:
        self.df: pd.DataFrame | None = pd.read_csv(filepath) if filepath != None else None
        if self.df is not None:
            self.preprocess_data()
    
    def preprocess_data(self):
        if self.df is None:
            return
        
        required_columns = ["Street", "Zip", "City", "Company", "Last Check-In Date"]
        for column in required_columns:
            if column not in self.df.columns:
                raise Exception("missing column {}".format(column))
        
        self.df["Last Check-In Date"] = pd.to_datetime(self.df["Last Check-In Date"], format="%d/%m/%Y")
    

    def get_earliest_customer(self):
        if self.df is None:
            return

        sorted = self.df.sort_values(by="Last Check-In Date", ascending=True)
        return sorted.head(n=1)
    
    def get_latest_customer(self):
        if self.df is None:
            return

        sorted = self.df.sort_values(by="Last Check-In Date", ascending=False)
        return sorted.head(n=1)
    
    def get_customer_list(self):
        if self.df is None:
            return
        
        full_names = (self.df["First Name"] + " " + self.df["Last Name"]).sort_values().dropna().values
        return full_names

    def get_companies_list(self):
        if self.df is None:
            return
        
        companies = self.df["Company"].dropna().unique()
        companies.sort()
        return companies