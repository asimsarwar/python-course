import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

trainsApplication = RailwayForm()
trainsApplication.name = "Asim"
trainsApplication.train = "Green Line Express"
trainsApplication.printData()