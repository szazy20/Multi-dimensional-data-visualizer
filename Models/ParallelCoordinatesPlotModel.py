import plotly.express as px

from Interfaces.IPlot import IPlot

class ParallelCoordinatesPlotModel(IPlot):
    
    # constructor
    def __init__(self):
        None

    # getter of data field
    def getData(self):
        return __data
    
    # getter of labels field
    def getLabels(self):
        return __labels

    # setter of data field
    def setData(self, data):
        self.__data = data

    # setter of labels field
    def setLabels(self, labels):
        self.__labels = labels

    # returns ready to display plot
    def createPlot(self):
        plot = px.parallel_coordinates(
            self.__data, 
            color=list(self.__labels)[0], # to change
            dimensions=self.__labels,
            color_continuous_scale=px.colors.diverging.Tealrose,
            color_continuous_midpoint=2)

        return plot