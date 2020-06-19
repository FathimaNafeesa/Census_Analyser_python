import re
from census_analyser_exceptions import *
from census_analyser import *
import pandas as pd


class DAOClass(object):

    def __init__(self):
        self.State = "State"
        self.StateCode = "StateCode"
        self.DensityPerSqKm = "DensityPerSqKm"
        self.AreaInSqKm = "AreaInSqKm"
        self.Population = "Population"
        self.Housing_units = "Housing units"
        self.Total_area = "Total area"
        self.Water_area = "Water area"
        self.Land_area = "Land area"

    def get_column(self):

        column_list = [self.State, self.StateCode, self.Population, self.DensityPerSqKm, self.AreaInSqKm,
                       self.Housing_units, self.Total_area, self.Water_area, self.Land_area]
        for column_name in column_list:
            if str(column_name) in dir(self):
                return column_name


if __name__ == "__main__":
    pass
