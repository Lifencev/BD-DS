import pandas as pd


def write_to_console(data: str):
    """
    Writes input to the console.

    Args:
        data: Data to be written.
    """
    print(data)


def write_to_file(data: str, file_name: str):
    """
    Writes input to the file.

    Args:
        data: Data to be written.
        file_name: Name of the file.
    """
    with open(file_name, "w") as f:
        f.write(data)


def write_to_file_pandas(data: pd.DataFrame, file_name: str):
    """
    Writes input to the file using pandas.

    Args:
        data: Data to be written.
        file_name: Name of the file.
    """
    data.to_csv(file_name, index=False)
