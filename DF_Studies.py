import Data_Frames as df
import DF_Manipulation as df_mp

if __name__ == '__main__':
    dataFrame = df.dataFrame()
    dataFrameManipulation = df_mp.manipulation(dataFrame.getDataFrame())
    dataFrameManipulation = dataFrameManipulation.df_manipulation()
    dataFrameManipulation = df_mp.manipulation(dataFrame.setNewDataFrame(dataFrameManipulation))

    dataFrameManipulation.plotDataFrame()