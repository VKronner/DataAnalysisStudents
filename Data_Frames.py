from mostlyai import MostlyAI
import constants as const
import pandas as pd

class dataFrame():
    def __init__(self):
        self.mydataFrame = pd.DataFrame()
        mostly = MostlyAI(api_key=const.API_KEY)

        sd = mostly.synthetic_datasets.get(const.DATASET_CODE)
        config = sd.config()
        config

        self.mydataFrame = pd.DataFrame(sd.data())
    def getDataFrame(self):
        return self.mydataFrame

    def setNewDataFrame(self, dataFrame):
        self.mydataFrame = dataFrame

        return self.mydataFrame