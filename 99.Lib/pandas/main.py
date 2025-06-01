import pandas as pd
from functools import wraps

def read_nba(func):
    @wraps(func)
    def inner(*args, **kwargs):
        nba = pd.read_csv("nba.csv")
        print(f"========= {func.__name__} =========")
        func(nba)
    return inner

def csv_reader():
    # making data frame from csv file
    df = pd.read_csv("nba.csv", index_col="Name")
    
    # retrieving row by loc method
    out = df.loc["Avery Bradley"]
    #out = df.loc["asdf"] # All NAN
    print(out)
    print("df.columns:", df.columns)
    print("nba info:", df.info())


def main():
    # * Sum method
    df = pd.read_csv("revenue.csv", index_col="Date")
    print("revenue.sum: ", df.sum())
    print("revenue.sum(index): ", df.sum(axis="index"))
    print("revenue.sum(columns): ", df.sum(axis="columns"))
    print("sum all: ", df.sum(axis="columns").sum())

    # * Select one column from a DataFrame
    print("revenue Miami:")
    print(df.Miami) # NOT work if col has space
    print("revenue New York:")
    print(df["New York"])

    # ~ it's reference. df will be changed if we change it here
    new_york_series = df["New York"]
    new_york_series.iloc[0] = 123
    print("=== refer:\n", df.head(1)) # New York[0] = 123

    # ~ full copy
    new_york_copy = df["New York"].copy()
    new_york_copy.iloc[0] = 456
    print("=== after copy:\n", df.head(1)) # New York[0] = 123

    # * Select multiple columns from a DataFrame
    nba = pd.read_csv("nba.csv")
    df_nt_copy = nba[["Name", "Team"]] # this is a copy of nba
    print("=== df_nt_copy:\n", df_nt_copy)

    # * Add new column to a DataFrame
    nba["Sport"] = "Basketball" # Add "Sport" column at the end of other columns
    print("=== After adding Sport col:\n", nba)
    nba.insert(loc=3, column="NewNum", value=123)
    print("=== After insert NewNum col:\n", nba)
    nba["DoubleSalary"] = nba["Salary"]*2
    print("=== After adding double salary col:\n", nba)

    n_unique()
    drop_nan()
    fill_nan()


@read_nba
def n_unique(nba={}):
    # * how many unique values. Reduce memory with "category"
    print("N unique:\n", nba["Team"].nunique())
    nba["Position"] = nba["Position"].astype("category")


@read_nba
def drop_nan(nba={}):
    # * Drop NAN
    #nba.dropna(how="any") # drop this row if has any NAN
    #nba.dropna(how="all") # drop this row if all col are NAN
    res = nba.dropna(subset=["College", "Salary"]) # drop this row if "College" OR "Salary" column is NAN
    print(res.tail(6))


@read_nba
def fill_nan(nba={}):
    # * Fill NAN
    nba["Salary"] = nba["Salary"].fillna(0)
    print(nba.tail(5))


def pd_categorical():
    s1 = ['a', 'a', 'b', 'd', 'c']
    s2 = [1, 4, 4, 3, 7]
    ss0 = pd.Categorical(s1, categories=['d', 'b', 'c'])
    ss1 = pd.Categorical(s1)
    ss2 = pd.Categorical(s2)

    print('ss0:', ss0)
    print('ss1:', ss1)
    print('ss2:', ss2)
    print('=============')
    print('ss0.codes:', ss0.codes)
    print('ss1.codes:', ss1.codes)
    print('ss2.codes:', ss2.codes)
    print('=============')

    ss2 = pd.Categorical(s2, ordered=True, categories=[4,3,7,1])
    print('orderd ss2:', ss2)
    print('ss2.min():', ss2.min())
    print('ss2.codes:', ss2.codes)
    print('ss2.categories:', ss2.categories)



if __name__ == "__main__":
    s = pd.Series([1, 2, 3])
    print("s.sum = ", s.sum())

    print("####################")
    #csv_reader()

    print("####################")
    main()

    print("####################")
    #pd_categorical()
