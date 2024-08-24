import pandas as pd


def csv_reader():
    # making data frame from csv file
    df = pd.read_csv("nba.csv", index_col="Name")
    
    # retrieving row by loc method
    out = df.loc["Avery Bradley"]
    #out = df.loc["asdf"] # All NAN
    print(out)
    print("df.columns:", df.columns)
    print("nba info:", df.info())

def revenue():
    df = pd.read_csv("revenue.csv", index_col="Date")
    print("revenue.sum: ", df.sum())
    print("revenue.sum(index): ", df.sum(axis="index"))
    print("revenue.sum(columns): ", df.sum(axis="columns"))
    print("sum all: ", df.sum(axis="columns").sum())

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


def main():
    old_report = pd.read_csv('summary.csv')
    old_report["summary"] = old_report["summary"].astype(str)
    old_report["ExceptionalRational"] = old_report["ExceptionalRational"].astype(str)
    old_report.loc[(old_report["summary"] == "nan"), "summary"] = ""
    old_report.loc[(old_report["ExceptionalRational"] == "nan"), "ExceptionalRational"] = ""
    print(old_report)


if __name__ == "__main__":
    s = pd.Series([1, 2, 3])
    print("s.sum = ", s.sum())
    #csv_reader()
    revenue()
    #pd_categorical()
    #main()
