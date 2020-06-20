class StateCensusDTO:
    def __init__(self, ):
        self.State = "State"
        self.Population = "Population"
        self.DensityPerSqKm = "DensityPerSqKm"
        self.AreaInSqKm = "AreaInSqKm"

    def __repr__(self):
        return self.State + "," + self.Population + "," + self.DensityPerSqKm + "," + self.AreaInSqKm


class StateCodeDTO:
    def __init__(self):
        self.State = "State Name"

    def __repr__(self):
        return self.State


class USStateCodeDTO:
    def __init__(self):
        self.State = "State"
        self.Population = "Population"
        self.AreaInSqKm = "Total area"

    def __repr__(self):
        return self.State + "," + self.Population + "," + self.AreaInSqKm
