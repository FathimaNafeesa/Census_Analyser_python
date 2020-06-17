import re
from census_analyser_exceptions import *


class DAOClass(object):

    def __init__(self, column_name):

        if re.search(r'(StateName|State)', str(column_name)):
            self.State = column_name

        elif re.search(r'(StateCode|StatesID)', str(column_name)):
            self.StateCode = column_name

        elif re.search(r'(DensityPerSqKm|Density)', str(column_name)):
            self.DensityPerSqKm = column_name

        elif re.search(r'(AreaInSqKm|Total area)', str(column_name)):
            self.area = column_name

        elif re.search(r'(population| population density)', str(column_name)):
            self.population = column_name
        else:
            raise CensusAnalyserException()

    def getColumn(self):

        if 'State' in dir(self):
            return self.State
        elif 'StateCode' in dir(self):
            return self.StateCode
        elif 'population' in dir(self):
            return self.population
        elif 'DensityPerSqKm' in dir(self):
            return self.DensityPerSqKm
        elif 'DensityPerSqKm' in dir(self):
            return self.DensityPerSqKm
        elif 'area' in dir(self):
            return self.area
        else:
            return None


if __name__ == "__main__":
    pass