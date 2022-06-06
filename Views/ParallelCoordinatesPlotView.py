import tkinter as tk
from tkinter import filedialog

from matplotlib.pyplot import margins

# class represents view of a parallel coordinates plot (in future it will serve GUI)
class ParallelCoordinatesPlotView:
        
    #constructor
    def __init__(self, master):
        canvas = tk.Canvas(master, height=200, width=310, bg="#6E46F2")
        canvas.pack()

        frame = tk.Frame(master, bg="#342173")
        frame.place(relwidth=1, relheight=1)

        self.runAppBtn = tk.Button(frame, text="Visualize", padx = 20, pady = 10, fg="white", bg="#34CB73")
        self.runAppBtn.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

        openFileBtn = tk.Button(frame, text="Choose File", padx = 20, pady = 10, fg="black", bg="#744AFF", command=self.chooseInputFile)
        openFileBtn.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

        values = ["ParallelCoordinates", "--", "---"]
        variable = tk.StringVar(frame)
        variable.set(values[0])

        select = tk.OptionMenu(frame, variable, *values, command=self.__setPlotType)
        select.place(relx=0.5, rely=0.80, anchor=tk.CENTER)
        self.__plotType = values[0]

        master.resizable(False, False)

    # getter of chosen filename
    def getFileName(self):
        try:
            return self.__filename.name
        except:
            return None

    # setter of plot type
    def __setPlotType(self, value):
        self.__plotType = value

    # getter of chosen plot type
    def getPlotType(self):
        return self.__plotType

    # shows popup with given title and message
    def openPopup(self, master, title, msg):
        top = tk.Toplevel(master, bg="#6E46F2")
        top.geometry("400x400")
        top.title(title)
        tk.Label(top, text = msg, bg="#6E46F2", font=('Arial 18 bold')).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # displays plot
    def displayPlot(self, plot):
        # hides the color scale that is useless in this case
        plot.update_layout(coloraxis_showscale=False)

        # shows the plot
        plot.show()

    # user chooses input file
    def chooseInputFile(self):
        self.__filename = filedialog.askopenfile(initialdir='/', title="Select File", filetypes=(("Comma separated files", "*.csv"),))

    # asks user whether continue by ommiting invalid values or terminate process
    def handleInvalidInput(self):
        result = tk.messagebox.askyesno(
            title = "Invalid data found",
            message = "Invalid data was found! Do you want to process file and omit invalid rows?",
            detail="If no, you have to specify path to new file"
        )

        return result