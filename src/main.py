if __name__ == "__main__":
    import argparse
    import analyzer

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    an = analyzer.Analyzer(args.file)

    print("List of companies in the data: ")
    print(", ".join(an.get_companies_list()))
    print("\n ")

    print("List of customers in the data: ")
    print(", ".join(an.get_customer_list()))
    print("\n ")

    print("Earliest customer in the data: ")
    earliest = an.get_earliest_customer()
    print("{} {} with check-In date {}\n".
    format(
        earliest["First Name"].values[0],
        earliest["Last Name"].values[0],
        earliest["Last Check-In Date"].values[0]
        ))

    print("Latest customer in the data: ")
    latest = an.get_latest_customer()
    print("{} {} with check-In date {}".
    format(
        latest["First Name"].values[0],
        latest["Last Name"].values[0],
        latest["Last Check-In Date"].values[0]
        ))
