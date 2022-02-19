import requests
import pandas as pd
from typing import cast

results = []

READABLE_FILE_PARAMS = {
    "file_okay": True,
    "dir_okay": False,
    "path_type": "Path",
}


def get_fips_data(row) -> str:
    """Get FIPS data for a row in the dataframe column.
    We constrain this operation to a method so we can map over each row in the
    DataFrame.
    Args:
        row: The row to retrieve FIPS information for.
    Returns:
       The FIPS string for the given row.
    """
    url = "https://geo.fcc.gov/api/census/block/find"

    # Get response from API
    payload = {
        "latitude": row["lat_tract"],
        "longitude": row["long_tract"],
        "format": "json",
    }
    response = requests.get(url, params=payload)

    # Parse json in response
    data = response.json()
    return data["County"]["FIPS"]


def augment_fips() -> None:
    """Augment a CSV with FIPS information.
    This script will read from INPUT_FNAME and write the augmented CSV to OUTPUT_FNAME.
    """
    input_fname = "urbanization-census-tract.csv"
    output_fname = "urbanization-census-tract-updated.csv"
    df = cast(pd.DataFrame, pd.read_csv(input_fname))
    df["lat_tract"] = df["lat_tract"].astype(float)
    df["long_tract"] = df["long_tract"].astype(float)

    # Map over each row to get FIPS data.
    df["FIPS"] = df.apply(get_fips_data, axis=1)
    df.to_csv(output_fname)


if __name__ == "__main__":
    augment_fips()