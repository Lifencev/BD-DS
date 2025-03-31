import app.io.input as input
import app.io.output as output


def main():
    pass


if __name__ == '__main__':

    data_from_console = input.read_from_consol()
    output.write_to_console(data_from_console)

    input_file_name = "D:\Coding\PythonProject\project_template\data\input_file.csv"
    data_from_file = input.read_from_file(input_file_name)

    output_file_name = "D:\Coding\PythonProject\project_template\data\output_file.csv"
    output.write_to_file(data_from_file, output_file_name)

    input_file_name_pandas = "D:\Coding\PythonProject\project_template\data\input_file_pandas.csv"
    data_from_file_pandas = input.read_from_file(input_file_name_pandas)

    output_file_name_pandas = "D:\Coding\PythonProject\project_template\data\output_file_pandas.csv"
    output.write_to_file_pandas(data_from_file_pandas, output_file_name_pandas)
