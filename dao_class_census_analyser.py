import re
from census_analyser_exceptions import *


class DAOClass(object):

    def __init__(self, columnList):

        if re.search(r'(StateName|State)', str(columnList)):
            self.State = columnList

        elif re.search(r'(StateCode|StatesID)', str(columnList)):
            self.StateCode = columnList

        elif re.search(r'(DensityPerSqKm|Density)', str(columnList)):
            self.DensityPerSqKm = columnList

        elif re.search(r'(AreaInSqKm|Total area)', str(columnList)):
            self.area = columnList

        elif re.search(r'(population| population density)', str(columnList)):
            self.population = columnList
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