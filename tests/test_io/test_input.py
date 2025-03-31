import pytest
import pandas as pd
import app.io.input as input


@pytest.fixture
def sample_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("It is a test")
    return str(file_path)


@pytest.fixture
def sample_csv_file(tmp_path):
    file_path = tmp_path / "sample.csv"
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    df.to_csv(file_path, index=False)
    return str(file_path)


def test_read_from_file_success(sample_text_file):
    content = input.read_from_file(sample_text_file)
    assert content == "It is a test"


def test_read_from_file_failure():
    with pytest.raises(FileNotFoundError):
        input.read_from_file("non_existent_file.txt")


def test_read_from_file_pandas_success(sample_csv_file):
    df = input.read_from_file_pandas(sample_csv_file)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["col1", "col2"]
    assert df.shape == (3, 2)


def test_read_from_file_pandas_failure():
    with pytest.raises(FileNotFoundError):
        input.read_from_file_pandas("non_existent_file.csv")
