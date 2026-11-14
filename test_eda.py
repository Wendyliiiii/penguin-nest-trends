import pandas as pd

from eda import find_yearly_changes


def test_find_yearly_changes():
    data = pd.DataFrame({
        "season_starting": [2000, 2001, 2002],
        "penguin_count": [100, 150, 120]
    })

    result = find_yearly_changes(data)

    assert list(result["count_change"]) == [50, -30]


def test_missing_years():
    data = pd.DataFrame({
        "season_starting": [2018, 2019, 2021, 2022],
        "penguin_count": [100, 150, 300, 250]
    })

    result = find_yearly_changes(data)

    assert list(result["season_starting"]) == [2019, 2022]
    assert list(result["count_change"]) == [50, -50]


def test_unsorted_years():
    data = pd.DataFrame({
        "season_starting": [2002, 2000, 2001],
        "penguin_count": [120, 100, 150]
    })

    result = find_yearly_changes(data)

    assert list(result["season_starting"]) == [2001, 2002]
    assert list(result["count_change"]) == [50, -30]


def test_original_data_unchanged():
    data = pd.DataFrame({
        "season_starting": [2000, 2001, 2002],
        "penguin_count": [100, 150, 120]
    })

    original = data.copy()

    find_yearly_changes(data)

    assert data.equals(original)


def main():
    test_find_yearly_changes()
    test_missing_years()
    test_unsorted_years()
    test_original_data_unchanged()
    print("All tests passed!")


if __name__ == "__main__":
    main()
