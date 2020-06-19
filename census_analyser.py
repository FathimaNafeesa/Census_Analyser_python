from dao_class_census_analyser import *
import pandas as pd


class StateCensusLoader:
    def __init__(self, ):
        self.State = "State"
        self.Population = "Population"
        self.DensityPerSqKm = "DensityPerSqKm"
        self.AreaInSqKm = "AreaInSqKm"
        self.data_frame = None

    def __repr__(self):
        return self.State + "," + self.Population + "," + self.DensityPerSqKm + "," + self.AreaInSqKm

    def __call__(self, file_path):
        try:
            column_list = repr(StateCensusLoader()).split(",")
            self.data_frame = pd.read_csv(file_path, usecols=column_list)
            return self.data_frame
        except IOError:
            check_exceptions_type(file_path)


class StateCodeLoader:
    def __init__(self):
        self.SrNo = "SrNo"
        self.State = "State"
        self.StateCode = "StateCode"
        self.TIN = "TIN"

    def __repr__(self):
        return self.SrNo + "," + self.State + "," + self.StateCode + "," + self.TIN

    def __call__(self, file_path):
        try:
            column_list = repr(StateCodeLoader).split(",")
            self.data_frame = pd.read_csv(file_path, usecols=column_list)
            return self.data_frame
        except IOError:
            check_exceptions_type(file_path)


class USStateCodeLoader:
    def __init__(self):
        self.State_id = "State Id"
        self.State = "State"
        self.Population = "Population"
        self.Housing_units = "Housing units"
        self.Total_area = "Total area"
        self.Water_area = "Water area"
        self.Land_area = "Land area"
        self.Population_density = "Population Density"
        self.Housing_density = "Housing Density"

    def __repr__(self):
        return self.State_id + "," + self.State + "," + self.Population + "," + self.Housing_units + "," \
               + self.Total_area + "," + self.Water_area + "," + self.Land_area + "," + self.Population_density + "," \
               + self.Housing_density

    def __call__(self, file_path):
        try:
            column_list = repr(USStateCodeLoader()).split(",")
            print(column_list)
            self.data_frame = pd.read_csv(file_path, usecols=column_list)

            print(self.data_frame)
            return self.data_frame
        except IOError:
            check_exceptions_type(file_path)


class CSVHandler(StateCensusLoader, StateCodeLoader, USStateCodeLoader):

    @staticmethod
    def get_number_of_record(census_file):
        number_of_records = census_file.last_valid_index()
        return number_of_records + 1

    @staticmethod
    def sort_data_frame(census_file, column_name, order=True):
        sorted_data = census_file.sort_values(column_name, ascending=order)
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
    def __init__(self, class_name, file_path):
        variable = class_name()
        self.data_frame = variable(file_path)

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
        return CSVHandler.sort_data_frame(self.data_frame, 'AreaInSqKm', False)


obj = CensusAnalyser(USStateCodeLoader, 'CSV_files/USCensusData (1).csv')

obj.get_number_of_records()
obj.sort_in_alphabetical_order()
obj.get_map_of_state_and_census_data()
obj.sort_according_to_population_density()
