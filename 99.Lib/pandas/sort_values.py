import pandas as pd

def main():
    df = pd.read_csv("my.csv")
    print("====== Original ======")
    print(df)

    print("\n====== sort_values('name'):")
    print(df.sort_values("name"))

    print("\n====== sort_values(['name', 'age', 'number']):")
    # * sort by "name", then by "age", then by "number"
    print(df.sort_values(["name", "age", "number"]))

if __name__ == "__main__":
    main()
