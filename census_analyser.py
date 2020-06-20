import pandas as pd

from census_analyser_adapter import CensusAdapter
from dto_class_census import *
from census_analyser_exceptions import *


class CensusDataLoader:

    def __call__(self, file_path, dto):
        column_list = repr(dto()).split(",")
        try:
            self.data_frame = pd.read_csv(file_path, sep=",", usecols=column_list)
            self.data_frame = CensusAdapter.get_dao_data_frame(str(dto), self.data_frame)
            return self.data_frame
        except FileNotFoundError:
            check_exceptions_type(file_path)
        except ValueError:
            raise CensusAnalyserException(ExceptionType.DELIMITER_ERROR, "Wrong delimiter")


class CSVHandler(CensusDataLoader):

    @staticmethod
    def get_number_of_record(census_data_frame):
        return census_data_frame.shape[0]

    @staticmethod
    def sort_data_frame(census_data_frame, column_name, order=True):
        sorted_data = census_data_frame.sort_values(column_name, ascending=order)
        sorted_data.to_json(
            r'C:\Users\FATHIMA\PycharmProjects\Census-Analyser\sorted_json_files\stateCensusSorted.json')
        return sorted_data

    @staticmethod
    def get_map_of_state_and_census_file(data_frame, format_of_file):
        dictionary = data_frame.to_dict()
        json_file = data_frame.to_json()
        csv_file = data_frame.to_csv()

        def get_map(format_of_file_=format_of_file):
            switcher = {
                0: dictionary,
                1: json_file,
                2: csv_file
            }
            return switcher[format_of_file_]

        return get_map()


class CensusAnalyser:
    def __init__(self, file_path, dto):
        variable = CensusDataLoader()
        self.data_frame = variable(file_path, dto)

    def get_number_of_records(self):
        return CSVHandler.get_number_of_record(self.data_frame)

    def sort_in_alphabetical_order(self):
        return CSVHandler.sort_data_frame(self.data_frame, 'State')

    def get_map_of_state_and_census_data(self):
        print("Select the required format: \n 1.Dictionary \n 2.json \n 3.csv")
        format_of_file = int(input("Format required:"))
        return CSVHandler.get_map_of_state_and_census_file(self.data_frame, format_of_file)

    def sort_according_to_population_density(self):
        return CSVHandler.sort_data_frame(self.data_frame, 'Population')

    def sort_according_to_area(self):
        return CSVHandler.sort_data_frame(self.data_frame, 'AreaInSqKm',
                                          False)  # boolean is for specifying the order of sort(default true)

    def to_find_most_populous_state(self):
        sorted_data = CSVHandler.sort_data_frame(self.data_frame, 'Population')
        return sorted_data.iloc[0]


obj_1 = CensusAnalyser('CSV_files/USCensusData (1).csv', USStateCodeDTO)
print(obj_1.to_find_most_populous_state())
obj_1.get_map_of_state_and_census_data()