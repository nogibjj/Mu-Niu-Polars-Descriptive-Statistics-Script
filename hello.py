import matplotlib.pyplot as plt
import math
import polars as pl


def calc_mean(df, colname):
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == pl.Utf8:
        return "Mean not available for string"
    else:
        return df[colname].mean()


def calc_median(df, colname):
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == pl.Utf8:
        return "Median not available for string"
    else:
        sorted_data = df[colname].sort()
        n = len(sorted_data)
        if n % 2 == 1:
            median_val = sorted_data[n // 2]
        else:
            median_val = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        return median_val


def calc_sd(df, colname):
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == pl.Utf8:
        return "Standard Deviation not available for string"
    else:
        variance = df[colname].var()
        std = math.sqrt(variance)
        return std


def draw(df, colname):
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == pl.Utf8:
        return "Plot not available for string"
    else:
        plt.hist(df[colname].to_numpy(), bins=5)  # Convert Polars column to NumPy array
        plt.xlabel(f"{colname}")
        plt.ylabel("Frequency")
        plt.title(f"{colname} Distribution")
        plt.show()
