import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def find_yearly_changes(data):
    """
    Returns nest count changes between consecutive breeding seasons.
    """
    data = data.sort_values("season_starting").copy()
    data["year_difference"] = data["season_starting"].diff()
    data["count_change"] = data["penguin_count"].diff()

    return data[data["year_difference"] == 1]


def main():
    penguins = pd.read_csv("AllCounts_V_5_0.csv")

    print(penguins.head())

    print("Number of rows:", len(penguins))
    print("Number of columns:", len(penguins.columns))
    print("Column names:", penguins.columns)

    adelie = penguins[
        (penguins["site_id"] == "BRDS")
        & (penguins["common_name"] == "adelie penguin")
        & (penguins["count_type"] == "nests")
        & (penguins["vantage"] == "aerial")
        & (penguins["season_starting"] >= 1984)
        & (penguins["season_starting"] <= 2024)
    ]

    print("Filtered rows:", len(adelie))
    print(adelie[["site_name", "season_starting", "penguin_count"]].head())

    print("Missing values in original data:")
    print(penguins.isna().sum())

    print("Missing values in filtered data:")
    print(adelie.isna().sum())

    all_years = set(range(1984, 2025))
    observed_years = set(adelie["season_starting"])
    missing_years = sorted(all_years - observed_years)

    print("Missing years:", missing_years)
    print("Nest count summary:")
    print(adelie["penguin_count"].describe())
    print("Breeding season summary:")
    print(adelie["season_starting"].describe())

    print("Categorical variable frequencies:")
    for column in ["site_name", "common_name",
                   "count_type", "vantage"]:
        print(column)
        print(adelie[column].value_counts())

    print("Duplicate breeding seasons:")
    print(adelie["season_starting"].duplicated().sum())

    years = adelie["season_starting"]
    counts = adelie["penguin_count"]
    result = stats.kendalltau(years, counts)

    print("Kendall's tau:", result.statistic)
    print("P-value:", result.pvalue)

    adelie = adelie.sort_values("season_starting")

    consecutive = adelie[
        adelie["season_starting"].diff() == 1
    ]

    previous_counts = adelie["penguin_count"].shift(1)

    lagged_counts = previous_counts.loc[consecutive.index]
    current_counts = consecutive["penguin_count"]

    lag_one_corr = current_counts.corr(lagged_counts)

    print("Lag-1 autocorrelation:", lag_one_corr)

    earlier = adelie[
        adelie["season_starting"] <= 2003
    ]

    later = adelie[
        adelie["season_starting"] >= 2004
    ]

    print("Earlier period rows:", len(earlier))
    print("Later period rows:", len(later))

    earlier_result = stats.kendalltau(
        earlier["season_starting"],
        earlier["penguin_count"]
    )

    later_result = stats.kendalltau(
        later["season_starting"],
        later["penguin_count"]
    )

    earlier_previous = earlier["penguin_count"].shift(1)
    earlier_consecutive = earlier[
        earlier["season_starting"].diff() == 1
    ]

    earlier_corr = earlier_consecutive["penguin_count"].corr(
        earlier_previous.loc[earlier_consecutive.index]
    )

    later_previous = later["penguin_count"].shift(1)
    later_consecutive = later[
        later["season_starting"].diff() == 1
    ]

    later_corr = later_consecutive["penguin_count"].corr(
        later_previous.loc[later_consecutive.index]
    )

    print("Earlier lag-1 correlation:", earlier_corr)
    print("Later lag-1 correlation:", later_corr)
    print("Earlier Kendall's tau:", earlier_result.statistic)
    print("Earlier p-value:", earlier_result.pvalue)
    print("Later Kendall's tau:", later_result.statistic)
    print("Later p-value:", later_result.pvalue)

    earlier_slope = stats.theilslopes(
        earlier["penguin_count"],
        earlier["season_starting"]
    )

    later_slope = stats.theilslopes(
        later["penguin_count"],
        later["season_starting"]
    )

    print("Earlier Theil-Sen slope:", earlier_slope.slope)
    print("Earlier slope CI:", earlier_slope.low_slope,
          earlier_slope.high_slope)

    print("Later Theil-Sen slope:", later_slope.slope)
    print("Later slope CI:", later_slope.low_slope,
          later_slope.high_slope)

    adelie = adelie.sort_values("season_starting")

    plot_data = adelie.set_index("season_starting")
    plot_data = plot_data.reindex(range(1984, 2025))

    plt.plot(
        plot_data.index,
        plot_data["penguin_count"],
        marker="o"
    )

    plt.title("Adélie Penguin Nest Counts at Cape Bird South")
    plt.xlabel("Breeding Season (Starting Year)")
    plt.ylabel("Number of Nests")

    plt.tight_layout()
    plt.savefig("penguin_trend.png")
    plt.show()

    plt.figure()

    sns.histplot(
        data=adelie,
        x="penguin_count",
        bins=10
    )

    plt.title("Distribution of Adélie Penguin Nest Counts")
    plt.xlabel("Number of Nests")
    plt.ylabel("Number of Breeding Seasons")

    plt.tight_layout()
    plt.savefig("penguin_distribution.png")
    plt.show()

    consecutive_changes = find_yearly_changes(adelie)

    print("Year-to-year changes:")
    print(consecutive_changes[
        ["season_starting", "count_change"]
    ].head())

    biggest_increase = consecutive_changes.loc[
        consecutive_changes["count_change"].idxmax()
    ]

    biggest_decrease = consecutive_changes.loc[
        consecutive_changes["count_change"].idxmin()
    ]

    print("Biggest increase:")
    print(biggest_increase[
        ["season_starting", "count_change"]
    ])

    print("Biggest decrease:")
    print(biggest_decrease[
        ["season_starting", "count_change"]
    ])


if __name__ == "__main__":
    main()
