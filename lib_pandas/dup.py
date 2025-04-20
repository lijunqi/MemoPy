import pandas as pd

def main():
    df = pd.read_csv("my.csv")
    print("====== Original ======")
    print(df)

    print("\n====== drop_duplicates():")
    # * drop if all cols value are identical
    # * keep first item
    print(df.drop_duplicates())

    print("\n====== drop_duplicates('name'):")
    # * Remove rows if "name" is identical
    print(df.drop_duplicates("name"))

    print("\n====== drop_duplicates('name', keep=False):")
    # * Remove rows occur more than once, only unique rows keep
    print(df.drop_duplicates("name", keep=False))

    print("\n====== drop_duplicates(['name', 'age']):")
    # * Remove rows which both "name" and "age" are identical
    print(df.drop_duplicates(["name", "age"]))

if __name__ == "__main__":
    main()
