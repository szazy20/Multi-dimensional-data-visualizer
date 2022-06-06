from Helpers.File import File
from Helpers.DataVerificator import DataVerificator
from Models.ParallelCoordinatesPlotModel import ParallelCoordinatesPlotModel
from Views.ParallelCoordinatesPlotView import ParallelCoordinatesPlotView
import tkinter as tk

# controls program flow
class ParallelCoordinatesPlotController: 
   
   # constructor
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("MD-Conv")
        self.__view = ParallelCoordinatesPlotView(self.__root)
        self.__model = ParallelCoordinatesPlotModel()
        self.__view.runAppBtn.bind("<Button-1>", lambda event: self.__initProgram())

    # runs the GUI
    def run(self):
        self.__root.mainloop()

    # starts execution process of getting parallel coordinates plot
    def __initProgram(self):
        self.__file = File(self.__view.getFileName())
        dv = DataVerificator()

        res = self.__file.verifyFile()
        if(res == None):
            res = dv.verifyData(self.__view.getFileName())
            if(res == True):
                if(self.__view.getPlotType() == "ParallelCoordinates"):
                    self.__execute()
                else:
                    self.__view.openPopup(self.__root, "Info", "Option is not implemented")
            else:
                if(self.__view.handleInvalidInput() == True):
                    self.__execute()
        else:
            self.__view.openPopup(self.__root, "File verification error", res)
        
    # executes reading from file and further operations
    def __execute(self):
        self.__file.readCsvData()
        data = self.__file.getData()
        labels = self.__file.getLabels()
        self.__model.setData(data)
        self.__model.setLabels(labels)
        self.__view.displayPlot(self.__model.createPlot())