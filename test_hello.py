import polars as pl
from hello import calc_mean, calc_median, calc_sd, draw

dataframe = None
try:
    dataframe = pl.read_csv("student_performance.csv")
except FileNotFoundError:
    pass


def test_df_exists():
    assert (
        dataframe is not None
    ), "DataFrame was not loaded. Check if 'student_performance.csv' exists."


def test_calc_mean():
    if dataframe is not None:
        for colname in dataframe.columns:
            if dataframe[colname].dtype != pl.Utf8:
                assert calc_mean(dataframe, colname) == dataframe[colname].mean()
            else:
                assert calc_mean(dataframe, colname) == "Mean not available for string"


def test_calc_median():
    if dataframe is not None:
        for colname in dataframe.columns:
            if dataframe[colname].dtype != pl.Utf8:
                assert calc_median(dataframe, colname) == dataframe[colname].median()
            else:
                assert (
                    calc_median(dataframe, colname) == "Median not available for string"
                )


def test_calc_sd():
    if dataframe is not None:
        for colname in dataframe.columns:
            if dataframe[colname].dtype != pl.Utf8:
                assert calc_sd(dataframe, colname) == dataframe[colname].std()
            else:
                assert (
                    calc_sd(dataframe, colname)
                    == "Standard Deviation not available for string"
                )


def test_draw():
    if dataframe is not None:
        for colname in dataframe.columns:
            if dataframe[colname].dtype == pl.Utf8:
                assert draw(dataframe, colname) == "Plot not available for string"


if __name__ == "__main__":
    test_df_exists()
    test_calc_mean()
    test_calc_median()
    test_calc_sd()
    test_draw()
