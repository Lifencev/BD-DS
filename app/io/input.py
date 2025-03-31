import csv

import pandas as pd


def read_from_consol():
    """
    Reads input from the console.

    Returns:
        data (str): The input read from the console.
    """
    data = str(input("Please enter the input from the console: "))
    return data


def read_from_file(file_name: str):
    """
    Reads data from a file.

    Args:
        file_name: The name of the file.

    Returns:
        data (str): The data read from the file.
    """
    with open(file_name, "r") as f:
        return f.read()


def read_from_file_pandas(file_name: str):
    """
    Reads data from a file using pandas.

    Args:
        file_name: The name of the file.

    Returns:
        data (pd.DataFrame): A pandas DataFrame containing the data read from the file.
    """
    data = pd.read_csv(file_name)
    return data
