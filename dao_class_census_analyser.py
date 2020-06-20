class DAOClass:

    def __init__(self, dto):
        self.State = "States"
        self.Population = "Population"
        self.AreaInSqKm = "AreaInSqKm"
        self.DensityPerSqKm = "DensityPerSqKm"
        self.Population_density = "Population Density"
        self.dto = dto

    def __repr__(self):
        if self.dto == "StateCensusDTO":
            return self.State + ',' + self.Population + ',' + self.AreaInSqKm + ',' + self.DensityPerSqKm
        elif self.dto == "StateCodeDTO":
            return self.State
        else:
            return self.State + "," + self.Population + "," + self.AreaInSqKm

