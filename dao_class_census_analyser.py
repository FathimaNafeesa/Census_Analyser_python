import re
from census_analyser_exceptions import *
from census_analyser import *
import pandas as pd


class DAOClass(object):

    def __init__(self, column_name):

        if re.search(r'(StateName|State)', str(column_name)):
            self.State = column_name

        elif re.search(r'(StateCode|StatesID)', str(column_name)):
            self.StateCode = column_name

        elif re.search(r'(DensityPerSqKm|Density)', str(column_name)):
            self.DensityPerSqKm = column_name

        elif re.search(r'(AreaInSqKm|Total area)', str(column_name)):
            self.AreaInSqKm = column_name

        elif re.search(r'(population| population density)', str(column_name)):
            self.Population = column_name
        else:
            raise CensusAnalyserException(ExceptionType.NO_COLUMN_FOUND_MATCH, "Column unidentified")

    def get_column(self):

        column_list = [self.State, self.StateCode, self.Population, self.DensityPerSqKm, self.AreaInSqKm]
        for column_name in column_list:
            if str(column_name) in dir(self):
                return column_name
        else:
            return None


if __name__ == "__main__":
    pass
