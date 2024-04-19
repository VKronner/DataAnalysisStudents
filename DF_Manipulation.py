import Data_Frames as df
import constants as const
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

class manipulation ():
    def __init__(self,dataFrame):
        self.myDF = dataFrame


    def getShape(self):
        print(self.myDF)

    def checkMissingValues(self):
        return self.myDF.isna().sum()
        # Checks if there is missing values in the DataFrame
        # Result 0
    def checkDuplicateValues(self):
        return self.myDF.duplicated().sum()
        # Checks if there is duplicated Values inside the DataFrame
        # Result 42566 from 1000000 of cases. Resulting in 4.25% of repetition.

    def checkNullableValues(self):
        return self.myDF.info()
        # Get all info about the DataFrame
        # No Null value, 8 columns and 1000000 of cases.

    def checkUniqueValues(self):
        return self.myDF.nunique()
        # Get all Unique Values that appear in the DataFrame
        # Affirms the right content inside the DataFrame

    def exploratoryAnalysis(self):
        print("Categories in Gender Variable: ",end=" ")
        print(self.myDF['gender'].unique())

        print("Categories in Race Ethnicity Variable: ", end=" ")
        print(self.myDF['race_ethnicity'].unique())

        print("Categories in Parental Level of Education Variable: ", end=" ")
        print(self.myDF['parental_level_of_education'].unique())

        print("Categories in Lunch Variable: ", end=" ")
        print(self.myDF['lunch'].unique())

        print("Categories in Test Preparation Course Variable: ", end=" ")
        print(self.myDF['test_preparation_course'].unique())

        # Show options inside the Writting Categories.

        numeric_features = [feature for feature in self.myDF.columns if self.myDF[feature].dtype != 'string']
        categorical_features = [feature for feature in self.myDF.columns if self.myDF[feature].dtype == 'string']

        print("We have {} numerical features: {}".format(len(numeric_features), numeric_features))
        print("We have {} categorical features: {}".format(len(categorical_features), categorical_features))

        # Show types of categories and how many of each type we have

    def df_manipulation(self):
        self.myDF['total score'] = (self.myDF['math_score'] +
                                    self.myDF['reading_score'] +
                                    self.myDF['writing_score'])

        self.myDF['average'] = self.myDF['total score']/3

        return self.myDF

    def numberOfPerfectScores(self):
        reading_perfect = self.myDF[self.myDF['reading_score'] == 100]['average'].count()
        writing_perfect = self.myDF[self.myDF['writing_score'] == 100]['average'].count()
        math_perfect = self.myDF[self.myDF['math_score'] == 100]['average'].count()

        print(f'Number of Students that had a perfect score in Reading: {reading_perfect}')
        print(f'Number of Students that had a perfect score in Writing: {writing_perfect}')
        print(f'Number of Students that had a perfect score in Math: {math_perfect}')

        # 424 got 100 in Reading
        # 46 got 100 in Writing
        # 0 got 100 in Math

    def plotDataFrame(self):
        # sns.set(style="whitegrid")
        # df = sns.load_dataset(self.myDF)
        sns.pairplot(self.myDF, hue='gender')
        plt.show()